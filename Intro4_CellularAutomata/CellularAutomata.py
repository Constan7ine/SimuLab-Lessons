import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Size of board NxN
N    = 100

ON   = 255
OFF  = 0
vals = (ON, OFF)

def init(n=N, randrow=False):
    grid = np.zeros(shape=(n,n))
    grid[0,n//2] = ON
    return grid

def update(d):
    global row
    data = grid[row]
    row += 1
    # We need to stop at the end of the board
    if row >= N: return

    # This will convert the neighbour states into a decimal number we can use as an index in the rules
    # 1 in third row of binary number is 4, also mod N to wrap the edge (LEFT NEIGHBOUR)
    # 1 in second row of binary number is 2, (CENTER NEIGHBOUR)
    # 1 in first row of binary number is just 1 (RIGHT NEIGHBOUR)
    def GetRuleIndex(i):
        return int(4*data[(i-1) % N]/ON + 2*data[i]/ON +  1*data[(i+1) % N]/ON)

    # Make a new row, we get the rule index from the three neighbours, and use it to get the state of each element
    grid[row] = np.array( [int(rule[GetRuleIndex(i)]) * 255 for i in range(N) ])

    mat.set_data(grid)
    return mat


# Interesting rules 90, 30, 54, 60, 150, 62
rulenum=62
fig, ax = plt.subplots()
ax.axis('off')
row = 0
grid = init()

# This converts the rule code into a list of 0 and 1 binary digits
# The format meants {firstFormatElement:PaddingWidthof8Binary}
# We also reverse it
rule = list('{0:08b}'.format(rulenum))
rule.reverse()

mat = ax.matshow(grid, cmap=cm.Greens)

# The update function defined here will be called each interval, updating the grif data held in mat
ani = animation.FuncAnimation(fig, update, frames=99, interval=60, save_count=50, repeat=False)
plt.show()
