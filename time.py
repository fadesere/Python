# %%
import pandas as pd
import seaborn as sns
sns.set_style("darkgrid")

my_df = pd.read_csv('STOCK_US_XNAS_GOOG2.csv')

my_df.tail()

# %%
my_df['Date'] = pd.to_datetime(my_df['Date'])
my_df = my_df.set_index('Date')
my_df.tail()

# %%
# converting selected variables to float
my_df[['Open','High','Low']] = my_df[['Open','High','Low']].replace(',','',regex=True).astype(float)
my_df.head()

# %%
my_df2=my_df.replace(',','',regex=True).astype(float) # converts all dataframe to float
my_df2.head()


# %%

my_df2.plot.line( y='Open', figsize=(12,8))


