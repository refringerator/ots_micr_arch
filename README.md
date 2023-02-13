# Otus Microservice Architecture course
## hw k8s basic

### TODO
Написать манифесты для деплоя в k8s для этого сервиса.  
Манифесты должны описывать сущности Deployment, Service, Ingress.  
В Deployment могут быть указаны Liveness, Readiness пробы.  
Количество реплик должно быть не меньше 2. Image контейнера должен быть указан с Dockerhub.  
Хост в ингрессе должен быть arch.homework.   
В итоге после применения манифестов GET запрос на http://arch.homework/health должен отдавать {“status”: “OK”}.   

### Results
```
$ curl http://arch.homework/health/
{"status": "OK"}
```

```
$ for i in {1..15}; do curl http://arch.homework/; done
Hello from awesome-deployment-5dd58b4849-cp786!
Hello from awesome-deployment-5dd58b4849-7x926!
Hello from awesome-deployment-5dd58b4849-ggscm!
Hello from awesome-deployment-5dd58b4849-ggscm!
Hello from awesome-deployment-5dd58b4849-7x926!
Hello from awesome-deployment-5dd58b4849-ggscm!
Hello from awesome-deployment-5dd58b4849-7x926!
Hello from awesome-deployment-5dd58b4849-ggscm!
Hello from awesome-deployment-5dd58b4849-7x926!
Hello from awesome-deployment-5dd58b4849-ggscm!
Hello from awesome-deployment-5dd58b4849-ggscm!
Hello from awesome-deployment-5dd58b4849-ggscm!
Hello from awesome-deployment-5dd58b4849-ggscm!
Hello from awesome-deployment-5dd58b4849-ggscm!
Hello from awesome-deployment-5dd58b4849-7x926!
```
