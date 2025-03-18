import pandas as pd

df = pd.read_csv('./groupby/sales.csv')

# basic groupby usage
grouped = df.groupby('year')
print(grouped['sales'].sum()) # returns a Series

# can do it all in one step by chaining the operations
print(df.groupby('year')['sales'].sum())

# group by mulitple columns
multi_index_series = df.groupby(['year', 'dept'])['sales'].sum()
print(multi_index_series.index) # note the series has a "MultiIndex" - tuples of year-dept combos


