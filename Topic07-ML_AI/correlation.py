# Learning correlation 
# Author: Andre

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# creating an array from 10 to 19
x = np.arange(10,20)
print(x)
# Creating an array manually
y = np.array([2,1,4,5,6,12,18,25,96,48])
print(y)
# Checking the correlation between them
r = np.corrcoef(x,y)[0,1]
print(r)
# plotting it 
plt.scatter(x,y)
plt.title('Correlation between arrays')
plt.xlabel('X values')
plt.ylabel("Y values")
plt.text(10.5, max(y)-10, f'Correlation coefficient (r): {r:.2f}', fontsize=12, color='blue')
plt.show()