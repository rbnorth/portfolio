# counter-app
Simple flask app that counts web site visits and stored in a default Redis backend. Used in Docker Deep Dive book

## commands

### start containers with doceker-compose
    docker-compose up -d

### list running containers
    docker-compose ps

### top for docker-compose
    docker-compose top

### list container images
    docker image ls

### list containers
    docker container ls

### list container networks
    docker network ls

### list container disk volumes
    docker valume ls

### verify running web server
    curl http://mackine-ip:5000

### shutdown containers with docker-compose
    docker-compose down

### stop containers with docker-compose
    docker-compose stop


**References:**
- Docker Deep Dive book (Compose chapter)
