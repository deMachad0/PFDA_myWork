# Generating data and using poisson distribution
# Author: Andre

import pandas as pd
import numpy as np

# Data range 
data = pd.date_range(start='1/1/2018', end='1/08/2018')
print(data)

# Use the formatt year first
data2 = pd.date_range(start='2023-01-01', end='2023-01-04')
print(data2)

# Use freq to find hourly data
data3 = pd.date_range(start='2023-01-01', end='2023-01-04', freq='H') # freq'H' represents hour
print(data3)

# Generate random data
rng = np.random.default_rng()
print(rng)

# Creating a dataframe where data = a random number from our data3
df = pd.DataFrame(index= data3, data = rng.random(len(data3)), columns=["admissions"])
print(df.head(3))

# The data above does not look a proper data, so lets do using poisson
mean_admissions = 15

df = pd.DataFrame(index=data3, data = rng.poisson(lam=mean_admissions, size= len(data3)), columns=['admissions'])
print(df.head(3))

import seaborn as sns
import matplotlib.pyplot as plt

# plot it
sns.lineplot(data=df, x=df.index, y='admissions')
plt.show()

# Checking the mean()
mean_distrib = df['admissions'].mean()
print(mean_distrib)

# This does not take into account the time of the day
# pass in an array into lam to reflect changing averages through out the day
x = np.linspace(-np.pi, np.pi, 24)
means = np.sin(x) +15
plt.plot(x, means)
plt.show()

number_ofdays = len(data3)/24
multiplier = (number_ofdays * 2) * -1
x = x = np.linspace(-np.pi, multiplier*np.pi, len(data3))
admissions_means = (np.sin(x) * (mean_admissions/2)) + mean_admissions
plt.plot(x, admissions_means)
plt.show()

df = pd.DataFrame(index = data3, data = rng.poisson(lam=admissions_means, size=len(data3)), columns=['admissions'])
print(df.head(3))

sns.lineplot(data=df,x = df.index, y='admissions')
plt.show()