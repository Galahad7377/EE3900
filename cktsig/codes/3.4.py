import numpy as np
import matplotlib.pyplot as plt


def v(t):
    return (2/3)*(1+np.exp((-1.5e6)*t))

t = np.linspace(0,7e-6)
plt.plot(t,v(t))
plt.grid()
plt.xlabel('$t$')
plt.ylabel('$v_c$')
plt.savefig('cktsig/figs/3.4.png')