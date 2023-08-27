FROM python:3.11.5-alpine3.18 as base
LABEL authors="saturnkim"

WORKDIR /opt/app-root/green_note
RUN apk update
RUN apk add gcc musl-dev libffi-dev

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install