# This scipt calculates the boolean product between to matrices. 

import numpy as np

def boolean_product(A, B):
    # Convert to NumPy arrays if not already
    A = np.array(A)
    B = np.array(B)
    
    # Get dimensions
    m, n = A.shape
    n2, p = B.shape
    assert n == n2, "Incompatible dimensions for matrix multiplication"
    
    # Initialize result matrix
    C = np.zeros((m, p), dtype=int)
    
    for i in range(m):
        for j in range(p):
            C[i][j] = np.any(A[i, :] & B[:, j])  # Logical AND followed by OR
    
    return C

# Example
A = [[1, 1, 0],
     [1, 0, 1],
     [0, 1, 0]]

B = [[1, 1, 0],
     [1, 0, 1],
     [0, 1, 0]]

C = boolean_product(A, B)
print(C)
