import matplotlib.pyplot as plt

a1 = 2.0 # Prey growth rate when there are no predators
a2 = 1.0 # Predator growth rate when there are no prey
b1 = 1.0 # predators supressing prey growth rate
b2 = 1.0 # enhancement of predator growth rate because of prey

maxt = 50.0
dt = 0.01 # step size
N = maxt/dt # number of steps

# Initial conditions
t = [0.0]
x = [1.0]
y = [1.1]

for i in range(0,int(N)):
	dxdt = (a1 - b1*y[i])*x[i]
	dydt = (-a2+b2*x[i])*y[i]
	x.append(x[i] + dxdt * dt)
	y.append(y[i] + dydt * dt)
	t.append(t[i] + dt)


plt.plot(t, x, t, y)
plt.show()