#!/usr/bin/env bash

mkdir -p ./secrets

cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1 > ./secrets/db_password