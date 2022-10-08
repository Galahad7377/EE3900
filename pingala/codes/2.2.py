import numpy as np
import matplotlib.pyplot as plt

def x(n):
    if (n==0 or n==1):
        return 1
    return x(n-1)+x(n-2)

X = [0]*15
for i in range(15):
    X[i] = x(i)

plt.stem(range(0,15),X)
plt.ylabel('$x(n)$')
plt.xlabel('$n$')
plt.grid()
plt.savefig('pingala/figs/2.2.png')
