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
source_file = open("202009CitibikeTripdataExample.csv","r")
# pass our `source_file` as an ingredient to the `csv` library's
# DictReader "recipe".
# store the result in a variable called `citibike_reader`
citibike_reader = csv.DictReader(source_file)
# the DictReader method has added some useful information to our data,
# like a `fieldnames` property that lets us access all the values
# in the first or "header" row
print(citibike_reader.fieldnames)
