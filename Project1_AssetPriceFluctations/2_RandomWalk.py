# In this we extend the model to so we can control the standard deviation and the mean of the distribution
# Furthermore we are no longer bound to a binary distribution, and use a range of floating point values
# We also learn about more ways of plotting information

# Import necessary modules
import time
import math
import random
import matplotlib.pyplot as plt

# Seeding the random pseudo random functions
random.seed(time.time())

# Our X range
nPeriods = 300
time = range(nPeriods)

# Parameters
drift = 0.002 # Also mu, the mean of the distribution
scale = 0.01   # Also sigma, the standard deviation

# Starting value
prices = [0]

# For each step, pic a random direction, apply parameters, 
# and then add the previous value so displacement is cumulative
for period in range(1, nPeriods):
	price = drift + scale*random.uniform(-1, 1)
	price += prices[period-1]
	prices.append(price)

# First use of list comprehension, used to find a line showing the upper edge the random walk should travel to
lower_bound = [period*drift - scale*math.sqrt(period) for period in time]
upper_bound = [period*drift + scale*math.sqrt(period) for period in time]

# Plot
plt.figure(1)
plt.plot(time, prices)
# Plot the line drawn by parameters, i.e. mean of distribution
plt.plot(time, [period*drift for period in time], ls='--')
# Plot an area between the bounds
plt.fill_between(time, lower_bound, upper_bound, facecolor='yellow', alpha=0.5)

# Lets plot a histogram so we can see the normal distribution. Note, drift needs to be one, or use a new range of random variables
norm = []
for i in range(20000):
	val = random.gauss(drift, scale)
	norm.append(val)

plt.figure(2)
plt.hist(norm, 100)

plt.show()