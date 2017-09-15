import numpy as np

triangle = np.array([
   [-3, 1, 1],
   [4, 4, 0]
])

transform = np.array([
    [2, -1],
    [1, 2]
])

print(np.dot(transform, triangle))