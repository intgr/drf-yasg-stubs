<a href="http://mypy-lang.org/">
<img src="http://mypy-lang.org/static/mypy_light.svg" alt="mypy logo" width="300px"/>
</a>

# Typing stubs for drf-yasg library

[![PyPI version](https://badge.fury.io/py/drf-yasg-stubs.svg)](https://badge.fury.io/py/drf-yasg-stubs)
[![Tests status](https://github.com/intgr/drf-yasg-stubs/workflows/Tests/badge.svg?branch=master)](https://github.com/intgr/drf-yasg-stubs/actions?query=workflow:Tests)

PEP 484 type stubs for Mypy and PyCharm.

This package contains type stubs to provide more precise static types and
type inference for
[drf-yasg](https://drf-yasg.readthedocs.io/en/stable/), the OpenAPI/Swagger
generator for Django REST Framework.

## Installation

```bash
pip install drf-yasg-stubs
```

That's all, run Mypy and it should be able to pick up these stubs.

## Changelog

#### 0.1.4 (2021-06-29)
* Allow passing `request_body=no_body` to `swagger_auto_schema` (#14)

  Contributed by Étienne Noss @etene

#### 0.1.3 (2021-01-15)
* Add re-exports to `inspectors/__init__.py` (#13)
* get_schema_view() now expects list arguments instead of tuple, as in
  drf-yasg 1.20 (#11)
* Type hints for OpenAPISchemaGenerator (#10)

#### 0.1.2 (2020-08-19)
* Fixed get_schema_view() arguments authentication_classes, permission_classes (#6)

#### 0.1.1 (2020-08-18)
* Fixed SchemaView method annotations (#2)
* Fixed @swagger_serializer_method decorator hints
* Improved hints for EndpointEnumerator, OpenAPISchemaGenerator

#### 0.1.0 (2020-01-13)
* Initial release

## Development

Release process: https://twine.readthedocs.io/en/stable/#using-twine

* docker build --tag=drf-yasg-stubs .
* docker run --rm -it drf-yasg-stubs twine upload 'dist/*'
* Create tag at https://github.com/intgr/drf-yasg-stubs/releases/new
