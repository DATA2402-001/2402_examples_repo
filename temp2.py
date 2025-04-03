import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score
import numpy as np


data = pd.read_csv('C:/Users/echalmers/Downloads/A4data (1)/stats.csv')

# drop fights that don't have a result
data = data.loc[~data['result'].isna(), :]

# drop the text columns
data.drop(['fight', 'fighter', 'opponent', 'fighter_url'], axis=1, inplace=True)

# fill missing values
data.loc[data['sig. str. %'].isna(), 'sig. str. %'] = 0
data.loc[data['td %'].isna(), 'td %'] = 0

# split into X (predictors) and Y (targets)
x = data.drop('result', axis=1)
y = data['result'] == 'win'

# split data into training and test
# training_idx = np.random.rand(len(data.index)) < 0.66
x_train = x.loc[training_idx]
y_train = y.loc[training_idx]
x_test = x.loc[~training_idx]
y_test = y.loc[~training_idx]


model = LogisticRegression()
model.fit(x_train, y_train)

predictions = model.predict(x_test)
print('r2', accuracy_score(predictions, y_test))
