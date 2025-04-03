import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np

stats = pd.read_csv('C:/Users/echalmers/Desktop/A4data/stats.csv')

# drop fights missing a result
stats = stats.loc[~stats['result'].isna(), :]

# drop unused info
stats.drop(['fight','fighter','opponent','fighter_url'], axis=1, inplace=True)

# fill missing percentages with zeros
stats.loc[stats['td %'].isna(), 'td %'] = 0
stats.loc[stats['sig. str. %'].isna(), 'sig. str. %'] = 0

# separate into X and Y
x = stats.drop('result', axis=1)
y = stats['result']

# split data into training and test subsets
training_idx = np.random.rand(len(y)) < 0.66
x_train = x.loc[training_idx, :]
x_test = x.loc[~training_idx, :]
y_train = y[training_idx]
y_test = y[~training_idx]


# instantiate a supervised learning model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# predictions
predictions = model.predict(x_test)

# measure accuracy
print('accuracy: ', (predictions == y_test).mean())