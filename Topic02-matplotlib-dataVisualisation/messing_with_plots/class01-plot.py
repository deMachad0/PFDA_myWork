# Learning plots again
# Author: Andre

import matplotlib.pyplot as plt

x = [0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5]
y = [4.8,5.5,3.5,4.6,6.5,6.6,2.6,3.0]

fig,ax = plt.subplots()

ax.bar(x,y)

plt.show()