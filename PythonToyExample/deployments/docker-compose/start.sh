#!/bin/bash


if [[ "$OSTYPE" == *"darwin"* ]]
then
eval $(docker-machine env cigo)
fi

docker-compose up -d
