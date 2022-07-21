# First attempt at making a function
import pandas as pd
import os
import csv

# Prints list of the seeds
# NEED TO ADD STRING PRINT TO DESCRIBE LIST
Seeds_df = os.path.join('assets', 'Seedbank-Python-Sheet1.csv')
Seeds_type = Seeds_df['Type']
print(Seeds_type)


Seeds_type = Seeds_df['Type']
harv_sea = Seeds_df['Season']
sun = Seeds_df['Sun Requirements']
days = Seeds_df['Average Days to Maturity']

details = pd.DataFrame(
    {'Vegetable': vegetable,
     'Season': season,
     'Sun_Requirements': sun,
     }
)

select = input('Enter Seed Name: ')
if select == -1:
    print("We don't have that seed (yet!)")
else:
    print("Seed's specifications are: \n 'Harvest Season: ', 'harv_sea' , \n Sun Requiremnts: ', sun, '\n Average Days to Maturity: ', 'days'")

 #   exit_choice = input('Do you want to exit [Yes|No]: ')
 #   if exit_choice == 'No' or exit_choice == 'no':
# break
