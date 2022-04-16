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


