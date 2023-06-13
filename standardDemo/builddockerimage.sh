#!/bin/bash
cp dockerimage/Dockerfile .
docker rmi -f docker rmi -f standarddemo
docker build -t standarddemo .

