# Credit_Approval_Prediction Analysis Pipeline
# Author: Daniel Merigo, Spencer Gerlach, Rusland Dimitrov, Mengjun Chen
# Date: 01-12-2022

# This makefile's purpose is to run all steps for the data science project pipeline for our credit approval prediction project

# To run the entire pipeline please enter all:

all: data/raw/crx.csv data/processed/train_df.csv data/processed/test_df.csv results/categorical_counts_histograms.png results/num_distributions.png results/matrix.png results/final_model.sav results/score_table.csv results/test_score_df.csv doc/credit-appr-predict-report.html

# Download data
data/raw/crx.csv: src/download_data.py
	python src/download_data.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data --out_path=data/raw

# Clean, scale and split data
data/processed/train_df.csv data/processed/test_df.csv: data/raw/crx.csv src/pre_process_crx.py
	python src/pre_process_crx.py --input=data/raw/crx.csv --out_dir=data/processed

# Exploratory Data Analysis (EDA)
results/categorical_counts_histograms.png results/num_distributions.png results/matrix.png: data/processed/train_df.csv src/eda_script.py
	python src/eda_script.py --input=data/processed/train_df.csv --output=results

# Fit, train and tune model
results/final_model.sav results/score_table.csv: data/processed/train_df.csv src/best_model_credit_card.py
	python src/best_model_credit_card.py --train_data='data/processed/train_df.csv' --out_dir='results'

# Score model
results/test_score_df.csv: results/final_model.sav src/model_test_script.py
	python src/model_test_script.py --trained_model_dir=results/final_model.sav --test_df_dir=data/processed/train_df.csv --out_dir='results'


# Render HTML report
doc/credit-appr-predict-report.html: results/test_score_df.csv results/score_table.csv doc/credit-appr-predict-report.Rmd doc/references.bib
	Rscript -e "rmarkdown::render('doc/credit-appr-predict-report.Rmd', output_format = 'html_document')"	


# Clean

clean:
	rm -rf data/raw/crx.csv
	rm -rf data/processed/train_df.csv
	rm -rf data/processed/test_df.csv
	rm -rf results/
	rm -rf doc/credit-appr-predict-report.html