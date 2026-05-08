"""Data-driven type classification for stage-1 metadata.

This module is intentionally table-shaped.  Add strings/prefixes/patterns here;
do not scatter type-kind checks through generators.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import re
from typing import Literal

TypeKind = Literal[
    'dynamic_any',
    'same',
    'cinder_scalar',
    'cinder_checked_container',
    'cinder_static_container',
    'python_scalar',
    'python_tuple',
    'python_container',
    'python_user_object',
    'int_enum',
    'iterator',
    'none_only',
    'optional',
    'union',
    'callable',
    'type_alias',
    'dynamic_unknown',
]


@dataclass(frozen=True)
class TypeRule:
    kind: TypeKind
    exact: frozenset[str] = frozenset()
    prefixes: tuple[str, ...] = ()
    contains: tuple[str, ...] = ()
    regexes: tuple[str, ...] = ()

    def matches(self, text: str) -> bool:
        if text in self.exact:
            return True
        if any(text.startswith(prefix) for prefix in self.prefixes):
            return True
        if any(piece in text for piece in self.contains):
            return True
        return any(re.search(pattern, text) for pattern in self.regexes)


@dataclass(frozen=True)
class TypeClassifierConfig:
    normalize_replacements: tuple[tuple[str, str], ...] = (
        ('typing.', ''),
        ('__static__.', ''),
        ('builtins.', ''),
    )
    alias_names: frozenset[str] = frozenset()
    int_enum_names: frozenset[str] = frozenset()
    rules: tuple[TypeRule, ...] = field(default_factory=lambda: DEFAULT_RULES)


DEFAULT_RULES: tuple[TypeRule, ...] = (
    TypeRule('dynamic_unknown', exact=frozenset({'', 'Any', 'Unknown', 'object'})),
    TypeRule('none_only', exact=frozenset({'None', 'NoneType'})),
    TypeRule('optional', prefixes=('Optional[',), contains=(' | None', 'None |')),
    TypeRule('union', prefixes=('Union[',), contains=(' | ',)),
    TypeRule('callable', prefixes=('Callable[',), regexes=(r'^\(.*\)\s*->\s*.+$',)),
    TypeRule('iterator', exact=frozenset({'Iterator', 'Generator'}), prefixes=('Iterator[', 'Generator[', 'Iterable[',)), 
    TypeRule('cinder_scalar', exact=frozenset({
        'int64', 'int32', 'int16', 'int8',
        'uint64', 'uint32', 'uint16', 'uint8',
        'double', 'float64', 'float32', 'cbool',
    })),
    TypeRule('cinder_checked_container', exact=frozenset({'CheckedList', 'CheckedDict'}), prefixes=('CheckedList[', 'CheckedDict[')),
    TypeRule('cinder_static_container', exact=frozenset({'Array', 'Vector'}), prefixes=('Array[', 'Vector[')),
    TypeRule('python_scalar', exact=frozenset({'int', 'float', 'bool', 'str', 'bytes'})),
    TypeRule('python_tuple', exact=frozenset({'tuple', 'Tuple'}), prefixes=('tuple[', 'Tuple[')),
    TypeRule('python_container', exact=frozenset({'list', 'dict', 'set', 'List', 'Dict', 'Set', 'Mapping'}), prefixes=(
        'list[', 'dict[', 'set[',
        'List[', 'Dict[', 'Set[', 'Mapping[',
    )),
)


def normalize_type_name(type_src: str | None, config: TypeClassifierConfig | None = None) -> str:
    if type_src is None:
        return ''
    config = config or TypeClassifierConfig()
    text = type_src.strip()
    for old, new in config.normalize_replacements:
        text = text.replace(old, new)
    return text.strip()


def classify_type_src(type_src: str | None, *, aliases: set[str] | None = None, int_enums: set[str] | None = None, config: TypeClassifierConfig | None = None) -> TypeKind:
    config = config or TypeClassifierConfig(alias_names=frozenset(aliases or ()), int_enum_names=frozenset(int_enums or ()))
    text = normalize_type_name(type_src, config)
    if text in config.alias_names:
        return 'type_alias'
    if text in config.int_enum_names or text.split('.')[-1] in config.int_enum_names:
        return 'int_enum'
    for rule in config.rules:
        if rule.matches(text):
            return rule.kind
    return 'python_user_object'


def classification_metadata(type_src: str | None, *, aliases: set[str] | None = None, int_enums: set[str] | None = None) -> dict[str, str]:
    normalized = normalize_type_name(type_src)
    return {
        'normalized_type_src': normalized,
        'type_kind': classify_type_src(normalized, aliases=aliases, int_enums=int_enums),
    }
