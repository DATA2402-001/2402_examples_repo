import pandas as pd

df = pd.read_csv('./groupby/sales.csv')

# basic groupby usage
grouped = df.groupby('year')
print(grouped['sales'].sum()) # returns a Series

# can do it all in one step by chaining the operations
print(df.groupby('year')['sales'].sum())

# group by multiple columns
multi_index_series = df.groupby(['year', 'dept'])['sales'].sum()
print(multi_index_series.index) # note the series has a "MultiIndex" - tuples of year-dept combos

# what was the most successful product-year?
totals = df.groupby(['year', 'dept'])['sales'].sum()
print(totals)

print(totals.sort_values().index[-1]) # sort and take the last index

# index all entries from the series that equal the max value
# (this way will return multiple rows if there are ties for highest)
biggest = totals.max()
print(totals[totals == biggest])

# use argmax to identify the numerical position of the largest total
print(totals.index[totals.argmax()])