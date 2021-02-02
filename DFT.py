"""
Numerical methods examples

Discrete Fourier transform

Anni Kauniskangas
3.1.2021
"""
import numpy as np
import matplotlib.pyplot as plt


def DFT(f,dt,T):
    t = np.arange(0,T,dt)  # Time samples
    f_n = np.array([f(time) for time in t])  # Time domain samples
    N = len(f_n)
    p = np.arange(-N/2,N/2,1)
    w_p = 2*np.pi/(N*dt) * p  # Frequencies
    f_p = []

    for w_p_val in w_p:
        sumf = 0
        for n in range(0,N):
            sumf += f_n[n] * np.exp(1j*w_p_val*t[n])
        f_p.append(sumf)
    f_p = np.array(f_p)  # Frequency domain samples
    return w_p,f_p

# Testing
def f(t):
    y = np.cos(t) + np.cos(2*t) + np.cos(4*t)
    return y

dt = 0.001*2*np.pi
omegas, vals = DFT(f,dt,2*np.pi)
vals *= dt  # Multiply back by dt
plt.plot(omegas,vals)
plt.show()