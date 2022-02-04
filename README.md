# learning-docker
Docker tutorial

https://www.tutorialkart.com/docker/docker-image-with-python-application-example/
https://betterprogramming.pub/how-to-create-a-dockerfile-for-a-python-application-8d078b16bc9a

https://docs.docker.com/engine/reference/commandline/cli/

# build an image
docker build -t python-hello-world .

# check the docker image
docker images

# run the docker image - docker run -it -d --name container_name image_name bash
docker run python-hello-world

# to list all containers
docker container ls -a

# to run a command in a running container
docker exec -it <container_id_or_name> /bin/bash
docker exec -it <container_id_or_name> echo foo && echo bar

# to stop a container
docker stop <container_id_or_name>

# to start a container in detached mode
docker container start <container_id_or_name>

# to start a container in interactive mode
docker container start -i <container_id_or_name>

# to fetch the logs of a container
docker logs <container_id_or_name>

# to delete a container
docker rm <container_id_or_name>

# to delete an image
docker image rm python-hello-world