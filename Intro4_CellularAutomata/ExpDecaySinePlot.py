import matplotlib.pyplot as plt
import numpy as np
import math

time = np.asarray(np.arange(0.0, 5.0, 0.01))

x = []
for t in time:
	x.append(math.exp(-t) * math.sin(t*3.14159*2))

plt.plot(time, x)
plt.show()
