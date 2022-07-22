# First attempt at making a function
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Prints list of the seeds
# NEED TO ADD STRING PRINT TO DESCRIBE LIST
path = 'assests\Seedbank-Python-Sheet1.csv'
Seeds_df = os.path.join(path, 'assets', 'Seedbank-Python-Sheet1.csv')
print(Seeds_df)

Seeds_df1 = pd.read_csv(
    'assests\Seedbank-Python-Sheet1.csv')
Seeds_type = Seeds_df1['Type']
print(Seeds_type)
# print(Seeds_df1.columns.tolist())

Seeds_type = Seeds_df1['Type']
harv_sea = Seeds_df1['Season']
sun = Seeds_df1['Sun Requirements']
day = Seeds_df1['Average Days to Maturity ']


#select = input('Enter Seed Name: ')
# if select == (index_col=[0, 20]):
#   print("We don't have that seed (yet!)")
# else:
#   print(
#       "Seed's specifications are: \n 'Harvest Season: ', [1] , \n Sun Requiremnts: ', sun, '\n Average Days to Maturity: ', 'days'")

#   exit_choice = input('Do you want to exit [Yes|No]: ')
#   if exit_choice == 'No' or exit_choice == 'no':
# break


sns.barplot(x='Average Days to Maturity ',
            y='Type',
            data=Seeds_df1,
            order=Seeds_df1.sort_values('Average Days to Maturity ').Type)

# Show the plot
plt.show()
