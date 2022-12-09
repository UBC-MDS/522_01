# Start from debian:stable image
FROM continuumio/miniconda3

RUN apt update && apt install -y make

RUN apt install chromium-driver -y

RUN apt-get install build-essential -y

RUN conda install -y python=3.10

WORKDIR /app

# Create the environment:
COPY credit-env.yaml .
RUN conda env create -f credit-env.yaml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "credit-env", "/bin/bash", "-c"]

# R 
RUN apt-get install r-base r-base-dev -y

RUN Rscript -e "install.packages(c('rmarkdown', 'here'), repos = 'https://mran.revolutionanalytics.com/snapshot/2022-12-05')"

RUN Rscript -e "install.packages('kableExtra'', dependencies = TRUE)"

# # Demonstrate the environment is activated:
# RUN echo "Make sure flask is installed:"
# RUN python -c "import flask"

