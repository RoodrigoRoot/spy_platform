FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev \
      gcc make libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir app/
WORKDIR app/
COPY . .
