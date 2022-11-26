# Author: Mengjun Chen
# date: 2022-11-24
"""
Using the cleaned training data to fit a best model for predicting the target. Save the model as a pickel file.

Usage: src/best_model_credit_card.py --train_data=<train_data> --out_dir=<out_dir>

Options: 

--train_data=<train_data>   path to training data (csv file)
--out_dir=<out_dir>         path to directory where the model should be written (sav file)
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
from sklearn.model_selection import GridSearchCV
import pickle


opt = docopt(__doc__)

def main(train_data, out_dir):

    train_df = pd.read_csv(train_data, encoding="utf-8", index_col=0)
    X_train, y_train = train_df.drop(columns=['A16']), train_df['A16']
    
    #fill missing value with most frequent value of that column for categorical; mean value for numerical 
    cat_imputer = SimpleImputer(strategy='most_frequent', fill_value=np.nan)
    num_imputer = SimpleImputer(strategy='mean', fill_value= np.nan)

    #seperate columns by data type
    numeric_features_nomi = [ 'A3', 'A8', 'A11', 'A15']
    numeric_features_miss = ['A2', 'A14']
    binary_feature_miss = ['A1']
    binary_feature_nomi = ['A9', 'A10', 'A12']
    categorical_features_nomi = ['A13']
    categorical_features_miss = ['A4', 'A5', 'A6', 'A7']
    #make pipeline for transformer
    num_transformer = make_pipeline(num_imputer, StandardScaler())
    cat_transformer_bi = make_pipeline(cat_imputer, OneHotEncoder(drop = 'if_binary', sparse=False, handle_unknown= 'ignore'))
    cat_transformer_nonbi = make_pipeline(cat_imputer, OneHotEncoder(sparse=False, handle_unknown= 'ignore'))
    #final preprocess transformer
    preprocessor = make_column_transformer(
        (num_transformer, numeric_features_miss),
        (StandardScaler(), numeric_features_nomi),
        (cat_transformer_bi, binary_feature_miss),
        (OneHotEncoder(drop = 'if_binary', sparse=False, handle_unknown= 'ignore'), binary_feature_nomi),
        (cat_transformer_nonbi, categorical_features_miss),
        (OneHotEncoder(sparse=False, handle_unknown= 'ignore'), categorical_features_nomi)
    )

    #logistic regression model with default hyperparameter is the best model in this case, details can see src/fit_credit_card_model.ipynb
    logreg = make_pipeline(preprocessor, LogisticRegression(random_state=522))

    param_dist2 = {
        "logisticregression__C": np.logspace(-3,3,7),
        "logisticregression__penalty" : ['l1','l2']
    }
    #using grid search for optimizing hyperparameter 
    grid_search_log = GridSearchCV(logreg, param_dist2, return_train_score=True, n_jobs = -1)
    grid_search_log.fit(X_train, y_train)
    # fit our best model
    best_logreg = grid_search_log.best_estimator_
    best_logreg.fit(X_train, y_train)

    # save fitted model by using pickle
    pickle.dump(best_logreg, open(out_dir+'/final_model.sav', 'wb'))

if __name__ == "__main__":
    main(opt['--train_data'],opt['--out_dir'])





