user_input = input('enter a number, q to quit')
list_o_nums = []

while user_input != 'q':
    user_input = int(user_input)
    list_o_nums.append(user_input)

    list_o_nums = list_o_nums[-3:]
    # if len(list_o_nums) > 3:
    #     del list_o_nums[0]

    print(list_o_nums)
    average = sum(list_o_nums) / len(list_o_nums)
    print(average)

    user_input = input('enter a number, q to quit')