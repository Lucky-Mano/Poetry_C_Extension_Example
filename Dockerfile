FROM python:slim

LABEL maintainer ""

RUN apt-get update && apt-get upgrade -y \
  && apt-get install build-essential -y \
  && pip install poetry