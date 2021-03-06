from typing import Any, Optional, Callable, Dict, OrderedDict

from ruamel import yaml

class _SwaggerSpecDict(OrderedDict): ...

VALIDATORS: Dict[str, Callable[[_SwaggerSpecDict], None]]

class _OpenAPICodec:
    media_type: str = ...
    def __init__(self, validators: Any): ...
    @property
    def validators(self): ...
    def encode(self, document: Any): ...
    def encode_error(self, err: Any): ...
    def generate_swagger_object(self, swagger: Any): ...

class OpenAPICodecJson(_OpenAPICodec):
    pretty: bool = ...
    def __init__(self, validators: Any, pretty: bool = ..., media_type: str = ...): ...

YAML_MAP_TAG: str

class SaneYamlDumper(yaml.SafeDumper):
    def ignore_aliases(self, data: Any): ...
    def increase_indent(self, flow: bool = ..., indentless: bool = ..., **kwargs: Any): ...
    def represent_odict(self, mapping: Any, flow_style: Optional[Any] = ...): ...

def yaml_sane_dump(data: Any, binary: Any): ...

class SaneYamlLoader(yaml.SafeLoader):
    def construct_odict(self, node: Any, deep: bool = ...): ...

def yaml_sane_load(stream: Any): ...

class OpenAPICodecYaml(_OpenAPICodec):
    media_type: str = ...
    def __init__(self, validators: Any, media_type: str = ...): ...
