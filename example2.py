# Change the current working directory with os.chdir()
import os
cwd = os.getcwd()
print('Current Working Directory is: ', cwd)
absolute_path = 'C:/Users/ok/Desktop/Python'
os.chdir(absolute_path)
print('New working directory is: ', os.getcwd())
# Returns:
# Current Working Directory is:  /Users/datagy
# New working directory is:  /Users/datagy/Documents


# import the `csv` library
import csv
# open the `202009CitibikeTripdataExample.csv` file in read ("r") mode
# this file should be in the same folder as our Python script or notebook
source_file = open("202009-citibike-tripdata.csv","r")
# pass our `source_file` as an ingredient to the `csv` library's
# DictReader "recipe".
# store the result in a variable called `citibike_reader`
citibike_reader = csv.DictReader(source_file)
# the DictReader method has added some useful information to our data,
# like a `fieldnames` property that lets us access all the values
# in the first or "header" row
print(citibike_reader.fieldnames)


# create a variable to hold the count of each type of Citi Bike user
# assign or "initialize" each with a value of zero (0)
subscriber_count = 0
customer_count = 0
other_user_count = 0
# step 3: loop through every row of our data
for a_row in citibike_reader:
#step 3a: if the value in the `usertype` column
# of the current row is "Subscriber"
    if a_row["usertype"] == "Subscriber":
        # add 1 to `subscriber_count`
        subscriber_count = subscriber_count +1
# step 3b: otherwise (else), if the value in the `usertype` column
# of the current row is "Customer"
    elif a_row["usertype"] == "Customer":
     # add 1 to `subscriber_count`
        customer_count = customer_count + 1   
# step 3c: the `usertype` value is _neither_"Subscriber" nor "Customer",
# so we'll add 1 to our catch-all `other_user_count` variable
    else:
        other_user_count = other_user_count + 1 
print("Number of subscribers:")
print(subscriber_count)
print("Number of customers:")
print(customer_count)
print("Number of 'other' users:")
print(other_user_count)     