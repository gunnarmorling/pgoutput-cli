FROM python:3.9-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 pypgoutput

COPY pgoutput-cli.py /usr/bin/pgoutput-cli
