# Each timestep we calculate the two probabilities
# We pick a random number and use the probabilities to see if X increases or decreases that timestep
# It's important to note that when picking random numbers for a probability, 
# what you want is for the number to be inside a range the size of the probability

import time
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

random.seed(time.time())

N = 100 # Number of ants total
sigma1 = 1 # Opinion on food source 1
sigma2 = 1 # Opinion on food source 2
herding = 50 # How strongly do the ants follow the herd?

deltaT = 2.0/float(N*(sigma1 + sigma2 +herding*N))
print(deltaT)

time = np.arange(0, 20, deltaT)

fig, ax = plt.subplots()
line, = ax.plot([time[0]], [50])

xs = np.array([50])

def update(i, time, line):
	global xs

	for x in xrange(0, 500):
		x = xs[-1]
		pplus =(N-x)*(sigma1+herding*x)*deltaT 
		pmin = x*(sigma2 + herding*(N-x))*deltaT
		rnd = random.random()
		if rnd < pplus: # If random number is less than probability of increase then increase Example: pplus = 0.4 rnd = 0.245
			x += 1
		elif rnd < (pplus + pmin): # If rnd is greater than pplus but less than both, then it must be pmin Example pplus = 0.6 pmin = 0.2 rnd = 0.712
			x -= 1
		xs = np.append(xs, x)

	line.set_data(time[:i*50],xs[:i*50])
	line.axes.axis([0, 0.5, 0, 100])
	return line,


ani = animation.FuncAnimation(fig, update, len(time), fargs=[time, line], interval=20, blit=True)
plt.show()