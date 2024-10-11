# learning Numpy again and using it to create a range of numbers
# Author: Andre

import matplotlib.pyplot as plt
import numpy as np

x = 0.5 + np.arange(8) # arrange(8) creates a range of 8 numbers
y = [1,3,5,8,3,6,4,6]
z = [3,5.6,9.4,9.1,4.6,7.7,8.1,9]

fig,ax = plt.subplots()

# Some types of plots
ax.bar(x,y) 
ax.plot(x,y) 
ax.scatter(x,y)
ax.fill_between(x,y,z)
ax.stackplot(x,y,z)
ax.stairs(y)
ax.stem(x,y)

# Setting names for the title and axis X and Y
ax.set(xlabel="x axls label", ylabel="y", title="Hey mom")

# another way to set names
ax.set_title("Yo mom")
ax.set_xlabel("X here")
ax.set_ylabel("Y here")

# the function that will do the formatting
def currency_formatting(x,pos): # pos is for position
    s = f"£{x}M"
    return s

ax.xaxis.set_major_formatter(currency_formatting)

ax.text(1, 8, "text to add", fontsize=10, verticalalignment="center") # 1 and 8 is for the numbers of the axis, text to be added, and position "center"

labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment="right")

# do an annotation to the plot and point to it
ax.annotate('max', (3, 8), xytext=(1, 9), arrowprops=dict(facecolor="black", shrink=0.05))
# xy text is where the arrow will be pointed

plt.show()