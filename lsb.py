# modules for reading the data

import pandas as pd
import numpy as num
import seaborn as sns

# funtion to read the data
Seeds_df = pd.read_csv(
    'assests\Seedbank-Python-Sheet1.csv')
Seeds_df.head()
print(Seeds_df)

# changing the data to be read as a list

Seeds_df = pd.read_csv(
    'assests\Seedbank-Python-Sheet1.csv', delimiter=',')
list_of_rows = [list(row) for row in Seeds_df.values]
list_of_rows.insert(0, Seeds_df.columns.to_list())
print(list_of_rows)
