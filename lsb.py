# First attempt at making a function
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

Seeds_type = Seeds_df1['Type']
harv_sea = Seeds_df1['Season']
sun = Seeds_df1['Sun Requirements']
days = Seeds_df1['Average Days to Maturity ']


# I've used full name to avoid duplicate first names in report

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


#input('Enter Seed Name: ')

# if input != get_requirements:
#    print("We don't have that seed (yet!)")
# else:
#     print(
#       "Seed's specifications are: \n 'Harvest Season: ', [1] , \n Sun Requiremnts: ', sun, '\n Average Days to Maturity: ', 'days'")

#   exit_choice = input('Do you want to exit [Yes|No]: ')
#   if exit_choice == 'No' or exit_choice == 'no':
# break

# PRINTS BARPLOT WORKS
sns.barplot(x='Average Days to Maturity ',
            y='Type',
            data=Seeds_df1,
            order=Seeds_df1.sort_values('Average Days to Maturity ').Type)

# Show the plot
plt.show()
