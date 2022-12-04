# Credit Approval Prediction

## Contributors:

-   Spencer Gerlach
-   Ruslan Dimitrov
-   Daniel Merigo
-   Mengjun Chen

This is a data analysis term project completed for DSCI 522 (Data Science Workflows), a course in the Master of Data Science program at the University of British Columbia. 

## Introduction

The overall goal of this project was to use a publicly available dataset to answer a question about the data, and to automate the data science workflow associated with the analysis.

This data analysis project includes an analysis of the [Credit Approval dataset](https://archive-beta.ics.uci.edu/dataset/27/credit+approval), made publicly available via the UC Irvine Machine Learning Repository. 

The project included the following major deliverables: 

- Write 4-5 R/python scripts, 
- Creation of a reproducible report in Jupyter Lab or R Markdown, 
- Automation of the analysis workflow using `GNU Make`

## Exploratory Data Analysis

The dataset in question, [Credit Approval dataset](https://archive-beta.ics.uci.edu/dataset/27/credit+approval), included a good selection of features upon which to build a simple automated machine learning and statistical exercise. The dataset contains data on Japanese credit card screening of credit card applications. All attribute names and values have been anonymized in order to protect the confidentiality of the applicants. A high level characterization of the features is found at the dataset page linked above. The raw dataset contains a mixture of categorical and numeric features named A1-A16, where the target feature A16 contains values of `+` or `-` indicating whether the candidate is approved or not.

An EDA analysis, [linked here](https://github.com/UBC-MDS/Credit_Approval_Prediction/blob/main/src/Exploratory_Data_Analysis.ipynb), was conducted to investigate the contents of the dataset, relabel and remove missing values, visualize the distribution of various feature values, and to detect any existing correlation between numeric features. 

The Credit Approval dataset is anonymized, so information gleaned from the EDA can only tell us which features (A1-A16) may or may not be important when predicting the target, and which features may be correlated or distributed according to certain known distributions. We are not able to apply any real-world contextual background or domain knowledge to the dataset without labelled feature names.

The EDA generated the following conclusions about the dataset:
- There are 690 rows in the original dataset, 522 of which will be used to train the ML models after a 80%/20% train-test data split. Some of this data is missing values that are replaced/filtered by the EDA.
- The dataset has 16 columns, 6 of which are numeric, and 10 are categorical.
- Numeric columns will require scaling during the preprosessing stage of model creation.
- There is no significant correlation found between any two features in the dataset.

## Analysis Question

This analysis will focus on predicting whether a credit card applicant will be approved or not approved based on a set of features describing that applicant. The dataset in question will be trained on the train portion of the initial dataset (defined during EDA phase), and evaluated against a smaller testing portion of the initial dataset.

Specifically, our analysis prediction question is: 

> "Given features about a credit card applicant, will the applicant be approved for a credit card?"

In our predictive study, we will evaluate the prediction accuracy of a number of simple machine learning models. After splitting the data in EDA into train and test splits, and conducting data preprocessing, we will train and evaluate the following models:

- Support Vector Machine Classifier (RBF Kernel), which we will refer to as `SVC`
- Logistic Regression model, which we will refer to as `Logistic Regression`

These models were compared and optimized using 5-fold cross validation, and hyperparameter optimization. These results can be viewed in the final report below.

## Report

The final report can be found [here](https://github.com/UBC-MDS/Credit_Approval_Prediction/blob/main/doc/credit-appr-predict-report.html).

## Usage

In order to replicate this analysis:

1. Clone this repo, following the [cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) documentation if requried.

2. Change the current wording directory to the root folder of the newly cloned repo.

3. Install the [dependencies](#Dependencies) listed below. 
    - Optionally, download, create, and activate the environment file (.yaml file) provided in the root directory of the repo.

4. Run the makefile from the terminal/command line using the prompt below. The makefile automates every step of the data analysis pipeline.
    - Link to the makefile: [Makefile](https://github.com/UBC-MDS/Credit_Approval_Prediction/blob/main/Makefile)

Prompt to run the makefile:

    - `make all`

5. To delete old files and redo the analysis, run the following prompts in the terminal/command line:

    - `make clear`

    - `make all`

## Dependencies

For a comprehensive list of required packages, refer to the `credit-env.yaml` file saved in the root directory of this repository [here](https://github.com/UBC-MDS/Credit_Approval_Prediction/blob/main/credit-env.yaml).

    - Install the project's dependency environment by running the following command in the conda base environment:
        - `conda env create -f credit-env.yaml`

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
-   scikit-learn>=1.1.3
-   pickle >=3
-   pandoc=2.19.2
-   dataframe-image
-   vl-convert-python

## Licenses

The Credit Approval materials here are licensed under the MIT License and the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.

The license information can be viewed in the `LICENSE` file found in the root directory of this repository.

## Attribution

The automated scripting files in src/ are based on the scripts created by Tiffany Timbers in 2019, available [here](https://github.com/ttimbers/breast_cancer_predictor/tree/master/src)