#!/bin/bash

cp -r ../src .
docker build -t python_test . 
rm -r src
