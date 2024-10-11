# reading in the csv as a pandas table
# Author: Andre


FILENAME = "data.csv"
DATADIR = "../../../datafiles/"

import pandas 

df = pandas.read_csv(DATADIR + FILENAME)
print(df)
