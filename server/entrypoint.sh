#!/bin/sh

# check database up and running
# if [ "$DATABASE" = "postgres" ]; then
#   echo "Waiting for postgres..."

#   while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
#     sleep 0.1
#   done

#   echo "PostgreSQL started"
# fi

# make migrations and migrate the database.
echo "Making migrations and migrating the database."
python manage.py makemigrations djangoapp --noinput 
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput
exec "$@" # execute all environment variables
