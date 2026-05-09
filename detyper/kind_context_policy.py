"""Context/source/target policy table for staged detyping/retyping.

Stage 2 reads annotation metadata from ast_data.json, looks up
POLICY[context][source_kind][target_kind], then applies each action to its named
place of interest.
"""

from __future__ import annotations

from enum import StrEnum
from typing import TypeAlias


class Place(StrEnum):
    ANNOTATION_SITE = 'annotation_site'
    ANNOTATED_VALUE = 'annotated_value'
    LOCAL_READS = 'local_reads'
    LOCAL_WRITES = 'local_writes'
    REASSIGN_RHS = 'reassign_rhs'
    FIELD_REASSIGN_RHS = 'field_reassign_rhs'
    FUNCTION_CALL_SITES = 'function_call_sites'
    METHOD_CALL_SITES = 'method_call_sites'
    CALL_ARGS_TO_PARAMETER = 'call_args_to_parameter'
    LITERAL_CALL_ARGS_TO_PARAMETER = 'literal_call_args_to_parameter'
    CALL_ARGS_TO_PARAMETER_FROM_CINDER_SCALAR = 'call_args_to_parameter_from_cinder_scalar'
    CALL_ARGS_TO_PARAMETER_FROM_PYTHON_OBJECT = 'call_args_to_parameter_from_python_object'
    CALL_RESULTS_FROM_RETURN = 'call_results_from_return'
    RETURN_VALUES = 'return_values'
    FIELD_READS = 'field_reads'
    ATTRIBUTE_RECEIVERS = 'attribute_receivers'
    FIELD_WRITES = 'field_writes'
    CONSTRUCTOR_CALL_ARGS = 'constructor_call_args'
    MODULE_GLOBAL_READS = 'module_global_reads'
    MODULE_GLOBAL_WRITES = 'module_global_writes'
    CLASS_ATTRIBUTE_READS = 'class_attribute_reads'
    CLASS_ATTRIBUTE_WRITES = 'class_attribute_writes'
    OVERRIDE_FAMILY_ANNOTATION_SITES = 'override_family_annotation_sites'
    INSTANCE_FIELD_READS = 'instance_field_reads'
    INSTANCE_FIELD_WRITES = 'instance_field_writes'


class Action(StrEnum):
    REMOVE_ANNOTATION = 'remove_annotation'
    REWRITE_PARAM_BINDING = 'rewrite_param_binding'
    WRAP_RUNTIME_TYPE = 'wrap_runtime_type'
    WRAP_BOX = 'wrap_box'
    WRAP_RUNTIME_TYPE_THEN_BOX = 'wrap_runtime_type_then_box'
    UNWRAP_BOX = 'unwrap_box'
    PRESERVE_ARGUMENT_MUTATIONS = 'preserve_argument_mutations'
    UNWRAP_CHECKED_RETURN_VALUE = 'unwrap_checked_return_value'
    WRAP_NONNULL_RUNTIME_TYPE = 'wrap_nonnull_runtime_type'


PolicyForPlaces: TypeAlias = dict[Place | str, tuple[Action | str, ...] | list[Action | str]]
PolicyByTarget: TypeAlias = dict[str, PolicyForPlaces]
PolicyBySource: TypeAlias = dict[str, PolicyByTarget]
PolicyTable: TypeAlias = dict[str, PolicyBySource]


# One big table. No clever shared policy aliases: when a square breaks, edit the
# square bob is looking at.
POLICY: PolicyTable = {
    'function_parameter_annotation': {
        'cinder_scalar': {'dynamic_any': {
            Place.LOCAL_READS: ('wrap_runtime_type',),
            Place.CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type_then_box',),
            Place.REASSIGN_RHS: ('wrap_box',),
        }},
        'cinder_checked_container': {'dynamic_any': {
            Place.ANNOTATION_SITE: ('rewrite_param_binding',),
            Place.CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type',),
            Place.LITERAL_CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type',),
        }},
        'cinder_static_container': {'dynamic_any': {
            Place.ANNOTATION_SITE: ('rewrite_param_binding',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {
            Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
            Place.FIELD_READS: ('wrap_runtime_type',),
        }},
        'python_user_object': {'dynamic_any': {
            Place.LOCAL_READS: ('wrap_runtime_type',),
        }},
        'optional': {'dynamic_any': {}},
        'union': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
    'method_self_parameter_annotation': {
        'python_user_object': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
    'method_parameter_annotation': {
        'cinder_scalar': {'dynamic_any': {
            Place.LOCAL_READS: ('wrap_runtime_type',),
            Place.CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type_then_box',),
            Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
        }},
        'cinder_checked_container': {'dynamic_any': {
            Place.ANNOTATION_SITE: ('rewrite_param_binding',),
            Place.CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type',),
            Place.LITERAL_CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type',),
        }},
        'cinder_static_container': {'dynamic_any': {
            Place.ANNOTATION_SITE: ('rewrite_param_binding',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'python_user_object': {'dynamic_any': {
            Place.LOCAL_READS: ('wrap_runtime_type',),
            Place.CALL_ARGS_TO_PARAMETER_FROM_CINDER_SCALAR: ('wrap_runtime_type_then_box',),
        }},
        'optional': {'dynamic_any': {}},
        'union': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
    'constructor_self_parameter_annotation': {
        'python_user_object': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
    'constructor_parameter_annotation': {
        'cinder_scalar': {'dynamic_any': {
            Place.LOCAL_READS: ('wrap_runtime_type',),
            Place.CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type_then_box',),
            Place.REASSIGN_RHS: ('wrap_box',),
        }},
        'cinder_checked_container': {'dynamic_any': {
            Place.ANNOTATION_SITE: ('rewrite_param_binding',),
            Place.CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type',),
            Place.LITERAL_CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type',),
        }},
        'cinder_static_container': {'dynamic_any': {
            Place.ANNOTATION_SITE: ('rewrite_param_binding',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'python_user_object': {'dynamic_any': {}},
        'optional': {'dynamic_any': {}},
        'union': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
    'function_return_annotation': {
        'cinder_scalar': {'dynamic_any': {
            Place.RETURN_VALUES: ('wrap_runtime_type_then_box',),
            Place.FUNCTION_CALL_SITES: ('wrap_runtime_type',),
            Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
        }},
        'cinder_checked_container': {'dynamic_any': {
            Place.RETURN_VALUES: ('wrap_runtime_type',),
            Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
        }},
        'cinder_static_container': {'dynamic_any': {
            Place.FUNCTION_CALL_SITES: ('wrap_runtime_type',),
            Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'python_user_object': {'dynamic_any': {
            Place.RETURN_VALUES: ('wrap_runtime_type',),
            Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
        }},
        'optional': {'dynamic_any': {
            Place.RETURN_VALUES: ('wrap_runtime_type',),
            Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
        }},
        'union': {'dynamic_any': {
            Place.RETURN_VALUES: ('wrap_runtime_type',),
            Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
        }},
        'none_only': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
    'method_return_annotation': {
        'cinder_scalar': {'dynamic_any': {
            Place.RETURN_VALUES: ('wrap_runtime_type_then_box',),
            Place.FUNCTION_CALL_SITES: ('wrap_runtime_type',),
            Place.METHOD_CALL_SITES: ('wrap_runtime_type',),
            Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
            Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
        }},
        'cinder_checked_container': {'dynamic_any': {
            Place.RETURN_VALUES: ('wrap_runtime_type',),
            Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
        }},
        'cinder_static_container': {'dynamic_any': {
            Place.FIELD_READS: ('wrap_runtime_type',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'python_user_object': {'dynamic_any': {
            Place.RETURN_VALUES: ('wrap_runtime_type',),
            Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
            Place.METHOD_CALL_SITES: ('wrap_runtime_type',),
            Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
        }},
        'optional': {'dynamic_any': {
            Place.RETURN_VALUES: ('wrap_runtime_type',),
            Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
            Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
        }},
        'union': {'dynamic_any': {
            Place.RETURN_VALUES: ('wrap_runtime_type',),
            Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
            Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
        }},
        'none_only': {'dynamic_any': {
            Place.RETURN_VALUES: ('wrap_box',),
            Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
        }},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
    'constructor_return_annotation': {
        'none_only': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
}

for context in [
    'function_local_annotation_no_value', 'method_local_annotation_no_value', 'constructor_local_annotation_no_value',
]:
    POLICY[context] = {
        'cinder_scalar': {'dynamic_any': {
            Place.LOCAL_READS: ('wrap_runtime_type',),
            Place.LOCAL_WRITES: ('wrap_box',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'python_user_object': {'dynamic_any': {}},
        'optional': {'dynamic_any': {}},
        'union': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    }

for context in [
    'function_local_annotation_with_value', 'method_local_annotation_with_value', 'constructor_local_annotation_with_value',
]:
    POLICY[context] = {
        'cinder_scalar': {'dynamic_any': {
            Place.ANNOTATED_VALUE: ('wrap_runtime_type_then_box',),
            Place.LOCAL_READS: ('wrap_runtime_type',),
            Place.REASSIGN_RHS: ('wrap_runtime_type_then_box',),
        }},
        'cinder_checked_container': {'dynamic_any': {
            Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'python_user_object': {'dynamic_any': {}},
        'optional': {'dynamic_any': {}},
        'union': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    }

POLICY.update({
    'module_global_annotation_no_value': {
        'cinder_scalar': {'dynamic_any': {}},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'python_user_object': {'dynamic_any': {}},
        'optional': {'dynamic_any': {}},
        'union': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
    'module_global_annotation_with_value': {
        'cinder_scalar': {'dynamic_any': {
            Place.ANNOTATED_VALUE: ('wrap_runtime_type_then_box',),
            Place.LOCAL_WRITES: ('wrap_box',),
        }},
        'cinder_checked_container': {'dynamic_any': {
            Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
            Place.LOCAL_READS: ('wrap_runtime_type',),
            Place.MODULE_GLOBAL_READS: ('wrap_runtime_type',),
            Place.FUNCTION_CALL_SITES: ('preserve_argument_mutations',),
            Place.METHOD_CALL_SITES: ('preserve_argument_mutations',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'python_user_object': {'dynamic_any': {
            Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
        }},
        'optional': {'dynamic_any': {}},
        'union': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
    'class_attribute_annotation_no_value': {
        'cinder_scalar': {'dynamic_any': {}},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'python_user_object': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
    'class_attribute_annotation_with_value': {
        'cinder_scalar': {'dynamic_any': {
            Place.ANNOTATED_VALUE: ('wrap_runtime_type_then_box',),
            Place.LOCAL_WRITES: ('wrap_box',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'python_user_object': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    },
})

for context in [
    'init_instance_variable_annotation_no_value', 'non_init_instance_variable_annotation_no_value',
]:
    POLICY[context] = {
        'cinder_scalar': {'dynamic_any': {
            Place.INSTANCE_FIELD_WRITES: ('wrap_runtime_type_then_box',),
            Place.INSTANCE_FIELD_READS: ('wrap_runtime_type',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'python_user_object': {'dynamic_any': {}},
        'optional': {'dynamic_any': {}},
        'union': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    }

for context in [
    'init_instance_variable_annotation_with_value', 'non_init_instance_variable_annotation_with_value',
]:
    POLICY[context] = {
        'cinder_scalar': {'dynamic_any': {
            Place.ANNOTATED_VALUE: ('wrap_runtime_type_then_box',),
            Place.FIELD_REASSIGN_RHS: ('wrap_runtime_type_then_box',),
            Place.FIELD_READS: ('wrap_runtime_type',),
        }},
        'cinder_checked_container': {'dynamic_any': {}},
        'cinder_static_container': {'dynamic_any': {
            Place.FIELD_READS: ('wrap_runtime_type',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {
            Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
            Place.FIELD_READS: ('wrap_runtime_type',),
        }},
        'python_user_object': {'dynamic_any': {
            Place.FIELD_READS: ('wrap_runtime_type',),
        }},
        'optional': {'dynamic_any': {}},
        'union': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    }

# IntEnum is not normal object. It is object-shaped to typechecker but int-like
# and identity-sensitive at runtime. Casts around IntEnum state changed
# DeltaBlue's planner direction decisions, so detyping IntEnum is annotation-only
# unless a future benchmark proves a specific boundary needs help.
for _context, _by_source in POLICY.items():
    if 'python_user_object' in _by_source:
        _by_source.setdefault('int_enum', {'dynamic_any': {}})


for context in [
    'module_global_annotation_with_none',
    'class_attribute_annotation_with_none',
    'function_local_annotation_with_none',
    'method_local_annotation_with_none',
    'constructor_local_annotation_with_none',
    'init_instance_variable_annotation_with_none',
    'non_init_instance_variable_annotation_with_none',
]:
    POLICY[context] = {
        'optional': {'dynamic_any': {
            Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
        }},
        'union': {'dynamic_any': {
            Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
        }},
        'python_user_object': {'dynamic_any': {}},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'cinder_scalar': {'dynamic_any': {}},
        'cinder_checked_container': {'dynamic_any': {}},
        'cinder_static_container': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    }


POLICY['module_global_annotation_with_none']['python_user_object'] = {'dynamic_any': {
    Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
}}
for _context in ['init_instance_variable_annotation_with_none', 'non_init_instance_variable_annotation_with_none']:
    POLICY[_context]['python_user_object'] = {'dynamic_any': {
        Place.FIELD_READS: ('wrap_runtime_type',),
    }}


for _context in ['function_parameter_annotation', 'method_parameter_annotation', 'constructor_parameter_annotation']:
    if 'python_user_object' in POLICY.get(_context, {}):
        POLICY[_context]['python_user_object']['dynamic_any'][Place.ATTRIBUTE_RECEIVERS] = ('wrap_nonnull_runtime_type',)
for _context in ['init_instance_variable_annotation_with_none', 'non_init_instance_variable_annotation_with_none']:
    POLICY[_context]['python_user_object']['dynamic_any'][Place.ATTRIBUTE_RECEIVERS] = ('wrap_nonnull_runtime_type',)


for _context in [
    'function_local_annotation_no_value', 'method_local_annotation_no_value', 'constructor_local_annotation_no_value',
    'function_local_annotation_with_value', 'method_local_annotation_with_value', 'constructor_local_annotation_with_value',
]:
    if 'python_user_object' in POLICY.get(_context, {}):
        POLICY[_context]['python_user_object']['dynamic_any'][Place.ATTRIBUTE_RECEIVERS] = ('wrap_nonnull_runtime_type',)


for _context in ['function_parameter_annotation_with_optional', 'method_parameter_annotation_with_optional', 'constructor_parameter_annotation_with_optional']:
    POLICY[_context] = {
        'python_user_object': {'dynamic_any': {
            Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
        }},
        'python_scalar': {'dynamic_any': {}},
        'python_tuple': {'dynamic_any': {}},
        'python_container': {'dynamic_any': {}},
        'cinder_scalar': {'dynamic_any': {
            Place.LOCAL_READS: ('wrap_runtime_type',),
            Place.CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type_then_box',),
        }},
        'cinder_checked_container': {'dynamic_any': {
            Place.ANNOTATION_SITE: ('rewrite_param_binding',),
            Place.CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type',),
            Place.LITERAL_CALL_ARGS_TO_PARAMETER: ('wrap_runtime_type',),
        }},
        'cinder_static_container': {'dynamic_any': {
            Place.ANNOTATION_SITE: ('rewrite_param_binding',),
        }},
        'optional': {'dynamic_any': {
            Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
        }},
        'union': {'dynamic_any': {}},
        'iterator': {'dynamic_any': {}},
        'dynamic_unknown': {'dynamic_any': {}},
    }


def policy_for(context: str, source_kind: str, target_kind: str = 'dynamic_any') -> dict[Place, tuple[Action, ...]]:
    raw = POLICY.get(context, {}).get(source_kind, {}).get(target_kind, {})
    return {
        Place(place): tuple(Action(action) for action in actions)
        for place, actions in raw.items()
    }


def policy_to_json(policy: PolicyForPlaces) -> dict[str, list[str]]:
    return {str(Place(place).value): [Action(action).value for action in actions] for place, actions in policy.items()}
