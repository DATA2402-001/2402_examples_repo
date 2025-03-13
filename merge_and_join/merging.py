import pandas as pd

# do a left join (instead of the default inner join)
df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "d"],
                    "data1": [1, 2, 3, 4, 5, 6, 7]})

df2 = pd.DataFrame({"key": ['a', 'b', 'c'],
                    'data2': [10, 20, 30]})

joined = pd.merge(df1, df2, on="key", how='left')
print(joined)

# join on two columns
df1 = pd.DataFrame({"key1": ["b", "b", "a", "c", "a", "a", "d"],
                    'key2': ['a', 'a', 'b', 'b', 'c', 'c', 'd'],
                    "data1": [1, 2, 3, 4, 5, 6, 7]})

df2 = pd.DataFrame({"key1": ['a', 'b', 'c', 'e'],
                    'key2': ['a', 'a', 'b', 'd'],
                    'data2': [10, 20, 30, 40]})

joined = pd.merge(df1, df2, on=['key1', 'key2'])
print(joined)

# join where left.key1 matches right.key2 (make it a left join)
joined = pd.merge(df1, df2, left_on='key1', right_on='key2', how='left')
print(joined)


# disambiguating names using suffixes
df1 = pd.DataFrame({"key": ["a", "a", "b", "c", "c", "d", "d"],
                    "data": [1, 2, 3, 4, 5, 6, 7]})

df2 = pd.DataFrame({"key": ['a', 'b', 'c', 'e'],
                    'data': [10, 20, 30, 40]})

joined = pd.merge(df1, df2, on='key', suffixes=['_left', '_right'])
print(joined)
