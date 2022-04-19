# change woring directory %%
import os
cwd = os.getcwd()
print('Current Working Directory is: ', cwd)
absolute_path = 'C:/Users/ok/Desktop/Python'
os.chdir(absolute_path)
print('New working directory is: ', os.getcwd())

# import panda %%
import pandas as pd

# import csv file %%
data = pd.read_csv('202009-citibike-tripdata.csv')

# print output table %%
data
# print distinct values in particular column %%
print(data['gender'].value_counts())

# check first five row in table
data.head()
# check last five row in table
data.tail()
#count distinct values in all variables
print(data.nunique())