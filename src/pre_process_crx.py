# authors: Spencer Gerlach, Ruslan Dimitrov, Daniel Merigo, Mengjun Chen
# date: 2022-11-23

"""
Cleans and splits Credit Approval data from UC Irvine's Machine 
Learning Repository 
https://archive-beta.ics.uci.edu/dataset/27/credit+approval.
Splits data into train and test data and writes to separate csv files.
Usage: src/pre_process_crx.py --input=<input> --out_dir=<out_dir>
  
Options:
--input=<input>       Path (including filename) to raw data (csv file)
--out_dir=<out_dir>   Path to directory where the processed data should be written
"""
# Importing needed libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from docopt import docopt
import os

opt = docopt(__doc__)

def main(input, out_dir):
    """
    Reads in raw csv file cleans it up by replacing
    missing values designated by ? with np.nan

    Splits data into train_df, test_df and saves csv
    files train_df.csv and test_df.csv in out_dir

    Example: python src/pre_process_crx.py --input=data/raw/crx.csv  
    --out_dir=data/processed/
    """
    df = pd.read_csv(input, encoding="utf-8")
    df = df.replace('?', np.nan)
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=522)
    train_df.to_csv(out_dir+ 'train_df.csv')
    test_df.to_csv(out_dir+ 'test_df.csv')

if __name__ == "__main__":
    main(opt['--input'], opt['--out_dir'])