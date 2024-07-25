"""
This module loads and concatenates parquet files into a single pandas DataFrame.

It performs the following operations:
- Defines the file path for parquet files.
- Retrieves all file paths matching the pattern for parquet files.
- Reads each parquet file into a pandas DataFrame.
- Concatenates all individual DataFrames into a single DataFrame.
"""

import glob
import pandas as pd


FILE_PATH = 'app/data/'
all_files = glob.glob(FILE_PATH + "data_chunk*.snappy.parquet")

df_list = [pd.read_parquet(file) for file in all_files]
df = pd.concat(df_list, ignore_index=True)
