from pandas import Series

s1 = Series({'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000})
s2 = Series({'Ohio': 10000, 'Texas': 1000, 'Oregon': 5000})

# adding the series automatically aligns on index values
s3 = s1 + s2
print(s3)



temperature = Series(
    [22.5, 24, 19.8, 21, 23.3, 25.1, 20.7],
    index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    name='temperatures'
)

# find the differnce between min and max temperatures
temp_range = temperature.max() - temperature.min()

# get names of days with temperature > 22°
bigger_than_22 = temperature > 22
print(temperature[bigger_than_22].index)

# convert to °F
temperature_f = temperature * 9/5 + 32
print(temperature_f)