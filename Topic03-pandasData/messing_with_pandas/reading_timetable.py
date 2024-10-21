#  Reading tsv file and csv together, manipulating them
# Author: Andre

import os
import pandas as pd
import matplotlib.pyplot as plt

DATADIR = r"C:\Users\demac\OneDrive\Desktop\pands\PFDA-mywork\PFDA -mywork\datafiles\lectures\topic03-pandas\messingwithPandas"
people_filename = os.path.join(DATADIR, "people-100.csv")
timetable_filename = os.path.join(DATADIR, "timetableData.tsv")


df = pd.read_csv(timetable_filename, sep="\t")
#df = pd.read_csv("https://1drv.ms/x/c/1d834ab2ce84e171/EU8ZiW-b5DpIvgrRmQ0ktcwBt_F_d3Ssl00jvL5XINo3Vg?e=QEeeBa")
                    
print(df.head(3))

print(df.iloc[40:50]) # returns rows 40 to 50
print(df.loc[42:44]) # returns only 42 and 44
print(df.loc[42:44,'Staff (delimited)']) # only return the staff column

print(df[df['Staff (delimited)'].str.contains('/')]) # returns the rows which have multiple staff
#cleandf = df.fillna(value=' ') # fill out all the columns that contains blank space ' '
#cleandf[cleandf['Staff (delimited)'].str.contains('/')]

# how to remove columns
df.drop([1,3])
df.head(4)
df.drop([1,3] , axis=0, inplace=True)
df = df.drop([1,3])
print(df.head(4))

# Make a new column
df['total_hours'] = df['Duration'] * df['Number of weeks']
print(df.head(3))

# reading another file
people_df = pd.read_csv(people_filename)
print(people_df.head(3))

# to get the email domains
people_df['domain'] = people_df['Email'].str.split('@').str[1]
print(people_df.head(3))

# 
email_employees = df['Email'].value_counts()

# a pie chart for email domain
plt.figure(figsize=(8, 8))
plt.pie('Email', labels=email_employees.index, autopct='%1.1f%%', startangle=140)

# Ensure that pie chart is circular
plt.axis('equal')

plt.title('Email of Employess')
plt.show()