# First attempt at making a function
import pandas as pd
import os

# Prints list of the seeds
# NEED TO ADD STRING PRINT TO DESCRIBE LIST
Seeds_df = pd.read_csv(
    'assests\Seedbank-Python-Sheet1.csv')
Seeds_type = Seeds_df['Type']
print(Seeds_type)

for items in Seeds_type(0, 19):
    Seeds_type = 'Type'
    harv_sea = 'Season'
    sun = 'Sun Requirements'
    days = 'Average Days to Maturity'


while True:
    select = input('Enter Seed Name: ')
    if select == -1:
        print("We don't have that seed (yet!)")
    else:
        print("Seed's specifications are: \n 'Harvest Season: ', 'harv_sea' , \n Sun Requiremnts: ', sun, '\n Average Days to Maturity: ', 'days'")

 #   exit_choice = input('Do you want to exit [Yes|No]: ')
 #   if exit_choice == 'No' or exit_choice == 'no':
# break
