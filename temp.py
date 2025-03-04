import pandas as pd
import numpy as np


# pop_data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
#         "year": [2000, 2001, 2002, 2001, 2002, 2003],
#         "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
# data = pd.DataFrame(pop_data)




# # these all work
# data.loc[:, "year"] = 1900
# data.iloc[2, :] = 5
# data.loc[data["pop"] > 2, :] = 0

# # this doesn't (it operates on the "year" column of a slice - not the original dataframe)
# data.loc[data['state'] == 'Ohio']['year'] = 2000

# # this is a better way to do the above
# data.loc[data['state'] == 'Ohio', 'year'] = 2000

# print(data)



frame = pd.DataFrame({"b": [4, 7, -3, 2], "a": [0, 1, 0, 1]})

# sort by column b
frame = frame.sort_values("b")

# sort and return as new DataFrame
frame = frame.sort_values('b')

# sort in-place and return None
frame.sort_values('b', inplace=True)
