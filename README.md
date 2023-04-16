# ots_micr_arch
Otus Microservice Architecture course

Сделать простейший RESTful CRUD по созданию, удалению, просмотру и обновлению пользователей.
Пример API - [https://app.swaggerhub.com/apis/otus55/users/1.0.0](https://app.swaggerhub.com/apis/otus55/users/1.0.0 "https://app.swaggerhub.com/apis/otus55/users/1.0.0")

Добавить базу данных для приложения.

Конфигурация приложения должна хранится в Configmaps.

Доступы к БД должны храниться в Secrets.

Первоначальные миграции должны быть оформлены в качестве Job-ы, если это требуется.

Ingress-ы должны также вести на url arch.homework/


### Env
* Ubuntu 20.04
* Minicube v1.29.0
* Kubectl v1.26.1
* Helm v3.10.1

#### Run app
```shell
minikube start --mount-string "$HOME/postgres-data:/data" --driver=docker --install-addons=true --kubernetes-version=stable

helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace fastapi-project  --create-namespace
  
kubectl apply -R -f k8s/ 
```

#### Get ingress IP
```
kubectl get services --namespace=fastapi-project | awk '/ingress-nginx-controller[[:blank:]]/{print $4}'
```

#### Apply migration job
```
kubectl apply -R -f k8s/job/
```

#### Run tests
```shell
newman run "tests/crud users.postman_collection.json" --env-var "host=http://arch.homework"
```
