# Docker Cheat Sheet

- [Docker Cheat Sheet](#docker-cheat-sheet)
  - [Useful Links](#useful-links)
  - [General](#general)
  - [Images](#images)
  - [Containers](#containers)
  - [Docker Hub](#docker-hub)
  - [Save Space Locally](#save-space-locally)

Primarily taken from [here](https://docs.docker.com/get-started/docker_cheatsheet.pdf) on the docker site but added more as necessary.

## Useful Links

- [Docker Hub](https://hub.docker.com/)
- [Play with Docker](https://labs.play-with-docker.com/)
- [Play with Kubernetes](https://labs.play-with-k8s.com/)
- [DockerCon](https://www.dockercon.com/)
- [kubeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)

## General

```bash
docker -d ## started docker daemon
docker --help ## get helop
docker info ## system wide info
```

## Images

```bash
docker build -t myimagename . ## build an image from a dockerfile
docker build -t myimagename . --no-cache ## force rebuild an image from a dockerfile
docker images ## list local images
docker rmi myimagename ## remove image
docker image prune ## remove unused docker images
docker run --rm -it -p 5000:5000/tcp myimagename:latest ## run image interactive
```

## Containers

```bash
docker  ## run image on a container with specific port
docker start mycontainername ## start container
docker stop mycontainername ## stop container
docker rm mycontainername ## remove container
docker ps ## list running containers
docker ps --all ## list running and stopped containers
docker logs -f mycontainername ## get logs  and watch of container
docker inspect mycontainername ## inspect running container
docker container stats ## view resource stats
docker exec -it mycontainername /bin/bash ## open up container and interact with it through bash to see directories etc e.g. ls, cd.., ls etc. Type exit to exit.
```

## Docker Hub

```bash
docker login -u {dockername} ## login to docker hub
docker tag myimagename {dockername}/name ## tag image on docker
docker push {dockername}/myimagename ## push to docker hub
docker search myimagename ## search on docker hub
docker pull myimagename ## pull image from docker hub
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
