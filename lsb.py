# First attempt at making a function
from ast import Break
import csv
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Prints list of the seeds

Welcome_message = "Here is a list of Louisville Seedbank's Top 20 most popular Seeds!"
print(Welcome_message)

path = 'assests\Seedbank-Python-Sheet1.csv'
Seeds_df = os.path.join(path, 'assets', 'Seedbank-Python-Sheet1.csv')
# print(Seeds_df)

Seeds_df1 = pd.read_csv(
    'assests\Seedbank-Python-Sheet1.csv')
Seeds_type = Seeds_df1['Type']
print(Seeds_type.tolist())
# print(Seeds_df1.columns.tolist())


# Function to take user input and return growing requirement values

with open(path) as csvfile:
    read_csv = csv.DictReader(csvfile)
    Seed_name = input('Enter Seed Name: ')
    for row in read_csv:
        if Seed_name == row['Type']:
            for k, v in row.items():
                print(k, ':', v)
            break
    else:
        print("We don't have that seed (yet!).")


# First barplot
sns.barplot(x='Average Days to Maturity ',
            y='Type',
            data=Seeds_df1,
            order=Seeds_df1.sort_values('Average Days to Maturity ').Type)

# Show first plot
plt.show()

# Second barplot
# sns.barplot(x='Sun Requirements',
#            y='Type',
#            data=Seeds_df1,
#            order=Seeds_df1.sort_values('Sun Requirements').Type)

# Show second plot
# plt.show()
