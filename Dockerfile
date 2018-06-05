# Project 
# Face recognition

# Pull base image
FROM ubuntu:18.04

# Author / maintainer 
MAINTAINER Prakash Pandey <prakash.pandey@shephertz.com> 

# Install dependency
RUN apt-get update

RUN apt-get install -y git

RUN apt-get install -y --no-install-recommends apt-utils

RUN apt-get install -y python-pip

RUN apt-get install -y cmake

RUN pip install dlib

#Install face-recognition library
RUN pip install face_recognition
# Get project from github
RUN cd /usr/bin && git clone https://github.com/prakashpandey/face-recognition.git

# Set the default command
ENTRYPOINT ["python /usr/bin/face-recognition/src/main/realtime.py"]


