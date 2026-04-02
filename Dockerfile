FROM ubuntu:latest

MAINTAINER "shipulin.a@galileosky.ru"

ENV PATH /usr/local/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

RUN apt-get update                               \
    && apt-get install -y                        \
    python3-pip libpython3.11-dev python3.11-dev   \
    && cd /usr/local/bin                         \
    && ln -s /usr/bin/python3 python

RUN apt-get update          \
    && apt-get install -y   \
    apt-utils bash vim curl \
    git gcc libxslt-dev

COPY . project
RUN pwd && ls -la

RUN pip3 install --upgrade pip
RUN pip3 install virtualenv
RUN virtualenv venv
RUN chmod -R 775 venv/bin/
RUN rm -rf $HOME/.cache/pip3/*
RUN venv/bin/activate
RUN pip3 install -r project/requirements.txt

RUN find project/ -name \*.pyc -delete

RUN pwd && ls -la

VOLUME ["project/src/allure_/allure_results"]

WORKDIR project

CMD tail -f /dev/null
