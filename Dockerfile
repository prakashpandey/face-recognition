# Project 
# Face recognition

# Pull base image
FROM ubuntu:16.04

# Author / maintainer 
MAINTAINER Prakash Pandey <prakash.pandey@shephertz.com> 

# Install dependency
RUN \
apt-get update
#Install face-recognition library
pip3 install face_recognition
# Get project from github
cd usr/bin && git clone https://github.com/prakashpandey/face-recognition.git

# Set the default command
ENTRYPOINT ["/usr/bin/face-recognition"]



