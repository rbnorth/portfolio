# docker

## contents
1. README.md
1. angular-app
1. counter-app
1. django-app
1. full-statck

### angular-app

### counter-app
This was a git download from docker deep dive. Where you work with docker-compose.

### django-app

### full-stack


## commands

### run commands

#### basic container run
    docker run alpine

#### run contain and drop into shell
    docker run -it alpine sh

#### run container in background
    docker run -d apline

#### container restart settings
    docker run --restart (always|no|no-failure[:maxretries]|unless-stopped) alpine

#### remove container when exited
    docker run --rm alpine

**References:**
- Docker Deep Dive book 
- Docker: Up and Running book
