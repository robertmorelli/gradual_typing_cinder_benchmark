import * as fs from 'node:fs';
import * as path from 'node:path';
import { AnalyzerService } from '../vendor/pyright/packages/pyright-internal/src/analyzer/service';
import { ConfigOptions } from '../vendor/pyright/packages/pyright-internal/src/common/configOptions';
import { createServiceProvider } from '../vendor/pyright/packages/pyright-internal/src/common/serviceProviderExtensions';
import { FullAccessHost } from '../vendor/pyright/packages/pyright-internal/src/common/fullAccessHost';
import { NullConsole } from '../vendor/pyright/packages/pyright-internal/src/common/console';
import { UriEx } from '../vendor/pyright/packages/pyright-internal/src/common/uri/uriUtils';
import { createFromRealFileSystem, RealTempFile } from '../vendor/pyright/packages/pyright-internal/src/common/realFileSystem';
import { getChildNodes } from '../vendor/pyright/packages/pyright-internal/src/analyzer/parseTreeWalker';
import { ParseNodeType } from '../vendor/pyright/packages/pyright-internal/src/parser/parseNodes';
const sourcePath='../static-python-perf/Benchmark/pystone/advanced/main.py'; const sourceText=fs.readFileSync(sourcePath,'utf8'); const fileUri=UriEx.file(path.resolve(sourcePath));
const tempFile=new RealTempFile(); const fsys=createFromRealFileSystem(tempFile,new NullConsole()); const sp=createServiceProvider(fsys,new NullConsole(),tempFile); const cfg=new ConfigOptions(UriEx.file(path.dirname(path.resolve(sourcePath)))); cfg.stubPath=UriEx.file(path.resolve(__dirname,'..','detyper','stubs')); cfg.typeshedPath=UriEx.file(path.resolve(__dirname,'..','vendor','pyright','packages','pyright-internal','typeshed-fallback')); const svc=new AnalyzerService('x',sp,{console:new NullConsole(),hostFactory:()=>new FullAccessHost(sp),configOptions:cfg,shouldRunAnalysis:()=>true}); svc.setFileOpened(fileUri,1,sourceText); while(svc.test_program.analyze()){}
const pr=svc.test_program.getBoundSourceFile(fileUri)!.getParseResults()!;
function txt(n:any){return sourceText.slice(n.start,n.start+n.length)}
function walk(n:any){ if(n.nodeType===ParseNodeType.Assignment && txt(n).startsWith('PtrGlb:')){console.log('assign',txt(n)); console.log('left',ParseNodeType[n.d.leftExpr.nodeType],txt(n.d.leftExpr)); console.log('right',ParseNodeType[n.d.rightExpr.nodeType],txt(n.d.rightExpr)); console.log('ta ann',ParseNodeType[n.d.leftExpr.d.annotation.nodeType],txt(n.d.leftExpr.d.annotation)); console.log('ta val',ParseNodeType[n.d.leftExpr.d.valueExpr.nodeType],txt(n.d.leftExpr.d.valueExpr));} for(const c of getChildNodes(n)) if(c) walk(c)}
walk(pr.parserOutput.parseTree);
