#!/bin/bash
docker ps | grep 850 | awk '{print $1}' | xargs docker stop
