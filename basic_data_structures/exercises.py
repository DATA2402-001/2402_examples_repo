# incrementing each value in a list by 1
def increment_each_by_one(l: list) -> list:
    return [element + 1 for element in l]

my_list = [0, 1, 2, 3, 4]
new_list = increment_each_by_one(my_list)
print(my_list)
print(new_list)



# associating month names with numbers
def get_month_number(month_name: str) -> int:
    months = ['jan', 'feb', 'mar', 'apr']
    numbers = [1, 2, 3, 4]

    for index in range(len(months)):
        if months[index] == month_name:
            return numbers[index]

# do it with a dict
months = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4}
months['jan']

print('jan'.__hash__())
print('abcd'.__hash__())

months.get('jan')