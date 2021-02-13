FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/src/app

WORKDIR /src/

COPY ./requirements/prod.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt --disable-pip-version-check

COPY ./app /src
