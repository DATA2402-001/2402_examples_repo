import numpy as np
import pandas as pd

# numpy concatenation
arr = np.array([[0, 1], [2, 3]])
stacked = np.concatenate([arr, arr], axis=1)
print(stacked)

# pandas concat
df1 = pd.DataFrame({'a':[1, 2, 3], 'b': [4, 5, 6]})
df2 = pd.DataFrame({'b':[7, 8, 9], 'c': [10, 11, 12]})

# stack vertically
vert_concat = pd.concat((df1, df2), axis=0)
print(vert_concat)

# stack horizontally
horizontal_concat = pd.concat((df1, df2), axis=1)
print(horizontal_concat)

# use ignore_index
vert_concat = pd.concat((df1, df2), axis=0, ignore_index=True)
print(vert_concat)

# use join='inner'
vert_concat = pd.concat((df1, df2), axis=0, join='inner')
print(vert_concat)