# Louisville_Seedbank_Project
The Louisville_Seedbank_Project is able to take input the name of one of the top 20 seeds that the Louisville Seedbank distributes and have three values come out. Value one: Harvest Season, Value two: Days to Maturity, Value three: Sun requirements. A list is printed of the Top 20 seeds, takes input, gives output, and finally shows two barplot graphs. This was completed for Code Louisville Data Analtics 1 course. 

# Requirements:
## 1. Category 1:Read data in.
   - Read in data from a local csv, excel file, json, or any other file type. There are many ways to do this, but using Pandas read_ functions is pretty easy.
     - Made my own csv file and read it using pandas
## 2. Category 2:Manipulate and clean your data.
    - Use custom functions or lambdas to perform specific operations to clean or manipulate your data, return those values, then use them in other parts of your project.
     - Pulled in first row of csv and print it as a list so that it is easy to input a seed type
## 3. Category 3:Analyze your data! 
    - Write custom functions to operate on your data. You may discover that you want to find out something particular about data that just doesn’t have a built-in Pandas function that accomplishes your goal. Maybe you want your function to read in a DataFrame, search the columns for any mention of “Cars”, then return the lowest-priced car in the column along with the mileage. This category is very open to interpretation, so any function operating on your data will work.
     - Made a custom funtion using the csv module to take user input and print out the growing requirments of that seed type.
## 4. Category 4:Visualize your data.
    - Make 2 basic plots with matplotlib, seaborn, or any other kind of visualization library that you think looks interesting.
     - One plot is a bar graph of seed type and the average days of maturity. Second barplot shows the difference bettween the average days of maturity versus the sun requirements. 
## 5. Category 5:Interpret your data and graphical output.
-If using some format other than a notebook, make sure your README explains your project. 
    -

