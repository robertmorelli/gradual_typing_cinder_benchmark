"""Source-preserving type analogues for static-analysis-only passes.

These rewrites are only valid when the replacement has exactly the same textual
length as the original, so Pyright locations still map back to original AST
coordinates without a source map.
"""

from __future__ import annotations

import re

ANALOGOUS_TYPE_NAMES: dict[str, str] = {
    # Same length: preserves every downstream line/column coordinate.
    'CheckedList': 'list       ',
    'CheckedDict': 'dict       ',
    'int64': 'int  ',
    'cbool': 'bool ',
    'clen': 'len ',
}

_PATTERN = re.compile(r'\b(' + '|'.join(re.escape(k) for k in ANALOGOUS_TYPE_NAMES) + r')\b(?=\s*\[|\b)')


def analysis_source(source: str) -> str:
    """Return a Pyright-only source with layout-preserving type analogues."""
    lines = source.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.lstrip().startswith(('import ', 'from ')):
            continue
        lines[index] = _PATTERN.sub(lambda match: ANALOGOUS_TYPE_NAMES[match.group(1)], line)
    return ''.join(lines)
