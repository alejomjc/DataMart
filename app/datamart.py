import pandas as pd
import glob

file_path = 'app/data/'
all_files = glob.glob(file_path + "data_chunk*.snappy.parquet")

df_list = [pd.read_parquet(file) for file in all_files]
df = pd.concat(df_list, ignore_index=True)
