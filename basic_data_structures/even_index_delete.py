def delete_even_indices(l: list) -> list:
    """
    accepts a list, and deletes all the even-numbered items from the list.
    So the list	['a', 'b', 'c', 'd']
    becomes	['b', 'd']
    """

    for i in range(len(l)-1, -1, -1):
        print(i)
        if i % 2 == 0:
            del l[i]
    return l

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
new_list = delete_even_indices(my_list)
print(new_list)