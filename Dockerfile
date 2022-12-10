# Start from debian:stable image
FROM continuumio/miniconda3

RUN apt update && apt install -y make

RUN apt install chromium-driver -y

RUN apt-get install build-essential -y


# Install python and dependencies

RUN conda install -y python=3.10 \
    && conda install -c anaconda -y ipykernel \
    && conda install -c conda-forge -y matplotlib \
    && conda install -c anaconda -y scikit-learn=1.1 \
    && conda install -c anaconda -y requests \
    && conda install -c anaconda -y graphviz \
    && conda install -c anaconda -y python-graphviz \ 
    && conda install -c conda-forge -y eli5 \ 
    && conda install -c conda-forge -y shap \ 
    && conda install -c conda-forge -y jinja2 \
    && conda install -c conda-forge -y altair_saver \
    && conda install -c conda-forge -y selenium=4.3 \
    && conda install -c conda-forge -y pandas=1.5 \
    && conda install -c conda-forge -y imbalanced-learn \
    && conda install -c conda-forge -y pip \
    && conda install -c conda-forge -y lightgbm \
    && conda install -c conda-forge -y docopt \ 
    && conda install -c conda-forge -y pandoc \
    && conda install -c conda-forge joblib=1.1.0

# Python dependencies using pip

RUN pip install -U scikit-learn \
    && pip install mglearn \ 
    && pip install psutil \ 
    && pip install vl-convert-python \ 
    && pip install feather-format \
    && pip install dataframe-image

# R-base and r-packages
RUN conda install -c conda-forge --quiet --yes \
    'r-base=4.1.2' \
    'r-rmarkdown' \
    'r-tidyverse=1.3*' \
    'r-knitr' \
    'r-kableextra'\

# RUN apt-get install r-base -y

# RUN Rscript -e "install.packages('hms')"

# RUN Rscript -e "install.packages('kableExtra', dependencies = TRUE)"

# RUN Rscript -e "install.packages(c('rmarkdown', 'here'), repos = 'https://mran.revolutionanalytics.com/snapshot/2022-12-05')"

# # # Demonstrate the environment is activated:
# # RUN echo "Make sure flask is installed:"
# # RUN python -c "import flask"

