import numpy as np
import matplotlib.pyplot as plt

# create an array of 100 random numbers
arr = np.random.random(100)

# scale to between -1 and 1
arr = arr * 2 - 1

# cumulative sum
arr = arr.cumsum()
print(arr)

# plot the random walk (not part of this course yet)
plt.plot(arr)
plt.show()
