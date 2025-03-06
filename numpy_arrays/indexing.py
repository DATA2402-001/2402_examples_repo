import numpy as np

# slicing a list returns a new list
a_list = [0, 1, 2, 3, 4, 5]
a_list_slice = a_list[:3]
print(a_list, a_list_slice)
a_list_slice[0] = 100
print(a_list, a_list_slice)

# slicing an array returns a *view* into the original array
# changing the slice changes the original array
arr = np.array([0, 1, 2, 3, 4, 5])
arr_slice = arr[:3]
arr_slice[0] = 100
print(arr)

# indexing 2d arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[1,1]) # gets middle element
print(arr[1,:]) # gets middle row


# using a boolean array for indexing
arr = np.array([1, 2, 3, 4, 5, 6])
bigger_than_4 = arr > 4  # this is a boolean array
print(arr[bigger_than_4])  # prints([5, 6]), where bigger_than_4 was true
print(arr[[True, False, True, False, True, False]])

# boolean indexing with a 2D array
scores = np.array([
    ['alice', 5],
    ['bob', 3],
    ['cindy', 4],
])
bob_score = scores[scores[:, 0] == 'bob', 1]
print(bob_score)

# boolean operations on logical arrays
arr1 = np.array([True, False])
arr2 = np.array([True, True])
print(arr1 & arr2)
print(arr1 | arr2)
print(~arr1)


# set all negative values to 0
arr = np.array([1, -2, 3, 0, -4, 2])
neg_value_index = arr < 0  # returns [False, True, False, False, True, False]
arr[neg_value_index] = 0
print(arr)


# reduce this table to exclude alice & david 
scores = np.array([
    ['alice', 5],
    ['bob', 3],
    ['cindy', 4],
    ['david', 1],
    ['edith', 2]
])

# step 1: create [False, True, True, False, True]
# by finding out where the first column
# is (NOT alice) AND (NOT david)
names = scores[:,0] # gives the column of names
keep_rows = (names != 'alice') & (names != 'david')  # could also write the negation e.g. ~(names == 'alice')
result = scores[keep_rows, :]
print(result)