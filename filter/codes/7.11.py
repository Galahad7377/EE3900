import numpy as np

x = [1,2,3,4,2,1]
N = len(x)
F =  [[0] * N] * N
for m in range(N):
    for n in range(N):
        F[m][n] = np.exp(-2j*m*n*np.pi/N)
X =[0]*N
for i in range(N):
    for j in range(N):
        X[i] += F[i][j]*x[j]
print(X)