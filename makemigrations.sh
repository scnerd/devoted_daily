#!/usr/bin/env bash

set -ex

docker-compose -f docker-compose.yml -f makemigrations_compose.yml up --build -d app postgres
sleep 1
docker-compose exec app ./manage.py makemigrations
docker-compose down