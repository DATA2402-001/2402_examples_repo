import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([5, 6, 7, 8], index=['c', 'd', 'e', 'f'])

print(s1)
print(s2)

print(s1 + s2) # auto-aligns using index

# retrieve value at an index (or range/slice of indices)
s1['a']
s1.loc['a':'c']
s1.iloc[0]

# boolean indexing
idx = s1>2
print(idx)
slice = s1[idx]
