# Credit Approval Prediction
# Ruslan Dimitrov, Spencer Gerlach, Daniel Merigo, Mengjun Chen

FROM continuumio/miniconda3

USER root

RUN apt-get update

RUN apt-get install -y make \
                       pandoc

RUN apt-get install -y chromium-driver
RUN apt-get install -y python3.10

RUN python -m pip install \
            vl-convert-python


# Install Python 3 packages
RUN conda install -c conda-forge -y \
    'pandas==1.4.*' \
    'ipykernel==6.19.*'\
    'vega_datasets==0.9.*' \
    'feather-format=0.4.*' 


RUN conda install -c conda-forge -y \
         'altair==4.2.*' \
         'altair_saver'

RUN pip install docopt==0.6.* \
        requests \
        feather-format==0.4.*

RUN conda install -c conda-forge -y \
        'scikit-learn==1.1.*'

RUN pip install dataframe-image

RUN conda install -c conda-forge -y \
        'matplotlib==3.6.*' \
        'jinja2==3.*'

RUN pip install imbalanced-learn==0.9.* \
        graphviz==0.20.* \
        selenium==4.2.* \
        xgboost==1.7.*

# Install R packages
RUN apt-get install -y wget r-base r-base-dev

# Install R dependencies
RUN apt-get install -y libxml2-dev libcurl4-openssl-dev libssl-dev libfontconfig1-dev

RUN Rscript -e "install.packages('knitr')" 
RUN Rscript -e "install.packages('rmarkdown')"
RUN Rscript -e "install.packages('kableExtra')"
RUN Rscript -e "install.packages('tidyverse')"

# RUN Rscript -e "install.packages('kableExtra', repos='https://cran.rstudio.com/')"


RUN pip install ipython \
            pickle5

RUN python -m pip install docopt-ng

RUN apt-get update --fix-missing \
    && apt-get install -y \
        pandoc-citeproc

