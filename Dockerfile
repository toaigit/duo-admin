FROM python:slim-buster

RUN pip install duo_client && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get --no-install-recommends install -y vim && \
    mkdir /tmp/workdir
WORKDIR /tmp/workdir
