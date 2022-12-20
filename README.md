# Auth_sprint_1
## Как запустить проект
**1) Склонировать проект**
```commandline
git clone git@github.com:Arkuk/Auth_sprint_1.git
```
**2) Перейти в папку Auth_sprint_1**
```commandline
cd ./Auth_sprint_1
```
**3) Скопировать env**
```commandline
cp .env.example .env
```
**4)  Запустить Docker**
```docker
docker-compose down
docker compose up -d
```
**После запуска вам будет доступна документация**

**[Ссылка на документацию](http://localhost/api/v1/swagger)**


## Как запустить тесты
**1) Склонировать проект(если не склонирован)**
```commandline
git clone git@github.com:Arkuk/Auth_sprint_1.git
```
**2) Перейти в папку Auth_sprint_1/app/tests/functional/**
```commandline
cd ./Auth_sprint_1/app/tests/functional
```
**3)  Запустить Docker**
```docker
docker-compose down
docker-compose up --build -d
```