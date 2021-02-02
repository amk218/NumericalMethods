"""
Numerical methods examples

Solving the simple harmonic oscillator DE using the Euler method

Anni Kauniskangas
7.1.2021
"""
import matplotlib.pyplot as plt
import numpy as np

def euler_SHO(x0,v0,t_max,dt):
    # Initial conditions
    t = 0
    x = x0
    v = v0
    e = (v**2+x**2)/2
    t_lst = []
    x_lst = []
    energy_lst = []

    # Iterate
    while t <= t_max:
        t_lst.append(t)
        x_lst.append(x)
        energy_lst.append(e)
        a = -x
        v = v + dt*a
        x = x + dt*v
        t = t + dt
        e = (v**2+x**2)/2


    return t_lst,x_lst,energy_lst

# Testing
t,x,e = euler_SHO(0,1,20,0.01)
plt.plot(t,x, label="Numerical solution")
plt.plot(t, np.sin(t), label="Analytic solution")
plt.plot(t, e, label="Energy")
plt.legend()
plt.show()


