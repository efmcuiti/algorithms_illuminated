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
	Z = [[None for j in range(len(A))] for i in range(len(A))]
	for i in len(A):
		for j in len(A):
			Z[i][j] = 0
			for k in len(A):
				Z[i][j] += A[i][k] * B[k][j]
	return Z