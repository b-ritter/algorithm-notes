import numpy as np
import unittest

A = np.array([
    [-7, 0],
    [-6, 3]
    ])
possible_A_inverse = np.array([[2/11, 5/11], [-1/22, 3/22]])

# print(np.allclose(np.linalg.inv(A), possible_A_inverse))

print(np.linalg.inv(A))
# print(possible_A_inverse)