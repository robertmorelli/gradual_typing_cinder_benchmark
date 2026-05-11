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
    ANNOTATED_VALUE_VALUE = 'annotated_value_value'
    ANNOTATED_VALUE_LITERAL = 'annotated_value_literal'
    LOCAL_READS = 'local_reads'
    LOCAL_WRITES = 'local_writes'
    REASSIGN_RHS = 'reassign_rhs'
    FIELD_REASSIGN_RHS_VALUE = 'field_reassign_rhs_value'
    FIELD_REASSIGN_RHS_LITERAL = 'field_reassign_rhs_literal'
    CALL_ARGS_TO_PARAMETER_VALUE = 'call_args_to_parameter_value'
    CALL_ARGS_TO_PARAMETER_LITERAL = 'call_args_to_parameter_literal'
    CALL_ARGS_TO_PARAMETER_FROM_CINDER_SCALAR = 'call_args_to_parameter_from_cinder_scalar'
    CALL_ARGS_TO_PARAMETER_FROM_PYTHON_OBJECT = 'call_args_to_parameter_from_python_object'
    CALL_RESULTS_FROM_RETURN = 'call_results_from_return'
    RETURN_VALUES = 'return_values'
    RETURN_LITERALS = 'return_literals'
    FIELD_READS = 'field_reads'
    ATTRIBUTE_RECEIVERS = 'attribute_receivers'
    SUBSCRIPT_INDICES = 'subscript_indices'
    SUBSCRIPT_RESULTS = 'subscript_results'
    FIELD_WRITES_VALUE = 'field_writes_value'
    FIELD_WRITES_LITERAL = 'field_writes_literal'
    CONSTRUCTOR_CALL_ARGS = 'constructor_call_args'
    CONSTRUCTOR_CALL_ARGS_VALUE = 'constructor_call_args_value'
    CONSTRUCTOR_CALL_ARGS_LITERAL = 'constructor_call_args_literal'
    MODULE_GLOBAL_READS = 'module_global_reads'
    MODULE_GLOBAL_WRITES = 'module_global_writes'
    CLASS_ATTRIBUTE_READS = 'class_attribute_reads'
    CLASS_ATTRIBUTE_WRITES = 'class_attribute_writes'
    OVERRIDE_FAMILY_ANNOTATION_SITES = 'override_family_annotation_sites'
    INSTANCE_FIELD_READS = 'instance_field_reads'
    INSTANCE_FIELD_WRITES_VALUE = 'instance_field_writes_value'
    INSTANCE_FIELD_WRITES_LITERAL = 'instance_field_writes_literal'


class Action(StrEnum):
    REMOVE_ANNOTATION = 'remove_annotation'
    REWRITE_PARAM_BINDING = 'rewrite_param_binding'
    WRAP_RUNTIME_TYPE = 'wrap_runtime_type'
    WRAP_BOX = 'wrap_box'
    WRAP_RUNTIME_TYPE_THEN_BOX = 'wrap_runtime_type_then_box'
    UNWRAP_BOX = 'unwrap_box'
    UNWRAP_CHECKED_RETURN_VALUE = 'unwrap_checked_return_value'
    WRAP_NONNULL_RUNTIME_TYPE = 'wrap_nonnull_runtime_type'


PolicyForPlaces: TypeAlias = dict[Place | str, tuple[Action | str, ...] | list[Action | str]]
PolicyByTarget: TypeAlias = dict[str, PolicyForPlaces]
PolicyBySource: TypeAlias = dict[str, PolicyByTarget]
PolicyTable: TypeAlias = dict[str, PolicyBySource]


PRODUCER_PLACES: set[Place] = {
    Place.LOCAL_READS,
    Place.MODULE_GLOBAL_READS,
    Place.FIELD_READS,
    Place.CLASS_ATTRIBUTE_READS,
    Place.INSTANCE_FIELD_READS,
    Place.SUBSCRIPT_RESULTS,
    Place.CALL_RESULTS_FROM_RETURN,
}

CONSUMER_PLACES: set[Place] = {
    Place.ANNOTATED_VALUE,
    Place.ANNOTATED_VALUE_VALUE,
    Place.ANNOTATED_VALUE_LITERAL,
    Place.REASSIGN_RHS,
    Place.FIELD_REASSIGN_RHS_VALUE,
    Place.FIELD_REASSIGN_RHS_LITERAL,
    Place.CALL_ARGS_TO_PARAMETER_VALUE,
    Place.CALL_ARGS_TO_PARAMETER_LITERAL,
    Place.CALL_ARGS_TO_PARAMETER_FROM_CINDER_SCALAR,
    Place.CALL_ARGS_TO_PARAMETER_FROM_PYTHON_OBJECT,
    Place.SUBSCRIPT_INDICES,
    Place.ATTRIBUTE_RECEIVERS,
    Place.RETURN_VALUES,
    Place.RETURN_LITERALS,
    Place.FIELD_WRITES_VALUE,
    Place.FIELD_WRITES_LITERAL,
    Place.CONSTRUCTOR_CALL_ARGS,
    Place.CONSTRUCTOR_CALL_ARGS_VALUE,
    Place.CONSTRUCTOR_CALL_ARGS_LITERAL,
    Place.MODULE_GLOBAL_WRITES,
    Place.CLASS_ATTRIBUTE_WRITES,
    Place.INSTANCE_FIELD_WRITES_VALUE,
    Place.INSTANCE_FIELD_WRITES_LITERAL,
}

def affinity_for_place(place: Place | str) -> str | None:
    place = Place(place)
    if place in PRODUCER_PLACES:
        return 'producer'
    if place in CONSUMER_PLACES:
        return 'consumer'
    return None


# One big table. No clever shared policy aliases: when a square breaks, edit the
# square bob is looking at.
POLICY: PolicyTable = {
    'class_attribute_annotation_no_value': {
        'cinder_scalar': {
            'dynamic_any': {},
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {},
        },
    },
    'class_attribute_annotation_with_none': {
        'cinder_checked_container': {
            'dynamic_any': {},
        },
        'cinder_scalar': {
            'dynamic_any': {},
        },
        'cinder_static_container': {
            'dynamic_any': {},
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {},
        },
        'union': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
    },
    'class_attribute_annotation_with_value': {
        'cinder_scalar': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type_then_box',),
                Place.ANNOTATED_VALUE_LITERAL: (),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type_then_box',),
                Place.LOCAL_WRITES: ('wrap_box',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {},
        },
    },
    'constructor_local_annotation_no_value': {
        'cinder_scalar': {
            'dynamic_any': {
                Place.LOCAL_READS: ('wrap_runtime_type',),
                Place.LOCAL_WRITES: ('wrap_box',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'constructor_local_annotation_with_none': {
        'cinder_checked_container': {
            'dynamic_any': {},
        },
        'cinder_scalar': {
            'dynamic_any': {},
        },
        'cinder_static_container': {
            'dynamic_any': {},
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {},
        },
        'union': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
    },
    'constructor_local_annotation_with_value': {
        'callable': {
            'dynamic_any': {},
        },
        'cinder_checked_container': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_LITERAL: ('wrap_runtime_type',),
                Place.SUBSCRIPT_INDICES: ('wrap_box',),
                Place.SUBSCRIPT_RESULTS: ('wrap_runtime_type',),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type_then_box',),
                Place.ANNOTATED_VALUE_LITERAL: (),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type_then_box',),
                Place.LOCAL_READS: ('wrap_runtime_type',),
                Place.REASSIGN_RHS: ('wrap_runtime_type_then_box',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'constructor_parameter_annotation': {
        'cinder_checked_container': {
            'dynamic_any': {
                Place.CALL_ARGS_TO_PARAMETER_LITERAL: (),
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type',),
                Place.CONSTRUCTOR_CALL_ARGS_LITERAL: ('wrap_runtime_type',),
                Place.CONSTRUCTOR_CALL_ARGS_VALUE: ('wrap_runtime_type',),
                Place.SUBSCRIPT_INDICES: ('wrap_box',),
                Place.SUBSCRIPT_RESULTS: (),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type_then_box',),
                Place.LOCAL_READS: ('wrap_runtime_type',),
                Place.REASSIGN_RHS: ('wrap_box',),
            },
        },
        'cinder_static_container': {
            'dynamic_any': {
                Place.ANNOTATION_SITE: ('rewrite_param_binding',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'constructor_parameter_annotation_with_optional': {
        'cinder_checked_container': {
            'dynamic_any': {
                Place.CALL_ARGS_TO_PARAMETER_LITERAL: (),
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type',),
                Place.SUBSCRIPT_INDICES: ('wrap_box',),
                Place.SUBSCRIPT_RESULTS: ('wrap_runtime_type',),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type_then_box',),
                Place.LOCAL_READS: ('wrap_runtime_type',),
            },
        },
        'cinder_static_container': {
            'dynamic_any': {
                Place.ANNOTATION_SITE: ('rewrite_param_binding',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'constructor_return_annotation': {
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'none_only': {
            'dynamic_any': {},
        },
    },
    'constructor_self_parameter_annotation': {
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {},
        },
    },
    'function_local_annotation_no_value': {
        'cinder_scalar': {
            'dynamic_any': {
                Place.LOCAL_READS: ('wrap_runtime_type',),
                Place.LOCAL_WRITES: ('wrap_box',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'function_local_annotation_with_none': {
        'cinder_checked_container': {
            'dynamic_any': {},
        },
        'cinder_scalar': {
            'dynamic_any': {},
        },
        'cinder_static_container': {
            'dynamic_any': {},
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {},
        },
        'union': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
    },
    'function_local_annotation_with_value': {
        'callable': {
            'dynamic_any': {},
        },
        'cinder_checked_container': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_LITERAL: ('wrap_runtime_type',),
                Place.SUBSCRIPT_INDICES: ('wrap_box',),
                Place.SUBSCRIPT_RESULTS: ('wrap_runtime_type',),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type_then_box',),
                Place.ANNOTATED_VALUE_LITERAL: (),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type_then_box',),
                Place.LOCAL_READS: ('wrap_runtime_type',),
                Place.REASSIGN_RHS: ('wrap_runtime_type_then_box',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'function_parameter_annotation': {
        'cinder_checked_container': {
            'dynamic_any': {
                Place.CALL_ARGS_TO_PARAMETER_LITERAL: (),
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type',),
                Place.SUBSCRIPT_INDICES: ('wrap_box',),
                Place.SUBSCRIPT_RESULTS: ('wrap_runtime_type',),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type_then_box',),
                Place.LOCAL_READS: ('wrap_runtime_type',),
                Place.REASSIGN_RHS: ('wrap_box',),
            },
        },
        'cinder_static_container': {
            'dynamic_any': {
                Place.ANNOTATION_SITE: ('rewrite_param_binding',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
                Place.FIELD_READS: ('wrap_runtime_type',),
            },
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'function_parameter_annotation_with_optional': {
        'cinder_checked_container': {
            'dynamic_any': {
                Place.CALL_ARGS_TO_PARAMETER_LITERAL: (),
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type',),
                Place.SUBSCRIPT_INDICES: ('wrap_box',),
                Place.SUBSCRIPT_RESULTS: ('wrap_runtime_type',),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type_then_box',),
                Place.LOCAL_READS: ('wrap_runtime_type',),
            },
        },
        'cinder_static_container': {
            'dynamic_any': {
                Place.ANNOTATION_SITE: ('rewrite_param_binding',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'function_return_annotation': {
        'cinder_checked_container': {
            'dynamic_any': {
                Place.CALL_RESULTS_FROM_RETURN: (),
                Place.RETURN_VALUES: (),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
                Place.RETURN_LITERALS: (),
                Place.RETURN_VALUES: ('wrap_runtime_type_then_box',),
            },
        },
        'cinder_static_container': {
            'dynamic_any': {
                Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'none_only': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {
                Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
                Place.RETURN_VALUES: ('wrap_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
                Place.RETURN_VALUES: ('wrap_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {
                Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
                Place.RETURN_VALUES: ('wrap_runtime_type',),
            },
        },
    },
    'init_instance_variable_annotation_no_value': {
        'cinder_scalar': {
            'dynamic_any': {
                Place.INSTANCE_FIELD_READS: ('wrap_runtime_type',),
                Place.INSTANCE_FIELD_WRITES_LITERAL: (),
                Place.INSTANCE_FIELD_WRITES_VALUE: ('wrap_runtime_type_then_box',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {},
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'init_instance_variable_annotation_with_none': {
        'cinder_checked_container': {
            'dynamic_any': {},
        },
        'cinder_scalar': {
            'dynamic_any': {},
        },
        'cinder_static_container': {
            'dynamic_any': {},
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
                Place.FIELD_READS: ('wrap_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
    },
    'init_instance_variable_annotation_with_value': {
        'cinder_checked_container': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: (),
                Place.ANNOTATED_VALUE_LITERAL: ('wrap_runtime_type',),
                Place.FIELD_READS: (),
                Place.LOCAL_READS: (),
                Place.SUBSCRIPT_INDICES: (),
                Place.SUBSCRIPT_RESULTS: (),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type_then_box',),
                Place.ANNOTATED_VALUE_LITERAL: (),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type_then_box',),
                Place.FIELD_READS: ('wrap_runtime_type',),
                Place.FIELD_REASSIGN_RHS_LITERAL: (),
                Place.FIELD_REASSIGN_RHS_VALUE: ('wrap_runtime_type_then_box',),
            },
        },
        'cinder_static_container': {
            'dynamic_any': {
                Place.FIELD_READS: ('wrap_runtime_type',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
                Place.FIELD_READS: ('wrap_runtime_type',),
            },
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.FIELD_READS: ('wrap_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'method_local_annotation_no_value': {
        'cinder_scalar': {
            'dynamic_any': {
                Place.LOCAL_READS: ('wrap_runtime_type',),
                Place.LOCAL_WRITES: ('wrap_box',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'method_local_annotation_with_none': {
        'cinder_checked_container': {
            'dynamic_any': {},
        },
        'cinder_scalar': {
            'dynamic_any': {},
        },
        'cinder_static_container': {
            'dynamic_any': {},
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {},
        },
        'union': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
    },
    'method_local_annotation_with_value': {
        'callable': {
            'dynamic_any': {},
        },
        'cinder_checked_container': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: (),
                Place.ANNOTATED_VALUE_LITERAL: ('wrap_runtime_type',),
                Place.FIELD_READS: (),
                Place.LOCAL_READS: (),
                Place.SUBSCRIPT_INDICES: ('wrap_box',),
                Place.SUBSCRIPT_RESULTS: ('wrap_runtime_type',),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type_then_box',),
                Place.ANNOTATED_VALUE_LITERAL: (),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type_then_box',),
                Place.LOCAL_READS: ('wrap_runtime_type',),
                Place.REASSIGN_RHS: ('wrap_runtime_type_then_box',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'method_parameter_annotation': {
        'cinder_checked_container': {
            'dynamic_any': {
                Place.ANNOTATION_SITE: (),
                Place.CALL_ARGS_TO_PARAMETER_LITERAL: (),
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type',),
                Place.LOCAL_READS: ('wrap_runtime_type',),
                Place.SUBSCRIPT_INDICES: ('wrap_box',),
                Place.SUBSCRIPT_RESULTS: ('wrap_runtime_type',),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type_then_box',),
                Place.LOCAL_READS: ('wrap_runtime_type',),
                Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
            },
        },
        'cinder_static_container': {
            'dynamic_any': {
                Place.ANNOTATION_SITE: ('rewrite_param_binding',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
                Place.CALL_ARGS_TO_PARAMETER_FROM_CINDER_SCALAR: ('wrap_runtime_type_then_box',),
                Place.LOCAL_READS: ('wrap_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'method_parameter_annotation_with_optional': {
        'cinder_checked_container': {
            'dynamic_any': {
                Place.CALL_ARGS_TO_PARAMETER_LITERAL: (),
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type',),
                Place.SUBSCRIPT_INDICES: ('wrap_box',),
                Place.SUBSCRIPT_RESULTS: ('wrap_runtime_type',),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.CALL_ARGS_TO_PARAMETER_VALUE: ('wrap_runtime_type_then_box',),
                Place.LOCAL_READS: ('wrap_runtime_type',),
            },
        },
        'cinder_static_container': {
            'dynamic_any': {
                Place.ANNOTATION_SITE: ('rewrite_param_binding',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'method_return_annotation': {
        'cinder_checked_container': {
            'dynamic_any': {
                Place.CALL_RESULTS_FROM_RETURN: (),
                Place.RETURN_VALUES: (),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
                Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
                Place.RETURN_LITERALS: (),
                Place.RETURN_VALUES: ('wrap_runtime_type_then_box',),
            },
        },
        'cinder_static_container': {
            'dynamic_any': {
                Place.FIELD_READS: ('wrap_runtime_type',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'none_only': {
            'dynamic_any': {
                Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
                Place.RETURN_VALUES: ('wrap_runtime_type_then_box',),
            },
        },
        'optional': {
            'dynamic_any': {
                Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
                Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
                Place.RETURN_VALUES: ('wrap_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
                Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
                Place.RETURN_VALUES: ('wrap_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {
                Place.CALL_RESULTS_FROM_RETURN: ('wrap_runtime_type',),
                Place.OVERRIDE_FAMILY_ANNOTATION_SITES: ('remove_annotation',),
                Place.RETURN_VALUES: ('wrap_runtime_type',),
            },
        },
    },
    'method_self_parameter_annotation': {
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {},
        },
    },
    'module_global_annotation_no_value': {
        'cinder_scalar': {
            'dynamic_any': {},
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {},
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'module_global_annotation_with_none': {
        'cinder_checked_container': {
            'dynamic_any': {},
        },
        'cinder_scalar': {
            'dynamic_any': {},
        },
        'cinder_static_container': {
            'dynamic_any': {},
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
    },
    'module_global_annotation_with_value': {
        'cinder_checked_container': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_LITERAL: ('wrap_runtime_type',),
                Place.CALL_RESULTS_FROM_RETURN: (),
                Place.SUBSCRIPT_INDICES: ('wrap_box',),
                Place.SUBSCRIPT_RESULTS: ('wrap_runtime_type',),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type_then_box',),
                Place.ANNOTATED_VALUE_LITERAL: (),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type_then_box',),
                Place.LOCAL_WRITES: ('wrap_box',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'non_init_instance_variable_annotation_no_value': {
        'cinder_scalar': {
            'dynamic_any': {
                Place.INSTANCE_FIELD_READS: ('wrap_runtime_type',),
                Place.INSTANCE_FIELD_WRITES_LITERAL: (),
                Place.INSTANCE_FIELD_WRITES_VALUE: ('wrap_runtime_type_then_box',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {},
        },
        'union': {
            'dynamic_any': {},
        },
    },
    'non_init_instance_variable_annotation_with_none': {
        'cinder_checked_container': {
            'dynamic_any': {},
        },
        'cinder_scalar': {
            'dynamic_any': {},
        },
        'cinder_static_container': {
            'dynamic_any': {},
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
        'python_container': {
            'dynamic_any': {},
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.ATTRIBUTE_RECEIVERS: ('wrap_nonnull_runtime_type',),
                Place.FIELD_READS: ('wrap_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
            },
        },
    },
    'non_init_instance_variable_annotation_with_value': {
        'cinder_checked_container': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_LITERAL: ('wrap_runtime_type',),
                Place.FIELD_READS: (),
                Place.LOCAL_READS: (),
                Place.SUBSCRIPT_INDICES: (),
                Place.SUBSCRIPT_RESULTS: (),
            },
        },
        'cinder_scalar': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type_then_box',),
                Place.ANNOTATED_VALUE_LITERAL: (),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type_then_box',),
                Place.FIELD_READS: ('wrap_runtime_type',),
                Place.FIELD_REASSIGN_RHS_LITERAL: (),
                Place.FIELD_REASSIGN_RHS_VALUE: ('wrap_runtime_type_then_box',),
            },
        },
        'cinder_static_container': {
            'dynamic_any': {
                Place.FIELD_READS: ('wrap_runtime_type',),
            },
        },
        'dynamic_unknown': {
            'dynamic_any': {},
        },
        'int_enum': {
            'dynamic_any': {},
        },
        'iterator': {
            'dynamic_any': {},
        },
        'optional': {
            'dynamic_any': {},
        },
        'python_container': {
            'dynamic_any': {
                Place.ANNOTATED_VALUE: ('wrap_runtime_type',),
                Place.ANNOTATED_VALUE_VALUE: ('wrap_runtime_type',),
                Place.FIELD_READS: ('wrap_runtime_type',),
            },
        },
        'python_scalar': {
            'dynamic_any': {},
        },
        'python_tuple': {
            'dynamic_any': {},
        },
        'python_user_object': {
            'dynamic_any': {
                Place.FIELD_READS: ('wrap_runtime_type',),
            },
        },
        'union': {
            'dynamic_any': {},
        },
    },
}

def policy_for(context: str, source_kind: str, target_kind: str = 'dynamic_any') -> dict[Place, tuple[Action, ...]]:
    raw = POLICY.get(context, {}).get(source_kind, {}).get(target_kind, {})
    return {
        Place(place): tuple(Action(action) for action in actions)
        for place, actions in raw.items()
    }


def policy_to_json(policy: PolicyForPlaces) -> dict[str, list[str]]:
    return {str(Place(place).value): [Action(action).value for action in actions] for place, actions in policy.items()}
