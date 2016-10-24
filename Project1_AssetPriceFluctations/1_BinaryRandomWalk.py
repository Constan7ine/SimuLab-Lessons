# Basic binary random walk
# Asset prices follow a model like this for the most part
# However external influences are more regular than you think and will massively 
# effect the model, creating great discontinuities

# Import necessary modules
import time
import random
import matplotlib.pyplot as plt

# Seeding the random pseudo random functions
random.seed(time.time())

# Our X range
nPeriods = 60
time = range(nPeriods)

# Starting value
prices = [0]

# For each step, pic a random direction, apply parameters, 
# and then add the previous value so displacement is cumulative
for period in range(1, nPeriods):
	price = random.choice([-1, 1])
	price += prices[period-1]
	prices.append(price)

# Plot
plt.plot(time, prices)
plt.show()