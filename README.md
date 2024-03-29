# Louisville_Seedbank_Project
The Louisville_Seedbank_Project is able to take input the name of one of the top 20 seeds that the Louisville Seedbank distributes and have three values come out. Value one: Harvest Season, Value two: Days to Maturity, Value three: Sun requirements. A list is printed of the Top 20 seeds, takes input, gives output, and finally shows two barplot graphs. This was completed for Code Louisville Data Analytics 1 course. 
![Barplot #1](https://github.com/Mariahjocorso/Louisville_Seedbank_Project/blob/main/assets/Seedbank_Project_Figure_1.png)
![Barplot #2](https://github.com/Mariahjocorso/Louisville_Seedbank_Project/blob/main/assets/Seedbank_Project_Figure_2.png)

# Requirements/Instructions
- Python 3.10.2
- Clone git repository https://github.com/Mariahjocorso/Louisville_Seedbank_Project 
- Run "pip install -r requirements.txt" to install the required packages.
 - if that does not work run "python3 -m pip install -r requirments.txt" to install required packages.
- Run python lsb.py once in Louisville_Seedbank_Project main directory.
- Make sure to capitalize the Seed name when entering input/check that spelling matches printed list.

# Project Requirements Met
1. Category 1:Read data in.
   - Read in data from a local csv, excel file, json, or any other file type. There are many ways to do this, but using Pandas read_ functions is pretty easy.
     - Made my own csv file of the top 20 seeds that our organization Louisville Seedbank handed out in the 2021 year, they are listed in alphabetical order and not in order of frequency that is was dispensed and read it using pandas.
2. Category 2:Manipulate and clean your data.
    - Use custom functions or lambdas to perform specific operations to clean or manipulate your data, 
    return those values, then use them in other parts of your project.
      - Pulled in first row of csv and print it as a list so that it is easy to input a seed type.
3. Category 3:Analyze your data! 
    - Write custom functions to operate on your data. You may discover that you want to find out something 
    particular about data that just doesn’t have a built-in Pandas function that accomplishes your goal.
    Maybe you want your function to read in a DataFrame, search the columns for any mention of “Cars”, then return the lowest-priced car inthe column along with the mileage. This category is very open to interpretation, so any function operating on your data will work.
      - Made a custom funtion using the csv module to take user input and print out the growing requirments of that seed type.
4. Category 4:Visualize your data.
    - Make 2 basic plots with matplotlib, seaborn, or any other kind of visualization library that you think looks interesting.
      - One plot is a bar graph of seed type and the average days of maturity. Second barplot shows the difference bettween the average days of maturity versus the sun requirements. 
5. Category 5:Interpret your data and graphical output.
    - If using some format other than a notebook, make sure your README explains your project. 
      - The first barplot is a visulization of the type of seeds verus the days it takes for the plant to reach maturity. This is an imporatant visulization when you're trying to feed a family or themselves. This can be utilized to find a plant that will grow quickly or find what food they may be able to grow within a certain time period that the grower may have access to their plot or land. 
      - The second barplot is a visulization of the average days of matuirty vs sun requirments. This can help growers understand that full sun plants on average need longer to reach maturity and it helps plan their gardens based on the sun on the plot. 
      
# Improvements 
## A list of improvements that I feel I can make to my code in the future
  - make data frame appendable and able to add in new seeds
  - have my function loop back up and ask for a second input after the first seeds (or not there seeds) response shows
  - have an exit option to ask if you want that second input and a way to exit to print graphs
  - look in to getting both graph to show at the same time and/or find a way to not have to close first graph to get second
  - look up clearical (character?) chart to see how to hold two vairble that are txt
  
