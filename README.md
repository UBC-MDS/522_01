# Credit Approval Prediction

## Contributors:

-   Spencer Gerlach
-   Ruslan Dimitrov
-   Daniel Merigo
-   Mengjun Chen

This was a data analysis term project completed for DSCI 522 (Data Science Workflows), a course in the Master of Data Science program at the University of British Columbia.

## Project Proposal

### Introduction

This data analysis project will include an analysis of the [Credit Approval dataset](https://archive-beta.ics.uci.edu/dataset/27/credit+approval), made publicly available via the UC Irvine Machine Learning Repository. The overall goal of this project was to answer a question using a publicly available dataset.

The project included the following major deliverables: - Write 4-5 R/python scripts, - Creation of a reproducible report in Jupyter Lab or R Markdown, - Automation of the analysis workflow using `GNU Make`

The dataset in question, Credit Approval, included a good selection of features upon which to build a simple automated machine learning and statistical exercise.

### Analysis Question

This analysis will focus on predicting whether someone will be approved or not approved based on a set of testing data. In other words, the dataset in question will be trained on some fraction of the initial dataset, and evaluated against a smaller testing portion of the initial dataset.

Specifically, our analysis prediction question is: - "Given features about a credit card applicant, will the customer be approved for a credit card?"

This section is not yet complete

### Report

The final report will be linked here once the project is completed.

## Usage

We used the dataset that comes from the UCI dataset. Here is the exact dataset [url](https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data).

In order to replicate this analysis, you first need to clone this repo, then running the following code in your terminal:

      python src/download_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data" --out_path=<supply an output location> [--filename=<supply a suitable filename>] The filename argument is optional and if not supplied it will default to 'crx.csv'. This is done so we ensure that by default the data file is downloaded and converted to a csv file the experiment can read.

## Dependencies

-   ipykernel
-   ipython\>=7.15
-   vega_datasets
-   altair_saver
-   selenium\<4.3.0
-   pandas\<1.5
-   pip
-   docopt=0.6.2
-   requests=2.22.0
-   feather-format=0.4.0

## Licenses

The Credit Approval materials here are licensed under the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.
