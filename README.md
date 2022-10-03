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
- to always restart the container, use --restart always

## to enable/disable automatic restart of the container
- docker update --restart=always <container_id_or_name>
- docker update --restart=no <container_id_or_name>

## run an image in the background with bash
- docker run -it -d --name <container_id_or_name> <image_name> bash
- docker container run -d --name fastapi_get_container -t -p 10000:10000 fastapi-get:latest

## to get information about a container
- docker inspect <container_id_or_name>

## to list all containers
- docker container ls -a

## to run a command in a running container
- docker exec -it <container_id_or_name> /bin/bash
- docker exec -it <container_id_or_name> sh
- docker exec -it <container_id_or_name> echo foo && echo bar

## to stop a container
- docker stop <container_id_or_name>

## to restart a container
- docker restart <container_id_or_name>

## to start a container in detached mode
- docker container start <container_id_or_name>

## to start a container in interactive mode
- docker container start -i <container_id_or_name>

## to fetch the logs of a container
- docker logs <container_id_or_name>
- docker logs --tail 50 <container_id_or_name>

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

## to deploy the [docker/getting-started](https://hub.docker.com/r/docker/getting-started) image with a service
- kubectl apply -f docker-getting-started-deployment.yaml
- kubectl get deployments
- kubectl rollout status deployment/getting-started-deployment
- kubectl logs deployment/getting-started-deployment
- kubectl get services
- browse to http://localhost:30001
- `port: 80` the port on which the app is running inside the container
- `targetPort: 80` the port on the pod where the service is running
- `nodePort: 30001` the port on the node where external traffic comes in
- The service will route traffic from port 30001 on your host to port 80 inside the pods it routes to
- kubectl delete -f docker-getting-started-deployment.yaml

## to deploy and run a locally built image in Kubernetes
- Push the local image to [Docker Registry](https://docs.docker.com/registry/)
- docker run -d -p 4000:5000 --name registry registry:2
- docker image tag fastapi-get localhost:4000/fastapi-get
- docker push localhost:4000/fastapi-get
- browse to http://localhost:4000/v2/_catalog
- docker pull localhost:4000/fastapi-get
- kubectl apply -f fastapi-get.yaml
- docker container stop registry && docker container rm -v registry

***

# Helm
- https://helm.sh/docs/intro/quickstart/
- https://helm.sh/docs/intro/install/
- [What is a Helm Chart?](https://www.freecodecamp.org/news/what-is-a-helm-chart-tutorial-for-kubernetes-beginners/)

## to install nginx using helm charts
- https://www.golinuxcloud.com/kubernetes-helm-charts/#51_Create_a_new_chart
- helm create nginx-chart
- helm lint nginx-chart
- helm install --dry-run nginx nginx-chart/
- helm install nginx nginx-chart/
- kubectl get all
- kubectl get pods -o wide
- browse to http://localhost:30004
- If `nodePort` is not specified in `service.yaml`, the Kubernetes control plane will allocate a port from a range (default: 30000-32767)
- helm uninstall nginx

## Example Helm Charts
- Simple example of the nginx helm chart: `\Helm\nginx-chart`
- Example of a web application with secrets and ingress: `\Helm\my-web-app-chart`