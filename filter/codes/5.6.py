import numpy as np

def u(n):
    if n >= 0:
        return 1
    else:
        return 0

def h(n):
    return u(n) * (-0.5)**n + u(n-2) * (-0.5)**(n-2) 

sum = 0
for i in range(100001):
    sum = sum + h(i)
print(sum)