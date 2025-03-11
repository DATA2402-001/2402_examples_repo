import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'patient_id': [123, 521, 888, 123],
        'height': [1.8, 5.8, 1.6, 5.9],
        'weight': [140,  3000,  999,  140],
    }
)

# convert heights in m (heights <2) to ft (*3.3)
df.loc[df['height'] < 2, 'height'] *= 3.3

# replace weights > 300 with np.nan
df.loc[df['weight'] > 300, 'weight'] = np.nan

print(df)