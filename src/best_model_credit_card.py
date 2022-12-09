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
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.svm import SVC
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import cross_validate
import pickle


opt = docopt(__doc__)

def preprocess():

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

    return preprocessor

def finding_best_model(X_train, y_train, out_dir):
    preprocessor = preprocess()
    # creating score table, by using default R^2 score
    cross_val_results= {}
    #dummy classifier as a baseline
    dum_pipe = make_pipeline(preprocessor, DummyClassifier())
    cross_val_results['dummy'] = pd.DataFrame(cross_validate(dum_pipe, X_train, y_train, return_train_score=True)).agg(['mean', 'std']).round(3).T

    #logistic regression model
    logreg = make_pipeline(preprocessor, LogisticRegression(random_state=522))
    cross_val_results['logreg'] = pd.DataFrame(cross_validate(logreg, X_train, y_train, return_train_score=True)).agg(['mean', 'std']).round(3).T

    #SVC model
    svc_pipe = make_pipeline(preprocessor, SVC(random_state=522))
    cross_val_results['svc'] = pd.DataFrame(cross_validate(svc_pipe, X_train, y_train, return_train_score=True)).agg(['mean', 'std']).round(3).T

    #finding the best hyperparameter for svc to see if it will be better than logistic regression after that 
    param_dist = {
        "svc__class_weight": [None, "balanced"],
        "svc__gamma": 10.0 ** np.arange(-2, 3),
        "svc__C": 10.0 ** np.arange(-2, 3)
    }

    random_search = RandomizedSearchCV(svc_pipe, param_distributions=param_dist, return_train_score=True, n_jobs = -1)
    random_search.fit(X_train, y_train)
    best_svc = random_search.best_estimator_
    cross_val_results['best_svc'] = pd.DataFrame(cross_validate(best_svc, X_train, y_train, return_train_score=True)).agg(['mean', 'std']).round(3).T


    param_dist2 = {
        "logisticregression__C": np.logspace(-3,3,7),
        "logisticregression__penalty" : ['l1','l2']
    }
    #using grid search for optimizing hyperparameter 
    grid_search_log = GridSearchCV(logreg, param_dist2, return_train_score=True, n_jobs = -1)
    grid_search_log.fit(X_train, y_train)
    
    best_logreg = grid_search_log.best_estimator_
    cross_val_results['best_logreg'] = pd.DataFrame(cross_validate(best_logreg, X_train, y_train, return_train_score=True)).agg(['mean', 'std']).round(3).T
    
    #save our final score table
    final_table = pd.concat(cross_val_results, axis=1) 
    table_path = out_dir + '/score_table.csv'
    final_table.to_csv(table_path, sep=',', encoding='utf-8')
    return best_logreg



def main(train_data, out_dir):
    #loading data
    train_df = pd.read_csv(train_data, encoding="utf-8", index_col=0)
    X_train, y_train = train_df.drop(columns=['A16']), train_df['A16']
    #loading best model
    best_model = finding_best_model(X_train=X_train, y_train=y_train, out_dir=out_dir)
    # fit our best model
    best_model.fit(X_train, y_train)
    # save fitted model by using pickle
    pickle.dump(best_model, open(out_dir+'/final_model.sav', 'wb'))
    
if __name__ == "__main__":
    main(opt['--train_data'],opt['--out_dir'])





