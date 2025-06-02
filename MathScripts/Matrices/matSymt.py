# This script checks if a matrix is Symmetic, by comparing it to its transpose.
import numpy as np

# Define the matrix
A = np.array([[1, 2, 3],
              [2, 2, 2],
              [3, 2, 3]])

# Check if the matrix is symmetric
if np.array_equal(A, A.T):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")
