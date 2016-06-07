#!/bin/sh
docker build --rm -t mydata/operatorui .
docker run -p 9000:9000 --rm -it mydata/operatorui
