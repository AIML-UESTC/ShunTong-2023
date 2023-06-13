#!/bin/bash
docker rmi -f standarddemo
docker build -t standarddemo .
