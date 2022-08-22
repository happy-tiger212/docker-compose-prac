## 진행 순서
### 프로젝트 구성 요소 정의
1. 빈 프로젝트 디렉터리 생성(doc_prac)
2. `Dockerfile` 파일 생성 및 내용 추가
3. `requirements.txt` 파일 생성 및 내용 추가
4. `docker-compose.yml` 파일 생성 및 내용 추가
### Django 프로젝트 만들기 (이미지 빌드하여 Django starter project 만듦)
5. `sudo docker-compose run web django-admin startproject composeexample .` 실행하여 Django 프로젝트 생성
`docker compose run [options] [-v VOLUME...] [-p PORT...] [-e KEY=VAL...] [-l KEY=VALUE...] SERVICE [COMMAND] [ARGS...]`: SERVICE를 start하고, COMMAND 실행
6. 소유권 변경
`sudo chown -R $USER:$USER composeexample manage.py`
### 데이터베이스 연결
7. settings.py에서 DATABASES 수정. 설정은 postgres Docker 이미지에 의해 결정됨.
8. `docker-compose up` 실행: 컨테이너 생성 및 시작
컨테이너 생성 후 서비스의 구성 또는 이미지가 변경된 경우, 컨테이너 `docker-compose up`을 중지하고 다시 생성하여 변경사항을 선택.
### migration
9. django container의 bash 통해(`docker exec -it <컨테이너명> /bin/bash`) `makemigrations`, `migrate` 진행
### django와 postgre SQL 연동
10. `docker exec -it <db컨테이너명> /bin/bash`,`psql -U postgres postgres` 로 postgres 컨테이너 진입
11. 유저 생성 `create user <name> password <password> superuser;`
12. 데이터베이스 생성 `create database <db name> owner <owner name>`
13. postgres에서 나간 후(`quit;`), 해당 db 컨테이너로 이동(`psql -U <user> <database>`)
14. `docker-compose.yml`의 db, user, password 변경
15. `docker-compose up`으로 컨테이너 실행
16. django container의 bash 열어`makemigration`, `migrate` 진행
17. postgreSQL 확인

## 그 외 사항
- `python manage.py makemigrations/migrate`은 `docker exec -it <db 컨테이너> /bin/bash`에서만 가능
- 컨테이너가 실행된 환경에서만 bash에 접근 가능