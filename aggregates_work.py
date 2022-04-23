# %% [markdown]
# # group by

# %%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# sets the default style for plotting
sns.set_style("darkgrid")
titanic_data = sns.load_dataset('titanic')
titanic_data.head()

# %%
# counting number of missing values in a colum
titanic_data['age'].isna().sum()

# %%
# variables with missing data
titanic_data.columns[titanic_data.isnull().any()]

# %%
#grouping by clas
titanic_gbclass = titanic_data.groupby("class")
type(titanic_gbclass)

# %%
# You can know the numer of group in a grouped column
titanic_gbclass.ngroups

# %%
# The size function can help determine the number of values in each group. it's similar to value_count
titanic_gbclass.size()

# %%
#The returns the indexes with value of First
titanic_gbclass.groups["First"]

# %%
# getting first or last in the group using first or last
titanic_gbclass.last()

# %%
# get_group gets all the associated values with group
titanic_second_class = titanic_gbclass.get_group("Second")
titanic_second_class.head()

# %%

# you can apply the max to any numerical variable in the froup
titanic_gbclass.age.max()

# %%
# passing the agg funtion to the group and extracting important aggrgate data

titanic_gbclass.fare.agg(['max', 'min', 'count', 'median', 'mean'])

# %% [markdown]
# # Concatenating Data
# #vertical, horizontal data frame or is it appending?

# %%
# let's check the shapes of the data frame we have. 

titanic_pclass1_data = titanic_data[titanic_data["class"] == "First"]
print(titanic_pclass1_data.shape)

titanic_pclass2_data = titanic_data[titanic_data["class"] == "Second"]
print(titanic_pclass2_data.shape)

# %%
# checking the content of the date frame
titanic_pclass1_data.info()

# %%
#concatenating data vertically, both the dataframes should have an equal number of columns
#appendind data
final_data = titanic_pclass1_data.append(titanic_pclass2_data, ignore_index=True)
print(final_data.shape)

# %%
#maybe I need to check the difference with appending
final_data = pd.concat([titanic_pclass1_data, titanic_pclass2_data])
print(final_data.shape)

# %%
df1 = final_data[:200]
print(df1.shape)
df2 = final_data[200:]
print(df2.shape)
final_data2 = pd.concat([df1, df2], axis = 1, ignore_index = True)
print(final_data2.shape)
final_data2.head()
final_data2.info()

# %%
# reading data from stata
df = pd.read_stata('citibike.dta')
df.dtypes

# %% [markdown]
# # Merging

# %%
# creating a dummy table
scores1 = [
{'Subject':'Mathematics', 'Score':85, 'Grade': 'B', 'Remarks': 'Good',
},
{'Subject':'History', 'Score':98, 'Grade': 'A','Remarks':
'Excellent'},
{'Subject':'English', 'Score':76, 'Grade': 'C','Remarks': 'Fair'},
{'Subject':'Chemistry', 'Score':72, 'Grade': 'C','Remarks': 'Fair'},
]
scores2 = [
{'Subject':'Arts', 'Score':70, 'Grade': 'C','Remarks': 'Fair'},
{'Subject':'Physics', 'Score':75, 'Grade': 'C','Remarks': 'Fair'},
{'Subject':'English', 'Score':92, 'Grade': 'A','Remarks':
'Excellent'},
{'Subject':'Chemistry', 'Score':91, 'Grade': 'A','Remarks':
'Excellent'},
]
scores1_df = pd.DataFrame(scores1)
scores2_df = pd.DataFrame(scores2)

# %%
scores1_df.head()

# %%
scores2_df.head()

# %%
# merging in python is similar to joint in sql(inne join, left  join and right  join)
join_inner_df = scores1_df.merge(scores2_df, on='Subject', how='inner')
join_inner_df.head()

# %%
# left join will return all values from the main data

join_inner_df = scores1_df.merge(scores2_df, on='Subject', how='left')
join_inner_df.head()

# %%
# Merging with right join
join_inner_df = scores1_df.merge(scores2_df, on='Subject', how='right')
join_inner_df.head()

# %%
#Merging with Outer Join

join_inner_df = scores1_df.merge(scores2_df, on='Subject', how='outer')
join_inner_df.head()

# %% [markdown]
# # Duplicates

# %%
scores = [['Mathematics', 85, 'Science'],
['English', 91, 'Arts'],
['History', 95, 'Chemistry'],
['History', 95, 'Chemistry'],
['English', 95, 'Chemistry'],
]
my_df = pd.DataFrame(scores, columns = ['Subject', 'Score', 'Subject'])
my_df.head()

# %%
# droping duplicates observations by rows like that of stata duplicates drop
result = my_df.drop_duplicates()
# if you want to remove the last intance you must specify it keep = last e.g:
result = my_df.drop_duplicates(keep='last')

result = result.reset_index(drop=True) ## resetting it to reformat the index
result.head()

# %%
#  dropping to all form of duplicates 

result = my_df.drop_duplicates(keep=False)
result.head()

# %%
# droping duplicates by column or variable

result = my_df.drop_duplicates(subset=['Score'])
result.head()

# %%
# Removing Duplicate Columns
# Let’s create a dummy dataset that contains duplicate column 
# names and duplicate values for all rows for different columns.

scores = [['Mathematics', 85, 'Science', 85],
['English', 91, 'Arts', 91],
['History', 95, 'Chemistry', 95],
['History', 95, 'Chemistry', 95],
['English', 95, 'Chemistry', 95],
]
my_df = pd.DataFrame(scores, columns = ['Subject', 'Score', 'Subject',
'Percentage'])
my_df.head()

# %%
# Let’s first remove the columns with duplicate names and values

result = my_df.loc[:,~my_df.columns.duplicated()]
result.head()

# %%
result = my_df.T.drop_duplicates().T
result.head()

# %% [markdown]
# # Pivot and Crosstab

# %%
# let's import some data
import matplotlib.pyplot as plt
import seaborn as sns
flights_data = sns.load_dataset('flights')
flights_data.head()

# %%
# this pivot.tabe changed the row to be month and column to year and value to be passengers

flights_data_pivot =flights_data.pivot_table(index='month',columns='year', values='passengers')
flights_data_pivot.head()

# %%
# cross tabulation

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# sets the default style for plotting
sns.set_style("darkgrid")
titanic_data = sns.load_dataset('titanic')
titanic_data.head()

# %%
# cross tabulation 
pd.crosstab(titanic_data["class"], titanic_data["age"], margins=True)

# %%
# Discretization and BinningDiscretization or 
# binning refers to creating categories or bins using numeric data
# Let's use the titanic data

titanic_data['age_group']=pd.cut(x = titanic_data['age'], bins =
[0,5,20,60,100], labels = ["toddler", "young", "adult","senior"])
titanic_data['age_group'].value_counts()

# %%
# find the minimum, maximum, median, 
# and mean values for ages and fare paid by
# passengers of different genders.

#By age
titanic_gbsex= titanic_data.groupby("sex") # group by clause
titanic_gbsex.age.agg(['max', 'min', 'count', 'median', 'mean'])

# %%
# by fare
titanic_gbsex.fare.agg(['max', 'min', 'count', 'median', 'mean'])


