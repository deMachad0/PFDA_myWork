# Larning how to read files using Pandas
# Author: Andre

import pandas as pd
import os

# r to read raw string
DATADIR = r"C:\Users\demac\OneDrive\Desktop\pands\PFDA-mywork\PFDA -mywork\datafiles\lectures\topic03-pandas\messingwithPandas"
FILENAME = "people-100.csv"

# combine directory and file using os.path.join
file_path = os.path.join(DATADIR, FILENAME)

df = pd.read_csv(file_path)


df.head()

# using parse_dates=['date'] to manipulate Period to be read as Data
df = pd.read_csv(file_path, parse_dates=['Date of birth'])
df.info() # show the information of the data

# Limiting data to be read
names_of_columns=['Index','User Id','First Name','Last Name','Sex','Email','Phone','Date of birth','Job Title']
df = pd.read_csv(file_path, usecols=names_of_columns)
df.head(3) # to read only 3 columns
df.info()

# How to deal with columns and header 
df = pd.read_csv(file_path, header=None, index_col=0)
df.head(3)
df.info()

# Naming the columns
names = ['Index','User Id','First Name','Last Name','Sex','Email','Phone','DOB','Job Title']
df = pd.read_csv(file_path, header=None, index_col=0, names=names, parse_dates=['DOB'])
df.head(3)
df.info()

# Also can be read from website/cloud
#df = pd.read_csv("https://extendsclass.com/csv-generator.html")
#df.head(3)