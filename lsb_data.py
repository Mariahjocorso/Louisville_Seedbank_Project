# modules for reading the data

import os
import pandas as pd
import numpy as num
import seaborn as sns

from lsb import Seeds_type

# funtion to read the data
# Seeds_df = pd.read_csv(
#   'assests\Seedbank-Python-Sheet1.csv')
# Seeds_df.head()
# print(Seeds_df)

# changing the data to be read as a list

# Seeds_df = pd.read_csv(
#  'assests\Seedbank-Python-Sheet1.csv', delimiter=',')
# list_of_rows = [list(row) for row in Seeds_df.values]
# list_of_rows.insert(0, Seeds_df.columns.to_list())
# print(list_of_rows)

# Changing function to only print out list of Seed Names

# Seeds_df = pd.read_csv(
#    'assests\Seedbank-Python-Sheet1.csv')
# Seeds_type = Seeds_df['Type']
# print(Seeds_type)

# printing as a dictionary (can this be used for what I want to do???)

# Seeds_df = pd.read_csv(
#    'assests\Seedbank-Python-Sheet1.csv', usecols=['Type', 'Sun Requirements', ])
# Seeds_df.to_dict(orient='dict')
# print(Seeds_df)

path = 'assests\Seedbank-Python-Sheet1.csv'
Seeds_df = os.path.join(path, 'assets', 'Seedbank-Python-Sheet1.csv')
print(Seeds_df)

Seeds_df1 = pd.read_csv(
    'assests\Seedbank-Python-Sheet1.csv')
Seeds_type = Seeds_df1['Type']
print(Seeds_type)
