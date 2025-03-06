import numpy as np

map_coords = np.random.random((100, 2))
our_position = np.array([0.5, 0.5])

# compute all 100 taxicab distances
diff = map_coords - our_position
abs_diff = np.abs(diff)
distances = abs_diff.sum(axis=1)
print(distances)