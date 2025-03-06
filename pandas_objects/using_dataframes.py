import pandas as pd

df = pd.DataFrame(
    {'sales': [10, 12, 8], 'overhead': [5, 8, 9]},
    index=['jan', 'feb', 'mar']
)
print(df)

# create a new column showing profit
# (subtract the “overhead” series from the “sales” series)
df['profit'] = df['sales'] - df['overhead']
print(df)

# access more than one column
print(df[['sales', 'overhead']])

# use iloc attribute to access a view of the dataframe 
# that supports numpy-like indexing
print(df.iloc[:,0])

# use loc attribute to index using the dataframe's own index values
print(df.loc[:, 'sales'])
print(df.loc[['jan', 'feb'], 'overhead'])

# this doesn't modify the original table, just
# the slice returned by .loc[['jan', 'feb']]
df.loc[['jan', 'feb']]['profit'] = 10
print(df)

# this modifies the original table
df.loc[['jan', 'feb'], 'profit'] = 10
print(df)


# some dataframe manipulation
data = {
    "Day": ["Monday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Product": ["Apples", "Bananas", "Apples", "Oranges", "Apples", "Bananas", "Oranges", "Bananas"],
    "Units Sold": [10, 15, 8, 12, 14, 20, 10, 18],
    "Price per Unit ($)": [1.5, 0.8, 1.5, 1.2, 1.5, 0.8, 1.2, 0.8],
}
df = pd.DataFrame(data)
df['total sales'] = df['Units Sold'] * df['Price per Unit ($)']
# reduce to rows with >10 units sold
print(df.loc[df['Units Sold'] > 10, ['Day', 'Product', 'Units Sold']])
