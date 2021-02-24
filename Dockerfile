FROM ubuntu:latest
USER root
WORKDIR /usr/src/app

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin
ENV FLASK_APP=insta-pie-api/src/api/api.py
ENV FLASK_DEBUG=1
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update \
    && apt-get install -y sudo python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip 

RUN adduser --disabled-password --gecos '' docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker

RUN sudo apt-get update 

RUN sudo apt-get -qq -y install firefox
RUN sudo apt-get install firefox-geckodriver

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD python -m flask run --host 0.0.0.0

