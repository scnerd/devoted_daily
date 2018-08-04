#!/usr/bin/env bash

mkdir -p ./media ./secrets

cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1 > ./secrets/db_password

docker-compose up --build -d
sleep 1
docker-compose exec app ./manage.py createsuperuser
