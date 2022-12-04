# author: Daniel Merigo
# date 2022-11-18
# based on the script download_data.py by Tiffany Timbers

"""Takes a url and downloads the data from the web as a csv in a local filepath, 
you can supply the filename and extension or leave the default 'crx.csv' by ommiting the filename argument

Usage: data_download.py --url=<url> --out_path=<out_path> [--filename=<filename>]

Options:
--url=<url>             Url for the csv file to download (must be in standard csv format)       (required)
--out_path=<out_path>   Path (not the filename) where the file will be downloaded and saved     (required)
—-[filename=<filename>]	Name of the output file with extension                                  (optional)
"""

import os
import pandas as pd
from docopt import docopt

ins = docopt(__doc__)

def main(url, out_path, filename=None):
    cols = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16']
    data = pd.read_csv(url, names=cols)
    if filename != None :
        name = filename
    else:
        name = 'crx.csv'
    out_file = out_path + '/' + name
    try:
        data.to_csv(out_file, index=False)
    except:
        os.makedirs(os.path.dirname(out_file))
        data.to_csv(out_file, index=False)

if __name__ == '__main__':
    main(ins['--url'], ins['--out_path'], ins['--filename'])
