requires images cp-django-app:v1 and cp-nginx:v1 correctly built
!) requires .env file with environment variables for cp-django-app
!) requires environment varables setted in kubernetes .yaml/config map/secrets

cd ~/server
docker build -t cp-django-app:v1 .

cd ~/
docker build . -t cp-nginx:v1 -f k8deployment/nginx_server/Dockerfile

-> it works because docker-compose creates a network where the containers can communicate with eachother
-> in the nginx.conf file in the cp-nginx container the proxy server is redirected to http://web:8000 and
-> web is how the cp-django-app:v1 container is tagged in docker-compose

to translates .yml file into .yaml file for kubernetes deployments run kompose convert
-> this is intended only for initial reference
