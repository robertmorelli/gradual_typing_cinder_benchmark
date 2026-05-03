"""Optional AST decoration using Pyright type hovers.

This module is intentionally side-effect-light for the detyping algorithm: it
only attaches best-effort ``pyright_type`` attributes to Python ``ast`` nodes.
Consumers may ignore them, and the transform should be identical when Pyright is
missing or returns no type.
"""

from __future__ import annotations

import ast
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any
from urllib.parse import quote


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

    def initialize(self) -> None:
        self.request('initialize', {
            'processId': None,
            'rootUri': self._root_uri,
            'capabilities': {},
        })
        self.notify('initialized', {})

    def open_file(self, uri: str, text: str) -> None:
        self.notify('textDocument/didOpen', {
            'textDocument': {
                'uri': uri,
                'languageId': 'python',
                'version': 1,
                'text': text,
            }
        })

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


def decorate_ast_with_pyright(tree: ast.AST, source: str, filename: str = 'module.py') -> ast.AST:
    """Attach best-effort ``pyright_type`` attributes to expression nodes.

    If Pyright is unavailable or any LSP interaction fails, every expression node
    still gets ``pyright_type = None`` so downstream code has a stable shape.
    """
    exprs = [node for node in ast.walk(tree) if isinstance(node, ast.expr)]
    for node in exprs:
        setattr(node, 'pyright_type', None)
    setattr(tree, 'pyright_types', {})

    try:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / filename
            path.write_text(source, encoding='utf-8')
            uri = _file_uri(path)
            lsp = _PyrightLsp(Path(tmp))
            try:
                lsp.initialize()
                lsp.open_file(uri, source)
                type_map: dict[tuple[int, int], str] = {}
                for node in exprs:
                    typ = lsp.hover(uri, node.lineno - 1, node.col_offset)
                    if typ:
                        setattr(node, 'pyright_type', typ)
                        type_map[(node.lineno, node.col_offset)] = typ
                setattr(tree, 'pyright_types', type_map)
            finally:
                lsp.close()
    except Exception:
        pass

    return tree
