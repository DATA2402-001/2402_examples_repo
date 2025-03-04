import numpy as np
import time

data1 = np.array([1, 2, 3, 4])  # a 1-D array (vector)
data2 = np.array([[1, 2], [3, 4]])  # a 2-D array

print(data1)
print(data2)


# multiply all elements of an array by 2
# native python
start_time = time.time()
array = np.array([i for i in range(1_000_000)])
for index in range(len(array)):
    array[index] *= 2
end_time = time.time()
print(end_time - start_time)

# in numpy
start_time = time.time()
array *= 2
end_time = time.time()
print(end_time - start_time)


# access some ndarray attributes
print(data1)
print(type(data1))
print(data1.ndim, data2.ndim)
print(data1.shape, data2.shape)


# create ndarray with a specific datatype
arr1 = np.array([1, 2, 3], dtype=np.float64)
print(arr1.dtype)
print(arr1.astype(np.int32).dtype)

# some ndarray methods
array = np.arange(0, 10)
print(array)
print(array.sum())
print(array.cumsum())
print(array.argmax())


# some arithmetic
arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 3, 4])

arr1 * 2  # give [2, 4, 6]
arr1 * arr2  # gives [2, 6, 12]
arr1 + arr2  # gives [3, 5, 7]

# comparisons
print(arr1 > arr2)
print(np.array([1, 2, 3]) > np.array([3, 2, 1]))
