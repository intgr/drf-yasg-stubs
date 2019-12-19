from typing import Any, Optional

SPEC_RENDERERS: Any
UI_RENDERERS: Any

def deferred_never_cache(view_func: Any): ...
def get_schema_view(
    info: Optional[Any] = ...,
    url: Optional[Any] = ...,
    patterns: Optional[Any] = ...,
    urlconf: Optional[Any] = ...,
    public: bool = ...,
    validators: Optional[Any] = ...,
    generator_class: Optional[Any] = ...,
    authentication_classes: Optional[Any] = ...,
    permission_classes: Optional[Any] = ...,
): ...
