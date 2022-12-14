import numpy as np

N=15
def x(n):
    if n < 0 or n > 5:
        return 0
    elif n < 4:
        return n + 1
    else:
        return 6 - n
def delta(n):
    if n == 0:
        return 1
    else:
        return 0
def h(n):
    if n == 0:
        return 1
    elif n > 0:
        return delta(n) + delta(n-2) - 0.5*h(n-1)
    else:
        return 2*(delta(n+1) + delta(n-1) - h(n+1))
def X(k):
    sum=0
    for n in range(N):
        sum = sum + x(n)*(np.exp(-2j*np.pi*k*n/N))
    return abs(sum)
def H(k):
    sum=0
    for n in range(N):
        sum = sum + h(n)*(np.exp(-2j*np.pi*k*n/N))
    return abs(sum)
def Y(k):
    return X(k)*H(k)
