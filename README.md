# Credit Approval Prediction

## Contributors:

-   Spencer Gerlach
-   Ruslan Dimitrov
-   Daniel Merigo
-   Mengjun Chen

This was a data analysis term project completed for DSCI 522 (Data Science Workflows), a course in the Master of Data Science program at the University of British Columbia.

## Project Proposal

## Introduction

This data analysis project will include an analysis of the [Credit Approval dataset](https://archive-beta.ics.uci.edu/dataset/27/credit+approval), made publicly available via the UC Irvine Machine Learning Repository. The overall goal of this project was to answer a question using a publicly available dataset.

The project included the following major deliverables: - Write 4-5 R/python scripts, - Creation of a reproducible report in Jupyter Lab or R Markdown, - Automation of the analysis workflow using `GNU Make`

## Exploratory Data Analysis

The dataset in question, [Credit Approval dataset](https://archive-beta.ics.uci.edu/dataset/27/credit+approval), included a good selection of features upon which to build a simple automated machine learning and statistical exercise. The dataset contains data on Japanese credit card screening of credit card applications. All attribute names and values have been anonymized in order to protect the confidentiality of the applicants. A high level categorization of the features is found at the dataset page linked above. The dataset contains a mixture of categorical and numeric features named A1-A16, where the target feature A16 contains values of `+` or `-` indicating whether the candidate is approved or not.

And EDA analysis [linked here](https://github.com/UBC-MDS/Credit_Approval_Prediction/blob/main/src/Exploratory_Data_Analysis.ipynb) was conducted to investigate the contents of the dataset, relabel and remove missing values, visualize the distribution of various feature values, and to detect and existing correlation between numeric features. 

The Credit Approval dataset is anonymized, so information gleaned from the EDA can only tell us which features A1-A16 may be more or less important when predicting the target, and which features may be correlated or distributed according to certain known distributions. We are not able to apply any real-world contextual background or domain knowledge to the dataset without labelled feature names.

The EDA generated the following conclusions about the dataset:
- There are 690 rows in the original dataset, 522 of which will be used to train the ML models after a 80%/20% train-test data split. Some of this data is unknown data that is replaced/filtered by the EDA.
- The dataset has 16 columns, 6 of which are numeric, and 10 are categorical.
- Numeric columns will require scaling during the preprosessing stage of model creation.
- There is no significant correlation found between any two features in the dataset.
### Analysis Question

This analysis will focus on predicting whether someone will be approved or not approved based on a set of testing data. In other words, the dataset in question will be trained on some fraction of the initial dataset, and evaluated against a smaller testing portion of the initial dataset.

Specifically, our analysis prediction question is: 

- "Given features about a credit card applicant, will the applicant be approved for a credit card?"

In our predictive study, we will evaluate the prediction accuracy of a number of ML models. After splitting the data in EDA into train and test splits, and conducting data preprocessing, we will train and evaluate the following models:
- Support Vector Machine Classifier (RBF Kernel), which we will refer to as `SVC`
- k-Nearest Neighbours model, which we will refer to as `kNN`
- Logistic Regression model, which we will refer to as `Logistic Regression`

These models will undergo hyperparameter optimization, and the best model will be scored against the test data.

### Report

The final report will be linked here once the project is completed.

## Usage

We used the dataset that comes from the UCI dataset. Here is the exact dataset [Credit Approval Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data).

In order to replicate this analysis, you first need to clone this repo, then running the following code in your terminal:

      python src/download_data.py --url="https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data" --out_path=<supply an output location> [--filename=<supply a suitable filename>] 
      
The filename argument is optional and if not supplied it will default to 'crx.csv'. 

This is done so we ensure that by default the data file is downloaded and converted to a csv file the experiment can read.

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

The Credit Approval materials here are licensed under the MIT License and the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.

The license information can be viewed in the `LICENSE` file found in the root directory of this repository.

## Attribution

The automated scripting file in `src/download_data.py` is based on the script `download_data.py` created by Tiffany Timbers 2019-12-18. It can be found [here](https://github.com/ttimbers/breast_cancer_predictor/blob/master/src/download_data.py)
