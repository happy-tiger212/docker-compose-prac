# Docker는  Dockerfile에 쓰여있는 이미지 빌드에 필요한 모든 명령을 순서대로 포함한 텍스트 명령어를 읽음으로써 이미지를 자동으로 build 할 수 있다.

# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/