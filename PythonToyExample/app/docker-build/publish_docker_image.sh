#!/bin/bash



if [[ "$OSTYPE" == *"darwin"* ]]
then
eval $(docker-machine env cigo)
fi

cp -r ../src .
docker build -t python_test . 
rm -r src
