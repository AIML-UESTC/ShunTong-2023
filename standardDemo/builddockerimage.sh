#!/bin/bash
cp dockerimage/Dockerfile .
docker rmi -f docker rmi -f standarddemo8507
docker build -t standarddemo8507 .
rm Dockerfile

