# authors: Spencer Gerlach, Ruslan Dimitrov, Daniel Merigo, Mengjun Chen
# date: 2022-11-24

"""
This scripts takes the train portion of the data previously split by pre_process.py
and performs an EDA to explore the data including creating a table. Ignore the warning as it is part of the vlc library used for image export

Usage: src/eda_script.py --input=<input> --output=<output>

Options:
--input=<input>      The path to a file containing an already clean and formatted dataset in csv format
--output=<output>     Path to where the train and test data should be written
"""


# Import required libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from docopt import docopt
import altair as alt
import dataframe_image as dfi

# The following function was prtovided by Joel Ostblom to enable figure saving using the Altair Library
import vl_convert as vlc

def save_chart(chart, filename, scale_factor=1):
    '''
    Save an Altair chart using vl-convert
    
    Parameters
    ----------
    chart : altair.Chart
        Altair chart to save
    filename : str
        The path to save the chart to
    scale_factor: int or float
        The factor to scale the image resolution by.
        E.g. A value of `2` means two times the default resolution.
    '''
    with alt.data_transformers.enable("default") and alt.data_transformers.disable_max_rows():
        if filename.split('.')[-1] == 'svg':
            with open(filename, "w") as f:
                f.write(vlc.vegalite_to_svg(chart.to_dict()))
        elif filename.split('.')[-1] == 'png':
            with open(filename, "wb") as f:
                f.write(vlc.vegalite_to_png(chart.to_dict(), scale=scale_factor))
        else:
            raise ValueError("Only svg and png formats are supported")


opt = docopt(__doc__)

def main(input, output):
    """
    This function takes the train portion of the data and generates an EDA with plots and tables

    Args:
        input (filepath): file location of the train portion of the data split
        output (filepath): path for the EDA output location
    """
    
    # Read train data into a dataframe
    train_df = pd.read_csv(input, encoding="utf-8")

    # Separate data into categorical and numeric features
    cat_feats = train_df.loc[:, ['A1', 'A4', 'A5', 'A6', 'A7', 'A9', 'A10', 'A12', 'A13', 'A16']]

    num_feats = train_df.loc[:, ['A2', 'A3', 'A8', 'A11', 'A14', 'A15']]

    # Categorical Histograms
    cat_hist = alt.Chart(cat_feats).mark_bar().encode(
        y = alt.Y(alt.repeat('repeat')),
        x = 'count()'
    ).repeat(repeat = ['A1', 'A4', 'A5', 'A6', 'A7', 'A9', 'A10', 'A12', 'A13', 'A16'], columns = 3)
    outfile = output + '/' + 'categorical_counts_histograms.png'
    save_chart(cat_hist, outfile, 2)

    # Numeric Plot Grid (deprecated)
    # num_grid = alt.Chart(num_feats).mark_circle().encode(
    #     alt.X(alt.repeat('column'), type = 'quantitative'),
    #     alt.Y(alt.repeat('row'), type = 'quantitative')
    # ).repeat(
    #     row = ['A2', 'A3', 'A8', 'A11', 'A14', 'A15'],
    #     column = ['A2', 'A3', 'A8', 'A11', 'A14', 'A15']).configure_axis(
    #         grid = False
    #     )

    # save_chart(num_grid, 'categorical_counts_histogram.png', 1)

    # Numeric distributions

    num_dist = alt.Chart(num_feats).mark_bar().encode(
        x = alt.X(alt.repeat('repeat'), bin= alt.Bin(maxbins= 30)),
        y = 'count()'
    ).properties(
        height = 100,
        width = 100
    ).repeat(repeat = ['A2', 'A3', 'A8', 'A11', 'A14', 'A15'], columns = 3)
    outfile = output + '/' + 'num_distributions.png'
    save_chart(num_dist, outfile, 2)

    # Numeric correlation matrix
    corr = train_df.corr('spearman').style.background_gradient()
    outfile = output + '/' + 'matrix.png'
    dfi.export(corr, outfile)

if __name__ == '__main__':
    main(opt['--input'], opt['--output'])

