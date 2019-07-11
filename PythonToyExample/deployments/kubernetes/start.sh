#!/bin/bash

kubectl apply -f mysql-python-deployment.yaml 

sleep 60

kubectl apply -f python-test-deployment.yaml
