""" 
Created on: May 5, 2020
Author efmcuiti
Testing file for algorithms.
"""
def directMultiplication(A, B):
	"""
	A, B: Matrices of size nxn.
	
	Returns the matrix resulting on the brute force multiplication AxB.
	"""
	assert len(A) == len(B)
	n = len(A)
	Z = [[None for j in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			Z[i][j] = 0
			for k in range(n):
				Z[i][j] += A[i][k] * B[k][j]
	return Z

# #Ussage:
# **brute force**:
# 1. Define the matrices:
# x = [[2, 1],[3, 4]]
# y = [[5, 6],[7, 8]]
# r = directMultiplication(x, y)
# print(r)