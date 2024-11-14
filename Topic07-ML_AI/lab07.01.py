# Knock Weather lab checking correlation
# Author: Andre

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Reading data
data = "https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv"
df = pd.read_csv(data, skiprows=19)
print(df.head())

# Checking correlation between the mean temperature and the month
corrtemp = df['month'].corr(df['meant'])
print(corrtemp)

# Plotting it
sns.lmplot(x='month',y='meant',data=df, order=3)
plt.title("Correlation between Monht and Mean Temperature")
plt.show()

# Cleaning some missing data from month and windspeed
cleandf = df[['month', 'wdsp']]
# Dropping NAs
cleandf.dropna(inplace=True)

# Trying again to drop 
cleandf['wdsp']= cleandf.loc[:, 'wdsp'].replace(' ', np.nan)
cleandf.dropna(inplace=True)

# Converting windspeed to float
#cleandf['wdsp'] = pd.to_numeric(cleandf['wdsp'], errors='coerce')
cleandf['wdsp']= cleandf['wdsp'].astype(float)

# Cheking correlation 
corrwind = cleandf['month'].corr(df['wdsp'])
print(f'wind correlation {corrwind}')

# Plotting it again
sns.set_style("whitegrid")
sns.lmplot(x='month', y='wdsp', data=cleandf, order=3)
plt.show()