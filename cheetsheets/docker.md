# docker command cheatsheet

## contents
1. running a container
1. container managament
1. Dockerfile anatomy
1. building an image
1. image management
1. working with containers
1. port mapping
1. connecting to container
   
### run a containger

    docker run -it --name <container> apline
    
    docker run -dt --restart always --name <container> apline
    
    docker run -it --name <container> --rm apline

### container management

    docker start <container>
    docker stop <container>
    
    docker rm <container>
    
    docker container prune
    
    docker rename <container> <new container>
    
    docker status
    docker status <container>

### Dockerfile

**FROM**

`FROM node:11.11.0`

**WORKDIR**

**LABEL**

`LABEL "maintainer"="brent.northcutt@gmail.com"

**USER**

`USER root` 

**ENV**

`ENV AP /data/app`
`ENV SCRATCH /etc/supervisor/conf.d`

**COPY**

**RUN**

**ADD**


**CMD**


### build
    docker build .
    docker build -t brentnorthcutt/simpleweb .

#### verify
    docker run brentnorthcutt/simpleweb


### port mapping
    docker run -p 8080:8080 brentnorthcutt/simpleweb


|incoming request | port inside contianer|
|-----------------|----------------------|
|         8080    |   8080               | 

### connecting to container

run and connect - used for debugging
    
    docker run -it brentnorthcutt/simpleweb sh

connect after container is running
    
    docker ps
    docker exec -it <container id> sh

## docker: up and running notes

### build and run image
    docker build -t example/docker-node-hello:latest .
    docker run -d -p 8080:8080 example/docker-node-hello:latest
    curl http://192.168.0.239:8080
    docker ps
    docker stop c4c15c01f3fa
    docker run -d -p 8080:8080 -e WHO="Sean and Karl" example/docker-node-hello:latest
    curl http://192.168.0.239:8080
    docker ps
    docker stop da28794ded4d

### image management

    docker image build
    
    docker image history
    
    docker image import
    
    docker image inspect
    
    docker image load
    
    docker image ls
    docker image ls <container>
    
    docker image prune
    docker image prune -a
    
    docker image pull
    docker image push
    
    docker image rm <container>
    
    docker image save
    
    docker image tag

