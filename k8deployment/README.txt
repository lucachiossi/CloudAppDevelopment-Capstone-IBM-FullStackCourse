eval $(minikube docker-env) -> to point minikube docker daemon
eval $(minikube docker-env -u) -> to go back to local docker daemon

NB: if you get 400: bad request response it is probably because you didn't add minikube ip
to cluster configurations

!!! MUST INCLUDE .env FILE WITH REQUIRED VARIABLES BEFORE RUNNING !!!
-> see env-template for an example

-> 0) GENERATE config-map and secrets
kubectl create cm web-config --from-file=.env

-> 1) APPLY yaml files:
kubectl apply -f nginx-service.yaml,web-service.yaml,nginx-deployment.yaml,web-deployment.yaml

-> 2) ACCESS nginx frontend:
minikube service nginx

-> 3) CLEAN minikube cluster
bash k8clean.sh
