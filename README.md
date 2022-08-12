***

# Docker
- https://www.tutorialkart.com/docker/docker-image-with-python-application-example/
- https://betterprogramming.pub/how-to-create-a-dockerfile-for-a-python-application-8d078b16bc9a
- https://docs.docker.com/engine/reference/commandline/cli/

## build an image
- docker build -t python-hello-world .
- docker image build . -t fastapi-get

## check the docker image
- docker images

## run the image
- docker run python-hello-world
- docker container run --name fastapi_get_container -t -p 10000:10000 fastapi-get:latest

## run an image in the background with bash
- docker run -it -d --name <container_id_or_name> <image_name> bash
- docker container run -d --name fastapi_get_container -t -p 10000:10000 fastapi-get:latest

## to list all containers
- docker container ls -a

## to run a command in a running container
- docker exec -it <container_id_or_name> /bin/bash
- docker exec -it <container_id_or_name> echo foo && echo bar

## to stop a container
- docker stop <container_id_or_name>

## to start a container in detached mode
- docker container start <container_id_or_name>

## to start a container in interactive mode
- docker container start -i <container_id_or_name>

## to fetch the logs of a container
- docker logs <container_id_or_name>

## to delete a container
- docker rm <container_id_or_name>

## to delete an image
- docker image rm python-hello-world

***

# Kubernetes
- https://kubernetes.io/docs/tutorials/kubernetes-basics/
- https://www.guru99.com/kubernetes-tutorial.html
- `Pod`: a collection of Containers
- `Namespace`: name to organize Pods
- `Node`: hardware for running Pods
- `Cluster`: a collection of Nodes
- `Service`: network abstraction over a set of pods
- `Server`: Kubernetes Control plane, e.g., api-server, etcd,etc
- `Client`: kubectl

## Kubernetes on Docker Desktop
- https://docs.docker.com/desktop/kubernetes/
- https://docs.docker.com/get-started/orchestration/
- https://docs.docker.com/get-started/kube-deploy/

## to create a pod with a single container that isolates a simple ping to 8.8.8.8
- kubectl apply -f ping-pod.yaml
- kubectl get pods
- kubectl logs ping-pod
- kubectl delete -f ping-pod.yaml

## to deploy the simple ping using deployment yaml file
- kubectl apply -f ping-deployment.yaml
- kubectl get deployments
- kubectl rollout status deployment/ping-deployment
- kubectl logs deployment/ping-deployment
- kubectl get services
- kubectl delete -f ping-deployment.yaml