# Docker는  Dockerfile에 쓰여있는 이미지 빌드에 필요한 모든 명령을 순서대로 포함한 텍스트 명령어를 읽음으로써 이미지를 자동으로 build 할 수 있다.

# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# WPRKDIR: 도커 이미지 파일안에서 어떤 디렉토리에 우리 앱을 복사해올건지 명시
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# 도커 명령어는 레이어 시스템이므로, 빈번히 변경되는 파일일수록 나중에 쌓아두는 것이 좋다.
# 왜냐하면 변경된 레이어 전까지는 캐시를 이용하여 재사용하고, 변경된 레이어 부터는 다시 image를 build하기 때문이다.