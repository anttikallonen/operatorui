#!/bin/sh
docker build --rm -t mydata/operatorui .
docker run --rm -it mydata/operatorui
