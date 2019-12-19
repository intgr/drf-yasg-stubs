from typing import Any, Optional

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help: str = ...
    def add_arguments(self, parser: Any) -> None: ...
    def write_schema(self, schema: Any, stream: Any, format: Any) -> None: ...
    def get_mock_request(self, url: Any, format: Any, user: Optional[Any] = ...): ...
    def get_schema_generator(self, generator_class_name: Any, api_info: Any, api_version: Any, api_url: Any): ...
    def get_schema(self, generator: Any, request: Any, public: Any): ...
    def handle(
        self,
        output_file: Any,
        overwrite: Any,
        format: Any,
        api_url: Any,
        mock: Any,
        api_version: Any,
        user: Any,
        private: Any,
        generator_class_name: Any,
        *args: Any,
        **kwargs: Any
    ) -> None: ...
