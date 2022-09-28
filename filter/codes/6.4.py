import numpy as np
import matplotlib.pyplot as plt

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
x_a = [0]*N
h_a = [0]*N
for n in range(N):
    x_a[n] = x(n)
    h_a[n] = h(n)
X = np.fft.fft(x_a)
H = np.fft.fft(h_a)
Y = X*H
y_a = np.fft.ifft(Y)
plt.stem(range(0,N),abs(y_a))
plt.show
print(y_a)