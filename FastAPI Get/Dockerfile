# get the latest python image
FROM python

# add a user and set work dir
RUN useradd -ms /bin/bash miko
USER miko
WORKDIR /home/miko/src

# copy the python source files
COPY ./src .

# install dependencies
RUN pip install -r dependencies.txt

# document that we’re running the application on port 10000
EXPOSE 10000

# start the python app
ENTRYPOINT [ "python", "main.py"]