# LU Decomposition Method (Doolittle's Method)

import numpy as np

A = np.array([
    [1, 1, 1],
    [4, 3, -1],
    [3, 5, 3]
], dtype=float)

B = np.array([1, 6, 4], dtype=float)

n = len(B)

L = np.zeros((n, n))
U = np.zeros((n, n))

# LU Decomposition
for i in range(n):
    L[i][i] = 1

    for j in range(i, n):
        U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

    for j in range(i + 1, n):
        L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

# Forward substitution (Ly = B)
y = np.zeros(n)
for i in range(n):
    y[i] = B[i] - sum(L[i][j] * y[j] for j in range(i))

# Backward substitution (Ux = y)
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

# Output
print("Solution:")
print("x1 =", round(x[0], 4))
print("x2 =", round(x[1], 4))
print("x3 =", round(x[2], 4))
