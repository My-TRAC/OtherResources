#!/bin/bash




cp -r ../src .
docker build -t sparsitytechnologies/python-test:latest . 
docker push sparsitytechnologies/python-test:latest
rm -r src
