#!/bin/bash




cp -r ../src .
docker build -t mytrac/access_all:latest . 
docker push mytrac/access_all:latest
rm -r src
