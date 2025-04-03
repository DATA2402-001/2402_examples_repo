import pandas as pd

df = pd.DataFrame(
    {'a': [1, 2, 3], 'b': [4, 5, 6]},
    index=['monday', 'tuesday', 'wednesday']
)

# retrieve a particular column (Series)
df['a'] # return the series for column a

# select multiple columns
df[['a', 'b']] # returns the dataframe containing cols a and b

# get list of columns and row index using attributes
df.columns
df.index

# do vectorized operations between columns
df['c'] = df['a'] - df['b']

# use loc and iloc for getting slices or specific values
print(df.loc['tuesday', 'c']) # returns float
print(df.loc['monday':'tuesday', 'a']) # returns series
print(df.loc[:, ['a', 'c']]) # returns dataframe

# boolean indexing
print(df.loc[(df['a'] > 1) & (df['b'] > 5), :])

# aggregations
print(df.sum(axis=0)) # returns a Series with col names as index
print(df.sum(axis=1)) # returns a Series with same row idx as df