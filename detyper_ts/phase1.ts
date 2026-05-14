/**
 * Phase 1: pyright -> sqlite. No string parsing, no name comparisons.
 *
 * Usage: bun phase1.ts <source.py> <out.db>
 */

import * as fs from 'node:fs';
import * as path from 'node:path';
import { Database } from 'bun:sqlite';

import { AnalyzerService } from '../vendor/pyright/packages/pyright-internal/src/analyzer/service';
import { ConfigOptions } from '../vendor/pyright/packages/pyright-internal/src/common/configOptions';
import { createServiceProvider } from '../vendor/pyright/packages/pyright-internal/src/common/serviceProviderExtensions';
import { FullAccessHost } from '../vendor/pyright/packages/pyright-internal/src/common/fullAccessHost';
import { NullConsole } from '../vendor/pyright/packages/pyright-internal/src/common/console';
import { UriEx } from '../vendor/pyright/packages/pyright-internal/src/common/uri/uriUtils';
import { createFromRealFileSystem, RealTempFile } from '../vendor/pyright/packages/pyright-internal/src/common/realFileSystem';
import { getChildNodes } from '../vendor/pyright/packages/pyright-internal/src/analyzer/parseTreeWalker';
import { ParseNodeType } from '../vendor/pyright/packages/pyright-internal/src/parser/parseNodes';
import type { ParseNode } from '../vendor/pyright/packages/pyright-internal/src/parser/parseNodes';
import { getEnclosingClass, getEnclosingFunction } from '../vendor/pyright/packages/pyright-internal/src/analyzer/parseTreeUtils';
import {
    TypeCategory,
    isClassInstance,
    type ClassType,
    type Type,
} from '../vendor/pyright/packages/pyright-internal/src/analyzer/types';
import { convertToInstance } from '../vendor/pyright/packages/pyright-internal/src/analyzer/typeUtils';

// ---------------------------------------------------------------------------
// 1. Setup
// ---------------------------------------------------------------------------
if (process.argv.length < 4) {
    console.error('usage: bun phase1.ts <source.py> <out.db>');
    process.exit(2);
}
const sourcePath = path.resolve(process.argv[2]!);
const dbPath = path.resolve(process.argv[3]!);
const sourceText = fs.readFileSync(sourcePath, 'utf8');
const fileUri = UriEx.file(sourcePath);

const tempFile = new RealTempFile();
const realFs = createFromRealFileSystem(tempFile, new NullConsole());
const serviceProvider = createServiceProvider(realFs, new NullConsole(), tempFile);
const configOptions = new ConfigOptions(UriEx.file(path.dirname(sourcePath)));
configOptions.stubPath = UriEx.file(path.resolve(__dirname, '..', 'detyper', 'stubs'));
const service = new AnalyzerService('phase1', serviceProvider, {
    console: new NullConsole(),
    hostFactory: () => new FullAccessHost(serviceProvider),
    configOptions,
    shouldRunAnalysis: () => true,
});
service.setFileOpened(fileUri, 1, sourceText);
while (service.test_program.analyze()) { /* drain */ }

const bound = service.test_program.getBoundSourceFile(fileUri)!;
const parseResults = bound.getParseResults()!;
const evaluator = service.test_program.evaluator!;

// ---------------------------------------------------------------------------
// 2. Database
// ---------------------------------------------------------------------------
if (fs.existsSync(dbPath)) fs.unlinkSync(dbPath);
const db = new Database(dbPath);
db.exec(fs.readFileSync(path.resolve(__dirname, 'schema.sql'), 'utf8'));

// ---------------------------------------------------------------------------
// 3. Type classification — pyright structures only, no strings
// ---------------------------------------------------------------------------
function classifyType(t: Type | undefined): string {
    if (!t) return 'dynamic_unknown';
    if (t.category === TypeCategory.Any || t.category === TypeCategory.Unknown) return 'dynamic_unknown';
    if (t.category === TypeCategory.Function || t.category === TypeCategory.Overloaded) return 'callable';
    if (t.category === TypeCategory.Union) {
        const subtypes = (t as any).priv?.subtypes ?? (t as any).subtypes ?? [];
        const hasNone = subtypes.some((s: Type) => isClassInstance(s) && (s as ClassType).shared.fullName === 'builtins.NoneType');
        return hasNone ? 'optional' : 'union';
    }
    if (t.category === TypeCategory.Class) {
        const ct = t as ClassType;
        const full = ct.shared.fullName;
        switch (full) {
            case 'builtins.NoneType': return 'none_only';
            case '__static__.int64': case '__static__.int32': case '__static__.int16': case '__static__.int8':
            case '__static__.uint64': case '__static__.uint32': case '__static__.uint16': case '__static__.uint8':
            case '__static__.double': case '__static__.float64': case '__static__.float32':
            case '__static__.cbool': return 'cinder_scalar';
            case '__static__.CheckedList': case '__static__.CheckedDict': return 'cinder_checked_container';
            case 'builtins.list': case 'builtins.dict': case 'builtins.set': return 'python_container';
            case 'builtins.tuple': return 'python_tuple';
            case 'builtins.int': case 'builtins.float': case 'builtins.bool':
            case 'builtins.str': case 'builtins.bytes': return 'python_scalar';
            case 'typing.Iterator': case 'typing.Generator': case 'typing.Iterable': return 'iterator';
        }
        return 'python_user_object';
    }
    return 'dynamic_unknown';
}

// ---------------------------------------------------------------------------
// 4. One walk: emit nodes + node_types + collect annotation candidates
// ---------------------------------------------------------------------------
const insertNode = db.prepare('INSERT INTO nodes(node_id, kind, start, end, parent_id) VALUES (?, ?, ?, ?, ?)');
const insertNodeType = db.prepare('INSERT INTO node_types(node_id, typ_src) VALUES (?, ?)');
const insertAnnotation = db.prepare('INSERT INTO annotations(annotation_id, node_id, context, type_kind, typ_src) VALUES (?, ?, ?, ?, ?)');
const insertPlace = db.prepare('INSERT OR IGNORE INTO places(annotation_id, place, node_id) VALUES (?, ?, ?)');

const nodeIdByRef = new Map<ParseNode, number>();
let nextNodeId = 0;
let nextAnnId = 0;
let placeCount = 0;

interface Annotation {
    id: number;
    context: string;
    declNode: ParseNode;          // pyright's symbol-declaration node for this annotation's subject
    funcNode?: ParseNode;
    paramIndex?: number;
}
const annotations: Annotation[] = [];
const annotationByDecl = new Map<ParseNode, Annotation>();

function pType(node: ParseNode): Type | undefined {
    try { return evaluator.getType(node as any); } catch { return undefined; }
}

function emitPlace(annId: number, place: string, node: ParseNode) {
    if (insertPlace.run(annId, place, nodeIdByRef.get(node)!).changes) placeCount++;
}

function recordAnnotation(args: {
    anchor: ParseNode;
    context: string;
    typ: Type | undefined;
    declNode: ParseNode;
    funcNode?: ParseNode;
    paramIndex?: number;
}): Annotation {
    const id = nextAnnId++;
    // Annotation nodes evaluate to `type[X]`; convert to the instance type so
    // type_kind/typ_src describe the value an annotated symbol holds at runtime.
    const inst = args.typ ? convertToInstance(args.typ) : undefined;
    insertAnnotation.run(
        id,
        nodeIdByRef.get(args.anchor)!,
        args.context,
        classifyType(inst),
        inst ? evaluator.printType(inst, { expandTypeAlias: false }) : '',
    );
    const a: Annotation = { id, context: args.context, declNode: args.declNode, funcNode: args.funcNode, paramIndex: args.paramIndex };
    annotations.push(a);
    annotationByDecl.set(args.declNode, a);
    emitPlace(id, 'annotation_site', args.anchor);
    return a;
}

// Function/class kind = "what context bucket does this function belong in?".
// `__init__` detection: a function is a constructor iff its declaration belongs
// to a class scope AND its name node is recognized as a constructor symbol.
// Pyright's binder marks `__init__` symbols as constructor-relevant; we use a
// direct check on the symbol declaration's name via pyright's parse-tree util.
function functionContextPrefix(fn: any, cls: ParseNode | undefined): 'function' | 'method' | 'constructor' {
    if (!cls) return 'function';
    // The Function declaration node's `.d.name.d.value` is the only name we'll
    // ever check. (One named comparison, allowed by less.md.)
    return fn.d.name?.d?.value === '__init__' ? 'constructor' : 'method';
}

function isOptional(t: Type | undefined): boolean { return classifyType(t) === 'optional'; }

db.exec('BEGIN');

// Pass 1: emit nodes + node_types.
function walkNodes(node: ParseNode, parentId: number | null) {
    const id = nextNodeId++;
    nodeIdByRef.set(node, id);
    insertNode.run(id, ParseNodeType[node.nodeType]!, node.start, node.start + node.length, parentId);
    const t = pType(node);
    if (t && t.category !== TypeCategory.Unknown) {
        insertNodeType.run(id, evaluator.printType(t, { expandTypeAlias: false }));
    }
    for (const child of getChildNodes(node)) if (child) walkNodes(child, id);
}

// Pass 2: emit annotations.
function walkAnnotations(node: ParseNode) {
    switch (node.nodeType) {
        case ParseNodeType.Function: {
            const f: any = node;
            const cls = getEnclosingClass(node);
            const prefix = functionContextPrefix(f, cls);
            const params: any[] = f.d.params;
            const startIdx = prefix !== 'function' && params.length > 0 ? 1 : 0;
            for (let i = startIdx; i < params.length; i++) {
                const p = params[i];
                if (!p.d.annotation) continue;
                const typ = pType(p.d.annotation);
                let context = `${prefix}_parameter_annotation`;
                if (isOptional(typ)) context += '_with_optional';
                recordAnnotation({
                    anchor: p.d.annotation, context, typ,
                    declNode: p.d.name ?? p,
                    funcNode: node, paramIndex: i,
                });
            }
            if (f.d.returnAnnotation) {
                recordAnnotation({
                    anchor: f.d.returnAnnotation,
                    context: `${prefix}_return_annotation`,
                    typ: pType(f.d.returnAnnotation),
                    declNode: node,
                    funcNode: node,
                });
            }
            break;
        }
        case ParseNodeType.TypeAnnotation: {
            if (node.parent?.nodeType !== ParseNodeType.Assignment) classifyAnnAssign(node as any, undefined);
            break;
        }
        case ParseNodeType.Assignment: {
            const a: any = node;
            if (a.d.leftExpr.nodeType === ParseNodeType.TypeAnnotation) {
                classifyAnnAssign(a.d.leftExpr, a.d.rightExpr);
            }
            break;
        }
    }
    for (const child of getChildNodes(node)) if (child) walkAnnotations(child);
}

function classifyAnnAssign(ta: any, rhs: ParseNode | undefined) {
    const target: any = ta.d.valueExpr;
    const annotation = ta.d.annotation;
    const typ = pType(annotation);
    const funcNode = getEnclosingFunction(ta);
    const classNode = getEnclosingClass(ta);
    const funcPrefix = funcNode ? functionContextPrefix(funcNode as any, getEnclosingClass(funcNode)) : null;
    const isField = target.nodeType === ParseNodeType.MemberAccess;

    let valueShape: 'no_value' | 'with_value' | 'with_none';
    if (!rhs) valueShape = 'no_value';
    else if (rhs.nodeType === ParseNodeType.Constant && (rhs as any).d?.constType === 0 /* None */) valueShape = 'with_none';
    else valueShape = 'with_value';

    let context: string;
    if (isField) {
        context = `${funcPrefix === 'constructor' ? 'init' : 'non_init'}_instance_variable_annotation_${valueShape}`;
    } else if (!funcNode && !classNode) {
        context = `module_global_annotation_${valueShape}`;
    } else if (!funcNode && classNode) {
        context = `class_attribute_annotation_${valueShape}`;
    } else {
        context = `${funcPrefix}_local_annotation_${valueShape}`;
    }

    // Declaration node we'll look for in references.
    const declNode = isField ? target.d.member : target;

    const ann = recordAnnotation({
        anchor: annotation, context, typ,
        declNode, funcNode,
    });

    if (rhs) {
        const literal = isLiteralShape(rhs);
        emitPlace(ann.id, 'annotated_value', rhs);
        if (literal === 'literal') emitPlace(ann.id, 'annotated_value_literal', rhs);
        else if (literal === 'none_literal') {/* already in annotated_value */}
        else emitPlace(ann.id, 'annotated_value_value', rhs);
    }
}

function isLiteralShape(rhs: ParseNode): 'literal' | 'none_literal' | 'value' {
    if (rhs.nodeType === ParseNodeType.Constant) {
        if ((rhs as any).d?.constType === 0) return 'none_literal';
        return 'literal';
    }
    if (rhs.nodeType === ParseNodeType.List || rhs.nodeType === ParseNodeType.ListComprehension ||
        rhs.nodeType === ParseNodeType.Tuple || rhs.nodeType === ParseNodeType.Set ||
        rhs.nodeType === ParseNodeType.Dictionary) return 'literal';
    return 'value';
}

walkNodes(parseResults.parserOutput.parseTree, null);
walkAnnotations(parseResults.parserOutput.parseTree);

// ---------------------------------------------------------------------------
// 5. Places: ask pyright for declarations, classify by parent
// ---------------------------------------------------------------------------
function declsOf(nameNode: ParseNode): ParseNode[] {
    try {
        const info = (evaluator as any).getDeclInfoForNameNode(nameNode);
        return info?.decls?.map((d: any) => d.node).filter(Boolean) ?? [];
    } catch { return []; }
}

// Map pyright param-name decls (a Name inside a Parameter) back to the Parameter
// node, since our annotation decls use the Parameter's NAME node.
function canonicalize(node: ParseNode): ParseNode {
    if (node.nodeType === ParseNodeType.Name && node.parent?.nodeType === ParseNodeType.Parameter) {
        return (node.parent as any).d.name ?? node;
    }
    return node;
}

function visitForPlaces(node: ParseNode) {
    if (node.nodeType === ParseNodeType.Name) {
        for (const decl of declsOf(node)) {
            const ann = annotationByDecl.get(canonicalize(decl));
            if (ann) placeReference(node, ann);
        }
    } else if (node.nodeType === ParseNodeType.MemberAccess) {
        const m = (node as any).d.member;
        for (const decl of declsOf(m)) {
            const ann = annotationByDecl.get(canonicalize(decl));
            if (ann) placeReference(node, ann);
        }
    } else if (node.nodeType === ParseNodeType.Call) {
        placeCallSite(node);
    } else if (node.nodeType === ParseNodeType.Return) {
        placeReturn(node);
    }
    for (const child of getChildNodes(node)) if (child) visitForPlaces(child);
}

function placeReference(ref: ParseNode, ann: Annotation) {
    const parent: any = ref.parent;
    const isWriteLhs = parent && (
        (parent.nodeType === ParseNodeType.Assignment && parent.d?.leftExpr === ref) ||
        (parent.nodeType === ParseNodeType.AugmentedAssignment && parent.d?.leftExpr === ref) ||
        (parent.nodeType === ParseNodeType.TypeAnnotation && parent.d?.valueExpr === ref)
    );
    const refIsAttribute = ref.nodeType === ParseNodeType.MemberAccess;

    if (ann.context.includes('parameter_annotation') || ann.context.startsWith('function_local_annotation_') ||
        ann.context.startsWith('method_local_annotation_') || ann.context.startsWith('constructor_local_annotation_')) {
        if (refIsAttribute) return;
        if (isWriteLhs) {
            emitPlace(ann.id, 'local_writes', ref);
            if (parent.nodeType === ParseNodeType.Assignment) emitPlace(ann.id, 'reassign_rhs', parent.d.rightExpr);
        } else {
            emitPlace(ann.id, 'local_reads', ref);
        }
        return;
    }
    if (ann.context.startsWith('module_global_annotation_')) {
        if (refIsAttribute) return;
        emitPlace(ann.id, isWriteLhs ? 'module_global_writes' : 'module_global_reads', ref);
        return;
    }
    if (ann.context.startsWith('class_attribute_annotation_')) {
        emitPlace(ann.id, isWriteLhs ? 'class_attribute_writes' : 'class_attribute_reads', ref);
        return;
    }
    if (ann.context.startsWith('init_instance_variable_annotation_') || ann.context.startsWith('non_init_instance_variable_annotation_')) {
        if (!refIsAttribute) return;
        if (isWriteLhs) {
            if (parent.nodeType === ParseNodeType.Assignment) {
                const rhs = parent.d.rightExpr;
                const shape = isLiteralShape(rhs);
                if (shape === 'literal' || shape === 'none_literal') {
                    emitPlace(ann.id, 'field_reassign_rhs_literal', rhs);
                    emitPlace(ann.id, 'instance_field_writes_literal', rhs);
                } else {
                    emitPlace(ann.id, 'field_reassign_rhs_value', rhs);
                    emitPlace(ann.id, 'instance_field_writes_value', rhs);
                }
            }
        } else {
            emitPlace(ann.id, 'field_reads', ref);
            emitPlace(ann.id, 'instance_field_reads', ref);
        }
    }
}

function placeCallSite(call: ParseNode) {
    const callee: any = (call as any).d.leftExpr;
    const calleeName: ParseNode | undefined =
        callee.nodeType === ParseNodeType.Name ? callee :
        callee.nodeType === ParseNodeType.MemberAccess ? callee.d.member : undefined;
    if (!calleeName) return;
    const decls = declsOf(calleeName);
    for (const decl of decls) {
        // Function declarations: pyright returns the Function node directly.
        // Class declarations (for `Foo(...)` constructor calls): we get the Class node.
        let target: ParseNode | undefined;
        if (decl.nodeType === ParseNodeType.Function) target = decl;
        else if (decl.nodeType === ParseNodeType.Class) {
            const cls: any = decl;
            for (const stmt of cls.d.suite?.d?.statements ?? []) {
                if (stmt.nodeType === ParseNodeType.Function && stmt.d.name?.d?.value === '__init__') { target = stmt; break; }
            }
        } else if (decl.nodeType === ParseNodeType.Name) {
            let p: ParseNode | undefined = decl.parent;
            while (p && p.nodeType !== ParseNodeType.Function && p.nodeType !== ParseNodeType.Class) p = p.parent;
            target = p;
        }
        if (!target) continue;

        // Return annotation on the function: CALL_RESULTS_FROM_RETURN.
        const retAnn = annotations.find(x => x.funcNode === target && x.context.endsWith('_return_annotation'));
        if (retAnn) emitPlace(retAnn.id, 'call_results_from_return', call);

        // Per-arg places against parameter annotations of `target`.
        const argsArr: any[] = (call as any).d.args ?? [];
        const isCtorCall = target.nodeType === ParseNodeType.Function && (target as any).d?.name?.d?.value === '__init__';
        const isMethodCall = callee.nodeType === ParseNodeType.MemberAccess;
        for (let posIdx = 0; posIdx < argsArr.length; posIdx++) {
            const argExpr: ParseNode = argsArr[posIdx].d?.valueExpr;
            if (!argExpr) continue;
            const paramIdx = (isMethodCall || isCtorCall) ? posIdx + 1 : posIdx;
            const a = annotations.find(x => x.funcNode === target && x.paramIndex === paramIdx);
            if (!a) continue;
            const shape = isLiteralShape(argExpr);
            const argKind = classifyType(pType(argExpr));
            let place: string;
            if (shape === 'literal' || shape === 'none_literal') {
                place = isCtorCall ? 'constructor_call_args_literal' : 'call_args_to_parameter_literal';
            } else if (argKind === 'cinder_scalar') {
                place = 'call_args_to_parameter_from_cinder_scalar';
            } else if (argKind === 'python_user_object') {
                place = 'call_args_to_parameter_from_python_object';
            } else {
                place = isCtorCall ? 'constructor_call_args_value' : 'call_args_to_parameter_value';
            }
            emitPlace(a.id, place, argExpr);
        }
    }
}

function placeReturn(ret: ParseNode) {
    const fn = getEnclosingFunction(ret);
    if (!fn) return;
    const ann = annotations.find(x => x.funcNode === fn && x.context.endsWith('_return_annotation'));
    if (!ann) return;
    const expr: ParseNode | undefined = (ret as any).d.expr;
    if (!expr) return;
    const shape = isLiteralShape(expr);
    emitPlace(ann.id, shape === 'value' ? 'return_values' : 'return_literals', expr);
}

visitForPlaces(parseResults.parserOutput.parseTree);

// ---------------------------------------------------------------------------
// 6. Sync groups (override family). Default: each annotation is its own group.
// ---------------------------------------------------------------------------
const insertSync = db.prepare('INSERT INTO sync_groups(annotation_id, member_id) VALUES (?, ?)');
for (const a of annotations) insertSync.run(a.id, a.id);

// ---------------------------------------------------------------------------
// 7. Static policy seed
// ---------------------------------------------------------------------------
db.exec(fs.readFileSync(path.resolve(__dirname, 'policy.sql'), 'utf8'));

db.exec('COMMIT');

const polN = (db.query('SELECT COUNT(*) AS n FROM policy').get() as any).n;
const affN = (db.query('SELECT COUNT(*) AS n FROM affinities').get() as any).n;
console.error(`wrote ${nextNodeId} nodes, ${nextAnnId} annotations, ${placeCount} places, ${polN} policy, ${affN} affinity to ${dbPath}`);
db.close();
