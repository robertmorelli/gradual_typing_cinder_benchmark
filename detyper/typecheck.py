"""Optional AST decoration using Pyright type hovers.

This module is intentionally side-effect-light for the detyping algorithm: it
only attaches best-effort ``pyright_type`` attributes to Python ``ast`` nodes.
Consumers may ignore them, and the transform should be identical when Pyright is
missing or returns no type.
"""

from __future__ import annotations

import ast
import json
import tokenize
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any
from urllib.parse import quote

_STUB_ROOT = Path(__file__).resolve().parent / 'stubs'


def _file_uri(path: Path) -> str:
    return 'file://' + quote(str(path.resolve()))


class _PyrightLsp:
    def __init__(self, root: Path, timeout: float = 2.0):
        exe = shutil.which('pyright-langserver')
        if exe is None:
            exe = shutil.which('pyright')
            args = [exe, '--stdio'] if exe else []
        else:
            args = [exe, '--stdio']
        if not args:
            raise FileNotFoundError('pyright-langserver/pyright not found')

        self.timeout = timeout
        self.proc = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=False,
        )
        self._next_id = 1
        self._root_uri = _file_uri(root)

    def close(self) -> None:
        try:
            self.notify('exit', {})
        finally:
            if self.proc.poll() is None:
                self.proc.terminate()

    def _send(self, payload: dict[str, Any]) -> None:
        assert self.proc.stdin is not None
        data = json.dumps(payload).encode('utf-8')
        header = f'Content-Length: {len(data)}\r\n\r\n'.encode('ascii')
        self.proc.stdin.write(header + data)
        self.proc.stdin.flush()

    def _recv(self) -> dict[str, Any] | None:
        assert self.proc.stdout is not None
        headers: dict[str, str] = {}
        while True:
            line = self.proc.stdout.readline()
            if not line:
                return None
            if line == b'\r\n':
                break
            key, _, value = line.decode('ascii').partition(':')
            headers[key.lower()] = value.strip()
        length = int(headers.get('content-length', '0'))
        if length <= 0:
            return None
        return json.loads(self.proc.stdout.read(length).decode('utf-8'))

    def request(self, method: str, params: dict[str, Any]) -> Any:
        req_id = self._next_id
        self._next_id += 1
        self._send({'jsonrpc': '2.0', 'id': req_id, 'method': method, 'params': params})
        while True:
            msg = self._recv()
            if msg is None:
                return None
            if msg.get('id') == req_id:
                return msg.get('result')

    def notify(self, method: str, params: dict[str, Any]) -> None:
        self._send({'jsonrpc': '2.0', 'method': method, 'params': params})

    def initialize(self, stub_path: str | None = None) -> None:
        init_options: dict[str, Any] = {}
        settings: dict[str, Any] = {
            'python': {'analysis': {}},
        }
        if stub_path is not None:
            settings['python']['analysis']['stubPath'] = stub_path
            init_options['stubPath'] = stub_path
        self.request('initialize', {
            'processId': None,
            'rootUri': self._root_uri,
            'workspaceFolders': [{'uri': self._root_uri, 'name': 'root'}],
            'initializationOptions': init_options,
            'capabilities': {},
        })
        self.notify('initialized', {})
        # Push settings via workspace/didChangeConfiguration too — pyright honors both paths.
        self.notify('workspace/didChangeConfiguration', {'settings': settings})

    def open_file(self, uri: str, text: str) -> None:
        self.notify('textDocument/didOpen', {
            'textDocument': {
                'uri': uri,
                'languageId': 'python',
                'version': 1,
                'text': text,
            }
        })

    def locations(self, method: str, uri: str, line: int, character: int) -> list[dict[str, Any]]:
        result = self.request(method, {
            'textDocument': {'uri': uri},
            'position': {'line': line, 'character': character},
        })
        if not result:
            return []
        if isinstance(result, dict):
            result = [result]
        out = []
        for item in result:
            if not isinstance(item, dict):
                continue
            target_uri = item.get('targetUri') or item.get('uri')
            rng = item.get('targetSelectionRange') or item.get('targetRange') or item.get('range')
            if isinstance(target_uri, str) and isinstance(rng, dict):
                out.append({'uri': target_uri, 'range': rng})
        return out

    def definition(self, uri: str, line: int, character: int) -> list[dict[str, Any]]:
        return self.locations('textDocument/definition', uri, line, character)

    def type_definition(self, uri: str, line: int, character: int) -> list[dict[str, Any]]:
        return self.locations('textDocument/typeDefinition', uri, line, character)

    def references(self, uri: str, line: int, character: int) -> list[dict[str, Any]]:
        return self.locations('textDocument/references', uri, line, character)

    def hover(self, uri: str, line: int, character: int) -> str | None:
        result = self.request('textDocument/hover', {
            'textDocument': {'uri': uri},
            'position': {'line': line, 'character': character},
        })
        if not result:
            return None
        contents = result.get('contents')
        if isinstance(contents, str):
            return contents
        if isinstance(contents, dict):
            value = contents.get('value')
            return value if isinstance(value, str) else None
        if isinstance(contents, list):
            parts = []
            for item in contents:
                if isinstance(item, str):
                    parts.append(item)
                elif isinstance(item, dict) and isinstance(item.get('value'), str):
                    parts.append(item['value'])
            return '\n'.join(parts) or None
        return None


def _query_position(node: ast.AST) -> tuple[int, int]:
    line = getattr(node, 'lineno', 1) - 1
    col = getattr(node, 'col_offset', 0)
    if isinstance(node, ast.Attribute):
        # AST col_offset for ``a.b`` points at ``a``.  Pyright hover/definition at
        # that position describes the receiver.  Query the attribute token.
        end_col = getattr(node, 'end_col_offset', None)
        if end_col is not None:
            col = max(col, end_col - len(node.attr))
    elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        col = col + (6 if isinstance(node, ast.AsyncFunctionDef) else 4 if isinstance(node, ast.FunctionDef) else 6)
    return line, col


def decorate_ast_with_pyright(tree: ast.AST, source: str, filename: str = 'module.py') -> ast.AST:
    """Attach best-effort ``pyright_type`` attributes to expression nodes.

    If Pyright is unavailable or any LSP interaction fails, every expression node
    still gets ``pyright_type = None`` so downstream code has a stable shape.
    """
    exprs = [node for node in ast.walk(tree) if isinstance(node, ast.expr)]
    symbol_nodes = [node for node in ast.walk(tree) if isinstance(node, (ast.Name, ast.Attribute, ast.Call, ast.arg, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
    for node in exprs:
        setattr(node, 'pyright_type', None)
    for node in symbol_nodes:
        setattr(node, 'pyright_definitions', [])
        setattr(node, 'pyright_type_definitions', [])
        setattr(node, 'pyright_references', [])
    setattr(tree, 'pyright_types', {})
    setattr(tree, 'pyright_symbol_locations', {})

    try:
        with tempfile.TemporaryDirectory() as tmp:
            # Use the original source unmodified -- pyright resolves __static__
            # symbols via the vendored stub configured in pyrightconfig.json below.
            pyright_source = source
            path = Path(tmp) / filename
            path.write_text(pyright_source, encoding='utf-8')
            # Point pyright at our vendored __static__ stub so CheckedList/int64/
            # cast/etc. resolve to real types instead of being unknown.
            (Path(tmp) / 'pyrightconfig.json').write_text(json.dumps({
                'stubPath': str(_STUB_ROOT),
                'useLibraryCodeForTypes': True,
                'reportMissingImports': 'none',
                'reportMissingTypeStubs': 'none',
            }), encoding='utf-8')
            uri = _file_uri(path)
            lsp = _PyrightLsp(Path(tmp))
            try:
                lsp.initialize(stub_path=str(_STUB_ROOT))
                lsp.open_file(uri, pyright_source)
                type_map: dict[tuple[int, int], str] = {}
                symbol_map: dict[tuple[int, int], dict[str, Any]] = {}
                for node in exprs:
                    line, char = _query_position(node)
                    typ = lsp.hover(uri, line, char)
                    if typ:
                        setattr(node, 'pyright_type', typ)
                        type_map[(node.lineno, node.col_offset)] = typ
                for node in symbol_nodes:
                    line, char = _query_position(node)
                    defs = lsp.definition(uri, line, char)
                    type_defs = lsp.type_definition(uri, line, char)
                    refs = lsp.references(uri, line, char)
                    setattr(node, 'pyright_definitions', defs)
                    setattr(node, 'pyright_type_definitions', type_defs)
                    setattr(node, 'pyright_references', refs)
                    if defs or type_defs or refs:
                        symbol_map[(node.lineno, node.col_offset)] = {
                            'definitions': defs,
                            'type_definitions': type_defs,
                            'references': refs,
                        }
                setattr(tree, 'pyright_types', type_map)
                setattr(tree, 'pyright_symbol_locations', symbol_map)
            finally:
                lsp.close()
    except Exception:
        pass

    return tree
