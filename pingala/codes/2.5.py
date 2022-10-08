import numpy as np
import matplotlib.pyplot as plt

def x(n):
    if (n==0 or n==1):
        return 1
    elif (n<0):
        return 0
    return x(n-1)+x(n-2)

def y(n):
    return x(n-1)+x(n+1)

Y = [0]*15
for i in range(15):
    Y[i] = y(i)

plt.stem(range(0,15),Y)
plt.ylabel('$y(n)$')
plt.xlabel('$n$')
plt.grid()
plt.savefig('pingala/figs/2.5.png')