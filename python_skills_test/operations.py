
# get inputs
cash = input('enter an amount of cash (including $)')
n_people = int(input('enter number of people'))
pennies = 100 * float(cash[1:])

# processing
pennies_per_person = pennies // n_people
pennies_left_over = pennies % n_people

# output
print(f'${pennies_per_person / 100} each')
print(f'{pennies_left_over} pennies left over')