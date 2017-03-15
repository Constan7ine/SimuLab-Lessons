import matplotlib.pyplot as plt
import random
import numpy as np
import math

#random.seed(3)

r = 3.0
sigma = 0.6

maxt = 15.0
dt = 0.01 # step size
N = maxt/dt

def h(u):
    return r*u - u**3

def f(u, t):
    return -t + r*u - u**3

def dW(dt):
    return math.sqrt(dt) * random.normalvariate(0, 1)

u = np.arange(-2.5, 2.3, 0.01)

h = [h(ui) for ui in u]

plt.plot(h, u)

u = [2.4] # Stock Index
t = [-3.9]

for i in range(0,int(N)):
    K = f(u[i], t[i]) * dt + sigma * dW(dt)
    
    newSlope = f(u[i] + K/2.0, t[i] + dt/2.0)
    u.append(u[i] + (dt * newSlope + sigma * dW(dt)))
    t.append(t[i] + dt)

plt.plot(t, u)
plt.show()
