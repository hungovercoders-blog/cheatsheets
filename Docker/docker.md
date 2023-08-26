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
  - [Save Space Locally](#save-space-locally)

Primarily taken from [here](https://docs.docker.com/get-started/docker_cheatsheet.pdf) on the docker site but added more as necessary.

## Useful Links

- [Docker Hub](https://hub.docker.com/)
- [Official Docker Images Available](https://hub.docker.com/search?image_filter=official&q=)
- [Docker Desktop](https://docs.docker.com/get-docker/)
- [Docker VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- [Play with Docker](https://labs.play-with-docker.com/)
- [Play with Kubernetes](https://labs.play-with-k8s.com/)
- [DockerCon](https://www.dockercon.com/)
- [kubeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)

## General

```bash
docker -d ## started docker daemon
docker --help ## get help
docker info ## system wide info
```

## Images

```bash
docker build --help ## get help
docker build -t myimagename:tag . ## build an image from a dockerfile, the "t" stands for tag
docker build -t myimagename:tag -f mycustom.dockerfile . ## build an image from a custom named docker file
docker build -t myimagename:tag . --no-cache ## force rebuild an image from a dockerfile
docker images ## list local images
docker rmi myimagename ## remove image
docker rmi imageid ## remove image
docker image prune ## remove unused docker images
```

## Containers

```bash
docker run --help ## get help
docker run -d -p 80:80 docker/getting-started  ## run getting started image on a container with specific port. The d switch means is not blocking so allows you to run more commands.
docker run --rm -it -p ext_port:int_port/tcp myimagename:latest ## run image interactive. The external port will be what expose outside (e.g. localhost), the internal port is what the app runs on inside
docker start mycontainername ## start container
docker stop mycontainername ## stop container
docker rm mycontainername ## remove container
docker ps ## list running containers
docker ps --all ## list running and stopped containers
docker logs -f mycontainerid ## get logs and watch container, very useful
docker inspect mycontainername ## inspect running container
docker container stats ## view resource stats
docker exec -it mycontainername /bin/bash ## open up container and interact with it through bash to see directories etc e.g. ls, cd.., ls etc. Type exit to exit.
```

## Docker Hub

```bash
docker login -u {dockername} ## login to docker hub
docker build -t {dockerregistry}/myimagename:tag . ## build image and you can use tag to add version
docker push {dockerregistry}/myimagename:tag ## push to docker hub with tag of version
docker tag {dockerregistry}/myimagename:oldtag {dockerregistry}/myimagename:newtag ## tag image on docker
docker search myimagename ## search on docker hub
docker pull {dockerregistry}/myimagename:tag ## pull image from docker hub
```

## Volumes

```bash
docker run -p ext_port:int_port/tcp -v /place/data myimagename:latest # add volume command to write data somewhere for state
docker run -p ext_port:int_port/tcp -v ${PWD}/myfolder:/place/data myimagename:latest # windows print working directory, use the current directory instead of "place/data" 
docker run -p ext_port:int_port/tcp -v $(PWD)/myfolder:/place/data myimagename:latest # mac/linux print working directory, use the current directory instead of "place/data"
```

## Docker Compose

```bash

```

## Docker File

- [Reference Builder](https://docs.docker.com/engine/reference/builder/)
- [My Docker Files](/docker/docker_files/)

```dockerfile
## State language and version
FROM        language:version:specific 

## Author
LABEL       author="Hungovercoder"   

## Set environment variables you can change
ENV         ENV=prd                   
## Set port which is reference in expose with dollar
ENV         PORT=3000                 

## Name of working directory
WORKDIR     /app/location             
## Copy specific files from a location to the working directory
COPY        file1 file2 ./           

## This could be install packages or libraries which is not dependent on your source code
RUN         do something
## Copy from a location to the working directory  
## remember to use .dockerignore file to remove files not needed      
COPY        from/. ./                 
## The port you will expose the app on referencing environment variable
EXPOSE      $PORT   

## How you want program to start
ENTRYPOINT  ["program", "start"]      
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
