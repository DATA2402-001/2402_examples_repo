
acceptable_flavours = ['vanilla', 'chocolate', 'Neapolitan']
unacceptable_flavours = ['mint-chocolate']
my_empty_list = []


# cast other kinds of sequences to list
numbers = list(range(10))
characters = list('abc')
print(numbers)
print(characters)

# read and write elements of a list by index (lists are mutable)
print(acceptable_flavours[2])
acceptable_flavours[2] = "cookies n cream"

# measure length of a list
print(f'length of the numbers list = {len(numbers)}')

# add an item to a list using the "append" method
my_list = ['a', 'b', 'c']
my_list.append('d')
print(my_list)
