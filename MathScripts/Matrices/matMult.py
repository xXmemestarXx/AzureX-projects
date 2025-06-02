# This script calculates the multiplication of two matrices, and the square.
# Example Python3 Code for the lecture on Graph Theory in DM534 by Daniel Merkle Nov. 28, 2017.

from math import *
from copy import *

# Assume M and N are both square (size x size) matrices 
def multSquareMatrices(M,N):
    size = len(M)
    result = [[0 for x in range(size)] for y in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] = result[i][j] + M[i][k] * N[k][j]
                
    return result

# Assume two matrices M and N, not necessarily squared
# (not needed further on in the lecture) 
def multGeneral(M,N):

    result = [[0 for x in range(len(N[0]))] for y in range(len(M))]

    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range(len(N)):
                result[i][j] = result[i][j] + M[i][k] * N[k][j]
                
    return result
   

def printMatrix(M):
    for row in M:
        print(["%3.0f" % a for a in row])
    print("\n")

M = [[ 1, 2],
     [2, 3]]
    
N = [[ 3, 2],
     [ 1, 2]]

S = [[ 1, 2, 0],
     [ 2, 0, 1],
     [-1, 2, 3]]
    
print("Initial Matrix M:\n")
printMatrix(M)

print("Initial Matrix N:\n")
printMatrix(N)

print("M x N:\n")
printMatrix( multGeneral(M,N) )

print("Initial Matrix S:\n")
printMatrix(S)

print("S x S:\n")
printMatrix( multSquareMatrices(S,S) )
