import matplotlib.pyplot as plt
import random
import numpy as np
import math

h = 0.0
r = 3.0
sigma = 0.1
dt = 0.1

# Initial conditions

u = np.arange(-2.0, 2.0, 0.01) # Stock Index

def h(u):
    return r*u - u**3

def dW(dt):
    return math.sqrt(dt) * random.normalvariate(0, 1)

h = [h(ui) + sigma*dW(dt)/dt for ui in u]
    
plt.plot(h, u)
plt.show()