import numpy as np

A = (1+np.sqrt(5))/2
B = (1-np.sqrt(5))/2
n = 100

def a(n):
    return (A**n-B**n)/(A-B)

def b(n):
    return a(n-1)+a(n+1)

sum = 0
for i in np.linspace(1,n,n):
    sum += a(i)
print(a(n+2)-1-sum)

sum = 0
for i in np.linspace(1,n,n):
    sum += a(i)/(10**i)
print(sum - 10/89)

print(b(n) - A**n - B**n)

sum = 0
for i in np.linspace(1,n,n):
    sum += b(i)/(10**i)
print(sum - 8/89)

