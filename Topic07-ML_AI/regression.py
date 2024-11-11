# Learning regression using seaborn
# Author: Andre

import seaborn as sns
import matplotlib.pyplot as plt

#  load the dataset
dataset = sns.load_dataset('tips')
# the first five entries of the dataset
print(dataset.head())
sns.set_style('whitegrid')
# Plotting the graph but without the line 
#sns.scatterplot(x='total_bill', y='tip', data=dataset)
sns.lmplot(x='total_bill', y='tip', order=1, data=dataset) # order=1 means a straight line, order=3 means a curvy line
plt.show()

# load the dataset of 'flights'
dataset1 = sns.load_dataset('flights')
print(dataset1.head())
# plotting it with dark style
sns.set_style('dark')
sns.lmplot(x='passengers', y='year', order=3, data=dataset1)
plt.show()