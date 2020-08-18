from typing import Any, Optional, Mapping, List, Type, Union, Dict, Callable, TypeVar, Tuple

from django.http.response import HttpResponseBase
from rest_framework.fields import Field
from rest_framework.parsers import BaseParser
from rest_framework.renderers import BaseRenderer
from rest_framework.serializers import Serializer, BaseSerializer

from drf_yasg import openapi
from drf_yasg.inspectors.base import FieldInspector, FilterInspector, PaginatorInspector
from drf_yasg.openapi import Parameter, _IN_any

class no_body: ...
class unset: ...

_T = TypeVar("_T")
_VIEW = TypeVar("_VIEW", bound=Callable[..., HttpResponseBase])
_FUNC = TypeVar("_FUNC", bound=Callable[..., Any])
_SerializerOrClass = Union[Serializer, Type[Serializer]]
_SchemaOrRef = Union[openapi.Schema, openapi.SchemaRef]

def swagger_auto_schema(
    method: Optional[str] = ...,
    methods: Optional[List[str]] = ...,
    auto_schema: Optional[Type] = ...,
    request_body: Optional[Union[_SchemaOrRef, _SerializerOrClass]] = ...,
    query_serializer: Optional[_SerializerOrClass] = ...,
    manual_parameters: Optional[List[openapi.Parameter]] = ...,
    operation_id: Optional[str] = ...,
    operation_description: Optional[str] = ...,
    operation_summary: Optional[str] = ...,
    security: Optional[List[dict]] = ...,  # TODO would pefer to have a more precise type for 'dict'
    deprecated: Optional[bool] = ...,
    responses: Optional[
        Dict[Union[int, str], Union[_SchemaOrRef, openapi.Response, _SerializerOrClass, str, None]]
    ] = ...,
    field_inspectors: Optional[List[Type[FieldInspector]]] = ...,
    filter_inspectors: Optional[List[Type[FilterInspector]]] = ...,
    paginator_inspectors: Optional[List[Type[PaginatorInspector]]] = ...,
    tags: Optional[List[str]] = ...,
    **extra_overrides: Any
) -> Callable[[_VIEW], _VIEW]: ...
def swagger_serializer_method(serializer_or_field: Union[_SerializerOrClass, Field]) -> Callable[[_FUNC], _FUNC]: ...
def is_list_view(path: Any, method: Any, view: Any) -> bool: ...
def guess_response_status(method: str) -> int: ...
def param_list_to_odict(parameters: List[Parameter]) -> Dict[Tuple[str, _IN_any]]: ...
def merge_params(parameters: List[Parameter], overrides: List[Parameter]) -> List[Parameter]: ...
def filter_none(obj: _T) -> _T: ...
def force_serializer_instance(serializer: _SerializerOrClass) -> Serializer: ...
def get_serializer_class(serializer: Optional[_SerializerOrClass]) -> Type[BaseSerializer]: ...
def get_object_classes(
    classes_or_instances: List[Union[type, object]], expected_base_class: Optional[type] = ...
) -> type: ...
def get_consumes(parser_classes: Union[BaseParser, Type[BaseParser]]) -> List[str]: ...
def get_produces(renderer_classes: Union[BaseRenderer, Type[BaseRenderer]]) -> List[str]: ...
def decimal_as_float(field: Field) -> bool: ...
def get_serializer_ref_name(serializer: Serializer) -> Optional[str]: ...
def force_real_str(s: Any, encoding: str = ..., strings_only: bool = ..., errors: str = ...) -> str: ...
def field_value_to_representation(field: Field, value: Any) -> Union[dict, list, str, int, float, bool, None]: ...
def get_field_default(field: Field) -> Any: ...
def dict_has_ordered_keys(obj: Mapping) -> bool: ...
