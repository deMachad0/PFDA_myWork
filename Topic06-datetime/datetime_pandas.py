# Messing with datetime using pands
# Author: Andre

import pandas as pd
# Getting data
df = pd.read_csv("co2-mm-mlo.csv")
print(df.head(3))

# Reading just 2 columns (Date, Interpolated)
fields = ['Date', 'Interpolated']
df = pd.read_csv("co2-mm-mlo.csv", usecols= fields)
print(df.head(3))

# Changing the name of columns and order to be printed out, also creating an index using skiprows=1
names = ['Date', 'DD', 'Ave', 'Interpolated', 'Trend', 'Num Days', 'extra']
df = pd.read_csv("co2-mm-mlo.csv", header=None, names = names, skiprows=1)
print(df.head(3))
print()
print(df['Date'])

# Change the dtype= object to regular date
df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'])

# Plot it using seaborn
import seaborn as sns

sns.lineplot(data=df, x='Date', y='Ave')
sns.lineplot(data=df, x='Date', y='Interpolated')

import matplotlib.pyplot as plt
plt.show()

# Manipulating another csv files, but having some problems because of columns
# there a couple of the rows that should be skip
#df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv")
#print(df.head(3))
# Solving the empty columns from file above using skiprows=19
df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv", skiprows=19)
print(df.head(3))

# Changing the format to a datetime, not worked, missing day
#pd.to_datetime(df[['year', 'month']])

# Creating a column for day
df['day'] = 1
print(df.head(3))

# Changing the format to a datetime again
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
df['date']

# plotting it
sns.lineplot(data=df, x='date', y="meant")
plt.show()

# Setting the index to the datetime
# do dome analysis on the data based on time 
df.set_index('date', inplace=True)
print(df.head(3))
sns.lineplot(data=df, x='date', y='meant')
plt.show()

# look at one year
# loc gets the tols that match the indexes value
dateFrom = "2010-01-01 01:00:00"
dateTo = "2011-01-01 01:00:00"
sns.lineplot(data=df.loc[dateFrom:dateTo], x='date', y='meant')
plt.show()
#iloc uses the row or column number
sns.lineplot(data=df.iloc[36:48], x='date', y='meant')
plt.show()

#Get the mean temperature of the total
dateFrom = "2010-01-01 01:00:00"
dateTo = "2011-01-01 01:00:00"
anual_temperature = df.loc[dateFrom:dateTo]['meant'].mean()
print(f"Anual temperature {anual_temperature}")

# Get the mean temperature of each year
anual_mean_temperature = df['meant'].resample('1YE').mean()
sns.lineplot(data=anual_mean_temperature)
plt.show()

# Aggregation
# agg() instead of doing mean(), you can do multiple operations
print(df.head(3))
rs = df.resample("1YE")
print(rs.mean())
rs_mean = rs['meant'].agg(["mean", "std"])
print(rs_mean)