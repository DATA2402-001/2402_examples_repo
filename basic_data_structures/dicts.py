# create a dictionary
months = {
    'january': 1,
    'february': 2,
    'march': 3
}

# retreive the value for "january"
print(months['january'])

# accessing a key that's not in there gives an error
# print(months['julianuary'])

# create a new key-value pair
months['julianuary'] = 13
print(months['julianuary'])

# check to see if a key exists with "in"
'january' in months

# read a value using "get"
months.get('abc', 0)

# note keys must be hashable
# months[['a', 'c']] = 5

# looping through key-value pairs
for key, value in months.items():
    print(key, value)