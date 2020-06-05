import operator

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

def strassen(X, Y):
    """
    X, Y: Matrices of size nxn (where n is power of 2).
    Returns the matrix multiplication by means of the Strassen's algorithm.
    """
    assert len(X) == len(Y)
    n = len(X)
    if n is 1:
        return [X[0][0] * Y[0][0]]
    else:
        # 1. Subdivide the matrices by half their size.
        A, B, C, D = halfSplit(X)
        E, F, G, H = halfSplit(Y)
        # 2. Cleverly compute seven recursions.
        P1 = strassen(A, operate([F, H], operator.sub))
        P2 = strassen(operate([A, B], operator.add), H)
        P3 = strassen(operate([C, E], operator.add), D)
        P4 = strassen(D, operate([G, E], operator.sub))
        P5 = strassen(operate([A, D], operator.add), operate([H, E], operator.add))
        P6 = strassen(operate([B, D], operator.sub), operate([G, H], operator.add))
        P7 = strassen(operate([A, C], operator.sub), operate([E, F], operator.add))
        # 3. Cleverly adds and subtracts each recursion.
        return [
                [operate([operate([P1, P4, P6], operator.add), P2], operator.sub), operate([P1, P2], operator.add)],
                [operate([P3, P4], operator.add), operate([operate([P1, P5], operator.add), P3, P7], operator.sub)]
                ]

def halfSplit(M):
    """
    M: Matrix of size nxn.
    Returns four matrices of size (n/2)x(n/2)
    """
    n = len(M)
    n2 = len(M) // 2
    r = {}
    # 1. Init the resulting parts as empty matrices.
    for i in range(4):
        r[i] = [[None for j in range(n2)] for i in range(n2)]
    # 2, Build the four parts with one swept.
    for i in range(n):
        for j in range(n):
            # 2.1. Define the indexes and the new host for the value.
                    ni, nj, h = decideHost(i, j, n2)
                    r[h][ni][nj] = M[i][j]
    return (r[0], r[1], r[2], r[3])

def decideHost(i, j, n):
    """
    i: Row index on the original matrix.
    j: Column index on the original matrix.
    n: Target size of the new matrix.
    Returns the sub-matrix and new row/column index.
    """
    h = 2 if i >= n else 0
    h = h+1 if j >= n else h
    ni = abs(n - i) if i >= n else i
    nj = abs(n - j) if j >= n else j
    return (ni, nj, h)

def operate(matrices, operator):
    """
    matrices: Set of matrices of size nxn.
    operator: Either addition (+) or subtraction (-).
    Returns the resulting matrix after sum or sub.
    """
    n = len(matrices[0])
    r = matrices[0]
    for m in range(1, n):
        for i in range(n):
            for j in range(n):
                r[i][j] = operator(r[i][j], matrices[m][i][j])
    return r

# Ussage:
# 1. Define the matrices:
x = [[2, 1],[3, 4]]
y = [[5, 6],[7, 8]]
# **brute force**:
# r = directMultiplication(x, y)
# **strassen**:
# r = strassen(x, y)
# print(r)
