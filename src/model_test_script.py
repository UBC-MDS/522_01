# Author: Spencer Gerlach, Mengjun Chen, Daniel Merigo, Ruslan Dimitrov
# date: 2022-11-25
"""
Using the best model for predicting the target to test the test data split. 
Save the output performance as a csv for later use in final reporting.
Usage: src/best_model_credit_card.py --trained_model_dir=<trained_model_dir> --test_df_dir=<test_df_dir> --out_dir=<out_dir>

Options: 
--trained_model_dir=<trained_model_dir>     path (including filename) to the trained model (.sav file)
--test_df_dir=<test_df_dir>     path (including file name) to the test data file (e.g. data/processed/test_df.csv)
--out_dir=<out_dir>     path (NOT including file name) to where the model results should be saved
""" 

#import necessary packages
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer
from docopt import docopt
import os 
import pickle

opt = docopt(__doc__)

def main(trained_model_dir, test_df_dir, out_dir):

    test_df = pd.read_csv(test_df_dir, encoding="utf-8", index_col=0)
    X_test, y_test = test_df.drop(columns=['A16']), test_df['A16']

    fitted_model = pickle.load(open(trained_model_dir,'rb'))
    test_score = fitted_model.score(X_test, y_test)
    test_score_df = pd.DataFrame([[test_score]], columns=['test_score'])

    try:
        test_score_df.to_csv(out_dir + "/test_score_df.csv", index=False)
    except:
        os.makedirs(os.path.dirname(out_dir + "/test_score_df.csv"))
        test_score_df.to_csv(out_dir + "/test_score_df.csv", index=False)

if __name__ == "__main__":
    main(opt['--trained_model_dir'],opt['--test_df_dir'],opt['--out_dir'])
