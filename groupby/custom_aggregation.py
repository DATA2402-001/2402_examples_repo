import pandas as pd

df = pd.DataFrame({
'degree': ['DS', 'DS', 'DS', 'BA', 'BA', 'BA'],
     'num_courses': [3, 4, 5, 3, 4, 5],
     'num_respond': [20, 40, 75, 100, 40, 10]
     })

def weighted_avg_courses(group_df: pd.DataFrame) -> float:
    weighted_sum = (group_df['num_courses'] * group_df['num_respond']).sum()
    return weighted_sum / group_df['num_respond'].sum()

print(df.groupby('degree').apply(weighted_avg_courses))



# the ram-purchasing example
df = pd.DataFrame({
        'date': ['2025-03-01','2025-03-01', '2025-03-02', '2025-03-02', '2025-03-03', '2025-03-03'],
        'customer': ['alice', 'bob', 'alice', 'charley', 'bob', 'charley'],
        'product': ['motherboard', 'ram', 'ram', 'ssd', 'ssd', 'ssd']
})

# group by customer. Aggregate to determine if each customer purchased RAM or not
def ram_in_products(series: pd.Series) -> bool:
    return 'ram' in series.values

print(df.groupby('customer')['product'].agg(ram_in_products))

# anther way
grouped = df.groupby('customer')
print(grouped.apply(lambda dataframe: 'ram' in dataframe['product'].values))
