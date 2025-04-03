from datetime import datetime, timedelta
import pandas as pd

d1 = datetime(year=2010, month=11, day=30, hour=12)
d2 = datetime(year=2012, month=7, day=21, hour=12, minute=15)

# subtracting datetime objects gives a timespan object
span = d2 - d1
print(type(span), span)

# adding a timespan to a datetime gives another datetime
print(d1 + timedelta(days=2, hours=1))


# vectorized operations on pandas datetime series
s1 = pd.to_datetime(pd.Series([
    '25/02/2000',
    '26/02/2000',
    '27/02/2000',
    '28/02/2000',
]))

s2 = pd.to_datetime(pd.Series([
    '25/05/2000',
    '26/05/2000',
    '27/05/2001',
    '28/05/2001',
]))

print(s2 - s1) # a series of timedeltas
print((s2 - s1) > timedelta(days=100)) # which deltas are over 100 days?