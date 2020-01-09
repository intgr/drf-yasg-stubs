from typing import Any, Optional

NotHandled: Any

def is_callable_method(cls_or_instance: Any, method_name: Any): ...
def call_view_method(view: Any, method_name: Any, fallback_attr: Optional[Any] = ..., default: Optional[Any] = ...): ...

class BaseInspector:
    view: Any = ...
    path: Any = ...
    method: Any = ...
    components: Any = ...
    request: Any = ...
    def __init__(self, view: Any, path: Any, method: Any, components: Any, request: Any): ...
    def process_result(self, result: Any, method_name: Any, obj: Any, **kwargs: Any): ...
    def probe_inspectors(
        self, inspectors: Any, method_name: Any, obj: Any, initkwargs: Optional[Any] = ..., **kwargs: Any
    ): ...
    def get_renderer_classes(self): ...
    def get_parser_classes(self): ...

class PaginatorInspector(BaseInspector):
    def get_paginator_parameters(self, paginator: Any): ...
    def get_paginated_response(self, paginator: Any, response_schema: Any): ...

class FilterInspector(BaseInspector):
    def get_filter_parameters(self, filter_backend: Any): ...

class FieldInspector(BaseInspector):
    field_inspectors: Any = ...
    def __init__(self, view: Any, path: Any, method: Any, components: Any, request: Any, field_inspectors: Any): ...
    def add_manual_fields(self, serializer_or_field: Any, schema: Any) -> None: ...
    def field_to_swagger_object(self, field: Any, swagger_object_type: Any, use_references: Any, **kwargs: Any): ...
    def probe_field_inspectors(self, field: Any, swagger_object_type: Any, use_references: Any, **kwargs: Any): ...

class SerializerInspector(FieldInspector):
    def get_schema(self, serializer: Any): ...
    def get_request_parameters(self, serializer: Any, in_: Any): ...

class ViewInspector(BaseInspector):
    body_methods: Any = ...
    implicit_body_methods: Any = ...
    implicit_list_response_methods: Any = ...
    field_inspectors: Any = ...
    filter_inspectors: Any = ...
    paginator_inspectors: Any = ...
    overrides: Any = ...
    def __init__(self, view: Any, path: Any, method: Any, components: Any, request: Any, overrides: Any): ...
    def get_operation(self, operation_keys: Any) -> None: ...
    def is_list_view(self): ...
    def has_list_response(self): ...
    def should_filter(self): ...
    def get_filter_parameters(self): ...
    def should_page(self): ...
    def get_pagination_parameters(self): ...
    def serializer_to_schema(self, serializer: Any): ...
    def serializer_to_parameters(self, serializer: Any, in_: Any): ...
    def get_paginated_response(self, response_schema: Any): ...