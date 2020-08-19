from typing import Any, Optional, List, Type, Tuple, Dict, Callable

from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.renderers import BaseRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.openapi import Info
from drf_yasg.renderers import _SpecRenderer

SPEC_RENDERERS: Tuple[Type[_SpecRenderer], ...]
UI_RENDERERS: Dict[str, Tuple[Type[BaseRenderer], ...]]

_View = Callable[..., Response]

class _SchemaView(APIView):
    public: bool
    generator_class = Type[OpenAPISchemaGenerator]
    def get(
        self, request: Request, version: str = ..., format: Optional[Any] = ...  # XXX format is unused?
    ) -> Response: ...
    @classmethod
    def apply_cache(cls, view: _View, cache_timeout: int, cache_kwargs: Dict[str, Any]) -> _View: ...
    @classmethod
    def as_cached_view(cls, cache_timeout: int = ..., cache_kwargs: Dict[str, Any] = ..., **initkwargs) -> _View: ...
    @classmethod
    def without_ui(cls, cache_timeout: int = ..., cache_kwargs: Dict[str, Any] = ...) -> _View: ...
    @classmethod
    def with_ui(cls, renderer: str = ..., cache_timeout: int = ..., cache_kwargs: Dict[str, Any] = ...) -> _View: ...

def deferred_never_cache(view_func: Any): ...
def get_schema_view(
    info: Optional[Info] = ...,
    url: Optional[str] = ...,
    patterns: Optional[Any] = ...,  # TODO
    urlconf: Optional[Any] = ...,  # TODO
    public: bool = ...,
    validators: Optional[List[str]] = ...,
    generator_class: Optional[Type[OpenAPISchemaGenerator]] = ...,
    authentication_classes: Optional[Tuple[Type[BaseAuthentication]]] = ...,
    permission_classes: Optional[Tuple[Type[BasePermission]]] = ...,
) -> _SchemaView: ...
