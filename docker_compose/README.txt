requires images cp-django-app:v1 and cp-nginx:v1 correctly built
requires .env file with environment variables for cp-django-app

-> it works because docker-compose creates a network where the containers can communicate with eachother
-> in the nginx.conf file in the cp-nginx container the proxy server is redirected to http://web:8000 and
-> web is how the cp-django-app:v1 container is tagged in docker-compose
