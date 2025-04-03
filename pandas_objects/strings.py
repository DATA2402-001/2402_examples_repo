import pandas as pd

s1 = pd.Series(['Mouse', 'dog', 'house and parrot', '23'])
contains_ou = s1.str.contains('ou')
print(contains_ou)
print(s1[contains_ou])