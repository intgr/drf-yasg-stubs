FROM python:3.6-buster

ENV PIPENV_VENV_IN_PROJECT=1 PIP_NO_CACHE_DIR=1 CI=true

RUN pip install --upgrade setuptools pip

WORKDIR /root/pkg
COPY requirements-test.txt /root/pkg/
RUN pip install -r requirements-test.txt

COPY . /root/pkg/

# TODO how can I ignore DeprecationWarning but error on other warnings?
RUN black --diff --check . && \
    flake8 && \
    python -W error::UserWarning setup.py sdist bdist_wheel && \
    twine check dist/*
