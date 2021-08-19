# docker command cheatsheet

## todo: 
1. organize notes
2. clean up

## contents
1. running a container
2. container managament
4. working with images
   1. Dockerfile anatomy
   2. tagging
   3. exporting image with tar
   4. image management
5. working with containers
   1. creating a container
   2. starting a container
   3. auto-restarting a container
   4. stopping a container
   5. killing a container
   6. pausing and unpausing a container
   7. cleaning up containers and images
6. exploring docker
   1. docker version
   2. server info
   3. downloading image update
   4. inspecting a container
   5. the shell
   6. return results
   7. getting inside a container
   8. volumes
   9. logging
   10. monitoring
   11. events
7. debugging
8. docker-compose
   1. sample
   2. commands
   3. maintance/auto restart
9. production grade workflow
10. ci/cd
11. multi-container application
12. "dockerizing" multiple services
13. aws

# content  
# running a containger

    docker run -it --name <container> apline
    
    docker run -dt --restart always --name <container> apline
    
    docker run -it --name <container> --rm apline

# container management

    docker ps 
    docker start <container id>
    docker stop <container id>
    
    docker rm <container id>
    
    docker container prune
    
    docker rename <container> <new container>
    
    docker status
    docker status <container>

# working with images

## Dockerfile anatomy
[docker best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

[dockerfile reference](https://docs.docker.com/engine/reference/builder/)

**.dockerignore**

**Comments**

`# from base image node`

**FROM**

`FROM node:11.11.0`

**USER**

`USER root` 

**LABEL**

`LABEL "maintainer"="brent.northcutt@gmail.com"`

**ENV**

`ENV AP /data/app`
`ENV SCRATCH /etc/supervisor/conf.d`

**WORKDIR**

`WORKDIR $AP`

**COPY**

**RUN**

`RUN apt-get -y update`

`RUN apt-get -y install supervisord`
`RUN mkdir -p /var/log/supervisor`

`RUN npm install`

**ADD**

`ADD ./supervisord/conf.d/* $SCRATCH`

`ADD *.js* $AP`

**CMD**

`CMD ["supervisord", "-n"]`

**ENTRYPOINT***

**ARG**

**EXPOSE**

**VOLUME**


_example of simple Dockerfile_

    # syntax=docker/dockerfile:1
    FROM node:12-alpine
    RUN apk add --no-cache python g++ make
    WORKDIR /app
    COPY . .
    RUN yarn install --production
    CMD ["node", "src/index.js"]

# build
`docker build .`

`docker build -t rbnorth/simpleweb .`


`docker build -t example/docker-node-hello:latest .`

_verify_
    
`docker run rbnorth/simpleweb`

## build and run image
    
    docker build -t example/docker-node-hello:latest .
    docker run -d -p 8080:8080 example/docker-node-hello:latest
    curl http://192.168.0.239:8080
    docker ps
    docker stop c4c15c01f3fa
    docker run -d -p 8080:8080 -e WHO="Sean and Karl" example/docker-node-hello:latest
    curl http://192.168.0.239:8080
    docker ps
    docker stop da28794ded4d

## tagging

_tag during build_

`docker build -t rbnorth/docker-node-hello:latest .`

_tag after build_

`docker tag example/docker-node-hello:latest rbnorth/docker-node-hello:latest`

## exporting image with tar

_get docker container id_

`docker container ls -a` 

_tar it up_

`docker export d9c6826e5dd3 -o docker-node-hello.tar`

_inspect contents_

`tar -tvf docker-node-hello.tar`

## image management

_build image_
`docker image build`

_print image history_    
`docker image history`
    

`docker image import`

_inspect image: find were files are being stored_    
    
`docker image inspect`
    
`docker image load`
    
_list local images_    

`docker image ls`

`docker image ls <container>`
    
_cleaning up images_

`docker image prune`

`docker image prune -a`
    
_pushes or pulls newly created image to dockerhub_

`docker image pull`

`docker image push`
    
`docker image rm <container>`
    
`docker image save`
    
`docker image tag`

# working with containers
## creating a container

`docker create -p 6379:6379 redis:latest`

## starting a container

## auto-restarting a containe

## stopping a container

## killing a container

## pausing and unpausing a container

## cleaning up containers and images

# exploring docker

## docker version

`docker version`

## server info

`docker info`

## downloading image update

`docker pull alpine:latest`

## inspecting a container

`docker ps`

`docker inspect <container id>`

## the shell

`docker run -it alpine:latest /bin/bash`

`docker run -it alpine:latest sh`

## return results

`docker run <container id> /bin/cat /etc/passwd`

## getting inside a container

`docker exec -it <containter id> /bin/bash`

`docker exec -it <container id> sh`

## volumes

`docker volume ls`

`docker volume create my-data`

`docker volume inspect my-data`

## logging

`docker logs <container id>`

## monitoring

`docker stats <container id>`

## events

`docker events`

# debugging

# docker-compose

_create a docker-compose file_

`touch docker-compose.yml`

_basic example of a docker-compose.yml_
    version: '3'
    services:
        redis-server:
            image: 'redis'
        node-app:
            build: .
            ports:
            - "4001:8081"

## commands

_start_

`docker-compose up`

`docker-compose up --build`

_run in background_

`docker-compose up -d`

_shutdown/stop_

`docker-compose down`

## maintance/auto restart

    'no'
    always
    on-failure
    unless-stopped

## container status with docker compose

`docker-compose ps`

# production grade workflow

    features --> pull request --> master --> testing --> aws
