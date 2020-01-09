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

## Development

Release process: https://twine.readthedocs.io/en/stable/#using-twine

* docker build --tag=drf-yasg-stubs .
* git tag $VERSION -a -m 'Release'
* git push --tags
* docker run --rm -it drf-yasg-stubs twine upload 'dist/*'
