############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM python

# File Author / Maintainer
MAINTAINER Brian Carpio

# Update the sources list

ADD /hello_world/ /hello_world

# Get pip to download and install requirements:
RUN pip install -r /hello_world/requirements.txt

# Expose ports
EXPOSE 8080

# Set the default directory where CMD will execute
WORKDIR /hello_world

# Set the default command to execute
# when creating a new container
# i.e. using CherryPy to serve the application
CMD python server.py
