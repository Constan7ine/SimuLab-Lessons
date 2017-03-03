import numpy as np
import matplotlib.pyplot as plt

# Note: Columns represent Alice. Positive Numbers are a win for Alice, negative numbers are a win for Bob
# If you transpose the matrix then positive and negative are flipped and columns represent Bob
M = [[1, 1],
     [-1, 1]]

a = float(M[0][0])
b = float(M[0][1])
c = float(M[1][0])
d = float(M[1][1])

PayoffsForAStrat1 = [a*p + c*(1-p) for p in np.arange(0, 1, 0.01)]
PayoffsForAStrat2 = [b*p + d*(1-p) for p in np.arange(0, 1, 0.01)]

OptimalStratForA = (d-c)/(a+d-b-c)
PayOff = (a*d-b*c)/(a+d-b-c)

OptimalStratForB = (d-b)/(a+d-b-c)

print("Alice should play strategy 1 {0}% of the time and win {1} points".format(OptimalStratForA*100, PayOff))
print("Bob should play strategy 1 {0}% of the time and lose of {1} points".format(OptimalStratForB*100, PayOff))

plt.plot(np.arange(0, 1, 0.01), PayoffsForAStrat1, np.arange(0, 1, 0.01), PayoffsForAStrat2)
plt.show()