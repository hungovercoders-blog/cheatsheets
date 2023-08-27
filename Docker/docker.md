# Docker Cheat Sheet

- [Docker Cheat Sheet](#docker-cheat-sheet)
  - [Useful Links](#useful-links)
  - [General](#general)
  - [Images](#images)
  - [Containers](#containers)
  - [Docker Hub](#docker-hub)
  - [Volumes](#volumes)
  - [Docker Compose](#docker-compose)
  - [Docker File](#docker-file)
  - [Docker Compose File](#docker-compose-file)
  - [Save Space Locally](#save-space-locally)
  - [Network](#network)

Primarily taken from [here](https://docs.docker.com/get-started/docker_cheatsheet.pdf) on the docker site but added more as necessary.

## Useful Links

- [Docker Hub](https://hub.docker.com/)
- [Official Docker Images Available](https://hub.docker.com/search?image_filter=official&q=)
- [Docker Desktop](https://docs.docker.com/get-docker/)
- [Docker VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) - You can do so much with this!!!!
- [Play with Docker](https://labs.play-with-docker.com/)
- [Play with Kubernetes](https://labs.play-with-k8s.com/)
- [DockerCon](https://www.dockercon.com/)
- [kubeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)

## General

```bash
docker -d ## started docker daemon
docker --help ## get help
docker info ## system wide info
docker version
```

## Images

```bash
docker build --help ## get help
docker build -t image_name:tag . ## build an image from a dockerfile, the "t" stands for tag
docker build -t image_name:tag -f mycustom.dockerfile . ## build an image from a custom named docker file
docker build -t image_name:tag . --no-cache ## force rebuild an image from a dockerfile
docker images ## list local images
docker rmi image_name ## remove image
docker rmi imageid ## remove image
docker image prune ## remove unused docker images
```

## Containers

```bash
docker run --help ## get help
docker run -d -p ext_port:int_port --name container_name image_name ## run docker image with name
docker run -d -p ext_port:int_port --name container_name --net=network_name image_name ## run docker image with name in a network ##
docker run -d --net=learn01 --name mongodb mongo ##run mongo with no ports specified and will pull down if don't have locally, name important here for connection strings
docker run -d -p 80:80 --name docker/getting-started docker/getting-started  ## run getting started image on a container with specific port. The d switch means is not blocking iso allows you to run more commands.
docker run --rm -it -p ext_port:int_port/tcp image_name:latest ## run image interactive. The external port will be what expose outside (e.g. localhost), the internal port is what the app runs on inside
docker start container_name ## start container
docker stop container_name ## stop container
docker rm container_name ## remove container
docker ps ## list running containers
docker ps --all ## list running and stopped containers
docker logs -f container_id ## get logs and watch container, very useful
docker inspect container_name ## inspect running container
docker container stats ## view resource stats
docker exec -it container_name sh ## open up container and interact with it through bash (Interactive Terminal) to see directories etc e.g. ls, cd.., ls etc. Type exit to exit.
docker container prune ## remove all stopped containers
```

## Docker Hub

```bash
docker login -u {dockername} ## login to docker hub
docker build -t {dockerregistry}/image_name:tag . ## build image and you can use tag to add version
docker push {dockerregistry}/image_name:tag ## push to docker hub with tag of version
docker tag {dockerregistry}/image_name:oldtag {dockerregistry}/image_name:newtag ## tag image on docker
docker search image_name ## search on docker hub
docker pull {dockerregistry}/image_name:tag ## pull image from docker hub
```

## Volumes

```bash
docker run -p ext_port:int_port/tcp -v /place/data image_name:latest # add volume command to write data somewhere for state
docker run -p ext_port:int_port/tcp -v "${PWD}/myfolder:/place/data" image_name:latest # windows print working directory, use the current directory instead of "place/data" - make sure in the current directory when running!
docker run -p ext_port:int_port/tcp -v "$(PWD)/myfolder:/place/data" image_name:latest # mac/linux print working directory, use the current directory instead of "place/data" - make sure in the current directory when running!
```

## Docker Compose

```bash
docker compose --help
docker compose build
docker compose build -f file_name
docker compose up
docker compose up -d                          ## detached mode so get your cmd tool back
docker compose up -d --no-deps container_name ## only restarts the one you specify
docker compose down
docker compose logs
docker compose logs -t                      # logs with timestamps
docker compose logs service1 service2       # specific container logs
docker compose logs --tail=5                # last 5 lines
docker compose logs -f                      # live error tracking
docker compose push
docker compose push service1 service2
docker compose ps                           # list
docker compose rm service                   # remove
docker compose start service
docker compose stop service
docker compose exec service shell_type      # open container files in cmd shell
docker compose up -d --scale service_name=4 # creates 4 containers for that service, ports and names must be unique so you can't assign these up front when doing this
```

## Docker File

- [Reference Builder](https://docs.docker.com/engine/reference/builder/)
- [My Docker Files](/docker/docker_files/)

```dockerfile
## State language and version
FROM        language:version:specific 

## Author
LABEL       author="Hungovercoder"   

## Pass in arguments
ARG        environment

## Set environment variables you can change
## In this case taking value from ARG above
ENV         ENV=$environment                   
## Set port which is reference in expose with dollar
ENV         PORT=3000                 

## Name of working directory
WORKDIR     /app/location             
## Copy specific files from a location to the working directory
COPY        file1 file2 ./           

## This could be install packages or libraries which is not dependent on your source code
RUN         do something
## You might want to echo vars back to confirm them
RUN         echo "Environment is $ENV"
## Copy from a location to the working directory  
## remember to use .dockerignore file to remove files not needed      
COPY        from/. ./                 
## The port you will expose the app on referencing environment variable
EXPOSE      $PORT   

## How you want program to start
ENTRYPOINT  ["program", "start"]      
```

## Docker Compose File

- [My Docker Compose Files](/docker/docker_compose_files/)

```yaml
version: '3.x'

services:

  app:
    container_name: container_name01
    image: imagename01
    build:
      context: ./
      dockerfile: nameof.dockerfile
      args:
        PACKAGES: "arg1 arg2 arg3"
    ports:
      - "int_port:ext_port"
    networks:
      - network-01
    volumes:
      - ./volume/location
    environment:
      - ENV=production
      - APP_VERSION=1.0
      ## you can use environment file too e.g.
      ## env_file:
        ##  .settings.env
    depends_on: 
      - container_name02
      
  data:
    container_name: container_name02
    image: imagename02
    networks:
      - network-01

networks:
  network-01:
    driver: bridge      
```

## Save Space Locally

```bash
docker system prune -a
```

```bash
wsl --shutdown
diskpart
```

```bash
select vdisk file="C:\Users\{user}\AppData\Local\Docker\wsl\data\ext4.vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exit
```

## Network

```bash
docker network create --driver bridge network_name
docker network ls
docker network inspect network_name
docker network rm network_name
docker network prune ## remove all unlinked networks
```
