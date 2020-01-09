FROM python:3.6-buster

ENV PIPENV_VENV_IN_PROJECT=1 PIP_NO_CACHE_DIR=1 CI=true

RUN pip install --upgrade setuptools pip pipenv

WORKDIR /root/pkg
COPY Pipfile /root/pkg/
RUN pipenv install --deploy --dev

COPY . /root/pkg/

RUN pipenv run black --diff --check . && \
    pipenv run flake8
