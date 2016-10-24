# for each timestep collect all neighbours in the 2D map
#
# N N N
# N A N         N = Neighbour, A = Agent being calculated
# N N N
#
# The choice state of that agent (+-1) is then:
# = sign(sum over neighbours: (coupling coefficient)(choice state of neighbour)-(individual preference of agent last timestep))
#
# the individual preference for that agent is then
# = (individual preference last timestep) + (adaption rate)(choice state this timestep) + (learning rate)(choice state last timestep)

# This assumes the choice state is not equal to the collective decision of the community
# If it is the new individual preference is = (preference last timestep) + (adaption rate)(choice this timestep)

# The collective decision of the community is 
# = 1/(number of neighbours)*sum of choice states of neighbours (i.e, it's an average)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation

Choice1   = +1.0
Choice2  = -1.0
vals = (Choice1, Choice2)
mu = 0.1
lamb = 0.0
N = 500

choiceGrid = np.random.choice(vals, N*N, p=(0.5, 0.5)).reshape(N, N)

prefGrid = np.random.choice(vals, N*N, p=(0.5, 0.5)).reshape(N, N)

def sign(z):
	if z > 0:
		return +1.0
	else:
		return -1.0

def update(data):
	global choiceGrid
	global prefGrid
	newChoiceGrid = choiceGrid
	newPrefGrid = prefGrid

	for i in range(N):
		for j in range(N):
			#Note coupling coefficient has been left out here
			sumnei = ((choiceGrid[i, (j-1)%N]) +
					(choiceGrid[i, (j+1)%N]) +
					(choiceGrid[(i-1)%N, j]) +
					(choiceGrid[(i+1)%N, j]))
				
			newChoiceGrid[i, j] = sign(sumnei-prefGrid[i, j])

			Mt = (1.0/4.0)*sumnei
			
			if (choiceGrid[i, j] == Mt):
				newPrefGrid[i, j] = prefGrid[i, j] + mu*newChoiceGrid[i, j]
			else:
 				newPrefGrid[i, j] = prefGrid[i, j] + mu*newChoiceGrid[i, j] + lamb*choiceGrid[i, j]

	mat.set_data(newChoiceGrid)
	choiceGrid = newChoiceGrid
	prefGrid = newPrefGrid
	return [mat]

fig, ax = plt.subplots()
ax.axis('off')
mat = ax.matshow(choiceGrid, cmap=cm.Greens)
ani = animation.FuncAnimation(fig, update, interval=10, save_count=50)
plt.show()