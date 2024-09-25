FROM python:slim

LABEL maintainer "Lucky-Mano <phatbowie@gmail.com>"

RUN apt-get update \
  && apt-get install -y \
    build-essential \
    clang \
    git \
  && pip install poetry
