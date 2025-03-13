import pandas as pd
import numpy as np
import time


df = pd.DataFrame(
    data=np.random.random((1_000_000, 2)),
    columns=['a', 'b']
    )

# vectorized multiplication of a * b
start = time.time()
df['c'] = df['a'] * df['b']
print(f'{time.time() - start}s elapsed')

# using apply
start = time.time()
df['c'] = df.apply(lambda row: row['a'] * row['b'], axis=1)
print(f'{time.time() - start}s elapsed')

# using native python loop
start = time.time()
for row_index in df.index:
    df.loc[row_index, 'c'] = df.loc[row_index, 'a'] * df.loc[row_index, 'b']
print(f'{time.time() - start}s elapsed')