# knock airport weather, checking regression
# Author: Andre

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Loading and printing a dataset
df = sns.load_dataset('tips')
print(df.head())

# Modify the script to produce a regression plot for the tips against the total bill
sns.set_style('darkgrid')
sns.lmplot(x='total_bill', y='tip', data=df, order=1)
plt.show()
sns.set_style('ticks')
sns.lmplot(x='total_bill', y='tip', data=df, order=3)
plt.show()

# Making a plot using tips agains size
sns.set_style('white')
sns.lmplot(x='size', y='tip', data=df)
plt.title('Size - Tips ')
# Using jitter to make it easier to see
sns.lmplot(x='size', y='tip', data=df, x_jitter=.05)
plt.title('Size - Tips (x_jitter)')
# Instead of dots, use an estimator to estimate the mean tip for each size
sns.lmplot(x='size', y='tip', data=df, x_estimator=np.mean)
plt.title('Size - Tips (estimator=)')
plt.show()