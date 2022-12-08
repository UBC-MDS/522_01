# Start from debian:stable image
FROM continuumio/miniconda3

RUN apt-get update

RUN apt install chromium-driver -y

RUN apt-get install build-essential -y

WORKDIR /app

# Create the environment:
COPY credit-env.yaml .
RUN conda env create -f credit-env.yaml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# Demonstrate the environment is activated:
RUN echo "Make sure flask is installed:"
RUN python -c "import flask"

