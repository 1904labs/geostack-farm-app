---
title: Geospatial Hackathon Collaborative project
layout: default
filename: full-stack.md 
--- 

## Description
If you want to do local development and testing with the full set of 
components (postgis, geosever, and this application) you can deploy
these using the docker-compose template provided

## Prerequisites
1. docker - https://docs.docker.com/get-docker/
2. docker-compose - https://docs.docker.com/compose/install/

## Setup  
__1. build the container__
```bash
docker-compose build
```

__2. pull the postgis and geoserver containers__
```bash
docker-compose pull
```

__3. Launch the stack__
```bash
docker-compose up
```
