import pandas as pd

df = pd.read_csv('./pivot_table/sample_data.csv')

pt = df.pivot_table(
    index=['dept', 'product'],
    columns='year',
    values='sales',
    aggfunc='sum'
)

print(pt)

# get same info using groupby
print(df.groupby(['dept', 'product', 'year'])['sales'].agg('sum'))