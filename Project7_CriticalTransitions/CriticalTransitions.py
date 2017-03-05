import matplotlib.pyplot as plt
import random
import math

h = 0.0
r = 3.0
sigma = 0.01

maxt = 20.0
dt = 0.1 # step size
N = maxt/dt # number of steps

# Initial conditions
t = [0.0]
u = [2] # Stock Index

def f(u):
    return -h + r*u - u**3

def dW(dt):
    return math.sqrt(dt) * random.normalvariate(0, 1)

for i in range(0,int(N)):
    K = f(u[i]) * dt + sigma * dW(dt)

    u.append(u[i] + (dt * f(u[i] + K/2.0) + sigma * dW(dt)))
    t.append(t[i] + dt)

plt.plot(t, u)
plt.show()