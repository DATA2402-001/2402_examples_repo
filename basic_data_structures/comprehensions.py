
# let's make a list with all the numbers from 1 to 10
# the long way
my_list = []
for num in range(1, 11):
    my_list.append(num)

# with a list comprehension:
my_list = [num for num in range(1, 11)]

# make one that has 2x all those numbers
my_list = [2*num for num in range(1, 11)]

# make one that has 2x all those numbers, but only up to 6
my_list = [2*num    for num in range(1, 11)     if 2*num <= 6]
