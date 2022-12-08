# Start from debian:stable image
FROM debian:stable

# Update debian:stable
RUN apt-get update

# Install python
RUN apt-get install -y python

# Install pip3 for python3
RUN apt-get install pip -y

# Install ipython
RUN pip install ipython

# Install Conda

