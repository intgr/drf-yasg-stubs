from typing import Any, Optional, List, Type, Tuple, Dict

from drf_yasg.openapi import Info

from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework.renderers import BaseRenderer

SPEC_RENDERERS: Tuple[Type[BaseRenderer, ...]]
UI_RENDERERS: Dict[str, Tuple[Type[BaseRenderer, ...]]]

def deferred_never_cache(view_func: Any): ...
def get_schema_view(
    info: Optional[Info] = ...,
    url: Optional[str] = ...,
    patterns: Optional[Any] = ...,  # TODO
    urlconf: Optional[Any] = ...,  # TODO
    public: bool = ...,
    validators: Optional[List[str]] = ...,
    generator_class: Optional[Type[OpenAPISchemaGenerator]] = ...,
    authentication_classes: Optional[List[str]] = ...,
    permission_classes: Optional[List[str]] = ...,
): ...
