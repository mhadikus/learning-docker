# learning-docker
Docker tutorial

https://www.tutorialkart.com/docker/docker-image-with-python-application-example/
https://docs.docker.com/engine/reference/commandline/cli/

# build an image
docker build -t python-hello-world .

# check the docker image
docker images

# run the docker image
#    docker run -it -d --name container_name image_name bash
#       -i option means that it will be interactive mode (you can enter commands to it)
#       -t option gives you a terminal (so that you can use it as if you used ssh to enter the container).
#       -d option (daemon mode) keeps the container running in the background.
#       bash is the command it runs.
docker run python-hello-world

# to list all containers
docker container ls -a

# to run a command in a running container
docker exec -it <container_id_or_name> "echo foo && echo bar"

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