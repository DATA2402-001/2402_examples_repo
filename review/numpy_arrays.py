import numpy as np

twoD_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

arr = np.array(twoD_list)

arr[:, 0] # get first column
arr[1, 1] # get element (1, 1)
arr[-2:, -2:] # get bottom 2x2 square
arr + arr # vector math
arr * arr # element-wise multiplication

arr1d = np.array([1, 2, 3])
arr2d = np.array([[1, 2], [3, 4]])

# boolean & comparison
bigger_than_3 = arr > 3
print(arr[bigger_than_3])

# universal functions
arr.sum() # sum all values
print(arr.sum(axis=0)) # sum columns
print(arr.sum(axis=1)) # sum rows
np.sqrt(arr) # vectorized sqrt
