#!/bin/bash




cp -r ../src .
docker build -t mytrac/python-test:latest . 
docker push mytrac/python-test:latest
rm -r src
