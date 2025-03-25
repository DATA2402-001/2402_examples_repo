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

# slide #11 exercise
df['>85 rating'] = df['rating'] > 85
pt = df.pivot_table(
    index=['dept', 'product'],
    columns=['year', '>85 rating'],
    values=['sales', 'rating'],
    aggfunc={'sales': 'sum', 'rating': 'mean'}
)
print(pt)
# get total sales for houseware/rug in 2016 with < 85 rating
print(pt.loc[('houseware', 'rug'), ('sales', 2016, False)])