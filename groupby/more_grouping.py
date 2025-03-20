import pandas as pd

df = pd.read_csv('./groupby/sales.csv')

# average rating by product
print(df.groupby('product')['rating'].agg('mean'))

# Total sales by year, only for the houseware dept.
df.loc[df['dept'] == 'houseware'].groupby('year')['sales'].sum()

# The ratio of total_sales / average_rating by department
aggregated = df.groupby('dept').agg({'sales': 'sum', 'rating': 'mean'})
print(aggregated['sales'] / aggregated['rating'])