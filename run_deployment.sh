#!/usr/bin/env sh

sleep 1

./manage.py migrate
./manage.py initadmin
./manage.py collectstatic --noinput
uwsgi --http :8000 --socket :3031 --module devoted_daily.wsgi