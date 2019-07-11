#!/bin/bash

kubectl delete -f mysql-python-deployment.yaml 

sleep 60

kubectl delete -f python-test-deployment.yaml
