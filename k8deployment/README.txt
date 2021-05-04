eval $(minikube docker-env) -> to point minikube docker daemon
eval $(minikube docker-env -u) -> to go back to local docker daemon

NB: if you get 400: bad request response it is probably because you didn't add minikube ip
to django's settings.py allowed hosts

1) APPLY yaml files:
apply -f nginx-service.yaml,web-service.yaml,nginx-deployment.yaml,web-deployment.yaml

2) ACCESS nginx frontend:
minikube service nginx
