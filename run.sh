#!/bin/bash

docker kill $(docker ps -q)
docker_clean_ps
docker rmi $(docker images -a -q)

docker-compose down

docker-compose build --no-cache
docker-compose up -d --force-recreate --build