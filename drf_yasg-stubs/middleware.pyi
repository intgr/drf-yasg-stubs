from typing import Any

class SwaggerExceptionMiddleware:
    get_response: Any = ...
    def __init__(self, get_response: Any): ...
    def __call__(self, request: Any): ...
    def process_exception(self, request: Any, exception: Any): ...