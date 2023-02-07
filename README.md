# Otus Microservice Architecture course
## hw Docker

Создать минимальный сервис, который
1.  отвечает на порту 8000
2.  имеет http-метод
    GET /health/
    RESPONSE: {"status": "OK"}
    
Cобрать локально образ приложения в докер.
Запушить образ в dockerhub

### Description
Simple shell web server created using `nc`

Image can be found on [DockerHub](https://hub.docker.com/r/refringerator/simple-server/tags)

### How to run
```shell
docker run --rm -p 8000:8000 refringerator/simple-server
```


