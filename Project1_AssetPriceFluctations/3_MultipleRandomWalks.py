# In this we demonstrate code reuse and abstraction using a function
# everything else is left the same

# Import necessary modules
import time
import random
import matplotlib.pyplot as plt

def RandomWalk(drift, scale, nPeriods):
	# Starting value
	prices = [0]
	# For each step, pic a random direction, apply parameters, 
	# and then add the previous value so displacement is cumulative
	for x in range(1, nPeriods):
		price = drift + scale*random.uniform(-1, 1)
		price += prices[x-1]
		prices.append(price)

	return prices

# Seeding the random pseudo random functions
random.seed(time.time())

# Our X range
nPeriods = 500
time = range(nPeriods)

# Parameters
drift = 0.0001
scale = 0.01

# Random walk some amount of times
for walk in range(1,10):
	prices = RandomWalk(drift, scale, nPeriods)
	plt.plot(time, prices)

# Draw the plot
plt.show()



	