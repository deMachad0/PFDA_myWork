# Learning how to combine axis
# Author: Andre 

import matplotlib.pyplot as plt
import numpy as np

num_cols = 3
num_rows = 2

fig, axs = plt.subplots(ncols=num_cols, nrows=num_rows, figsize=(8,4))
for row in range(num_rows):
    for col in range(num_cols):
        axs[row, col].annotate(f"[{row},{col}]", (0.5, 0.5), ha="center")

plt.show()


# using data as matriz

data = [
    [2,4,5,6,3,5,6,7],
    [9,8,7,6,5,4,3,2],
    [1,2,3,4,5,6,7,8],
    [5,5,5,5,5,5,5,5]
]
x = 0.5 + np.arange(8) # x: A sequence of 8 numbers starting at 0.5 and incrementing by 1. It's created using np.arange(8)

num_cols1 = 2
num_rows1 = 2
fig, axs = plt.subplots(ncols=num_cols1, nrows=num_cols1, figsize=(8,4))
count = 0 #count keeps track from data to plot in the current subplot.
for row in range(num_rows1):
    for col in range(num_cols1):
        axs[row,col].plot(x,data[count]) # axs[row,col] This accesses a specific subplot in the grid 
        count += 1

plt.show()