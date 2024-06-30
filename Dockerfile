FROM python:3.12-slim

COPY requirements.txt /tmp

RUN apt-get update && \
    apt-get -y install libpq-dev gcc git && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY pgoutput-cli.py /usr/bin/pgoutput-cli
