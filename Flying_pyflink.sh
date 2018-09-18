#!/bin/sh
#PROJECT should be named according to the parent folder name
PROJECT=pyflinker
# the p flag of the docker compose should have same name that of the parent folder.i.e here it is pyflinker.
docker-compose -p pyflinker up -d
docker-compose scale taskmanager=$1

#pyflinker_jobmanager_1 is the name of the job manger.
docker exec pyflinker_jobmanager_1 ./bin/pyflink-stream.sh /script/$2 - $1


