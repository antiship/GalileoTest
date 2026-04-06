FROM ubuntu:latest

MAINTAINER "shipulin.a@galileosky.ru"

ENV PATH /usr/local/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

RUN apt-get update            \
    && apt-get install -y     \
    apt-utils bash vim curl   \
    git gcc openssh git gcc   \
    build-base libxslt-dev    \
    --no-cache ca-certificates

RUN apt-get update                  \
    && apt-get install -y           \
    python3-pip python3 pip         \
    && cd /usr/local/bin            \
    && ln -s /usr/bin/python python

FROM python:3.13

# install pip
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py
RUN pip install --upgrade pip
RUN pip install virtualenv
RUN virtualenv venv
RUN chmod -R 775 venv/bin/
RUN rm -rf $HOME/.cache/pip3/*
RUN venv/bin/activate

COPY . project
RUN pwd && ls -la

RUN pip install -r project/requirements.txt

RUN find project/ -name \*.pyc -delete

RUN pwd && ls -la

VOLUME ["project/src/allure_/allure_results"]

WORKDIR "./project"

CMD ["tail", "-f", "/dev/null"]
