import numpy as np

predicted = np.array([2, 4, 1, 6, 8, 4])
actual = np.array([4, 4, 0, 3, 7, 6])

error = predicted - actual
sq_error = error * error
mse = sq_error.mean()

print(mse)
