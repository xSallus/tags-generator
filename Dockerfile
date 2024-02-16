# syntax=docker/dockerfile:1

FROM alpine:latest
WORKDIR /app

COPY requirements.txt .
COPY run.py .
COPY src ./src
COPY __tests__ ./__tests__

RUN mkdir ./tmp/
RUN apk update && apk add python3 py3-pip
RUN pip install -r requirements.txt --break-system-packages
CMD python3 run.py