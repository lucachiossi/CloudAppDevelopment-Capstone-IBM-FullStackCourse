FROM nginx:1.19.10

RUN rm /etc/nginx/conf.d/default.conf
COPY ./k8deployment/nginx_server/nginx.conf /etc/nginx/conf.d/default.conf

RUN mkdir /django_app
RUN mkdir /django_app/static
COPY ./server/static /django_app/static
