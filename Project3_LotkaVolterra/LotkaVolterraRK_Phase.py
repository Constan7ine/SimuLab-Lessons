import matplotlib.pyplot as plt

a1 = 2.0 # Prey growth rate when there are no predators
a2 = 1.0 # Predator growth rate when there are no prey
b1 = 1.0 # predators supressing prey growth rate
b2 = 1.0 # enhancement of predator growth rate because of prey

maxt = 20.0
dt = 0.1 # step size
N = maxt/dt # number of steps

# Initial conditions
t = [0.0]
x = [0.9] # Prey Population
y = [1.0] # Predator Population

def f(x, y):
	return  (a1 - b1*y)*x

def g(x, y):
	return (-a2 + b2*x)*y

for i in range(0,int(N)):
	K = f(x[i], y[i]) * dt
	I = g(x[i], y[i]) * dt

	x.append(x[i] + dt * f(x[i] + K/2.0, y[i] + I/2.0))
	y.append(y[i] + dt * g(x[i] + K/2.0, y[i] + I/2.0))
	t.append(t[i] + dt)

plt.plot(x, y)
plt.show()