# messing with regex while using csv file
# Author: Andre

import pandas as pd
import os

DATADIR = r"C:\Users\demac\OneDrive\Desktop\pands\PFDA_myWork\Topic04-regular_expressions"
people_filename= os.path.join(DATADIR, "people-100.csv")

people_df = pd.read_csv(people_filename)
print(people_df.head(3))

people_df['domain'] = people_df['Email'].str.split('@').str[1]
print(people_df.head(3))

# removing domain column
people_df.drop('domain', axis=1, inplace=True)
print(people_df.head(3))

# using regex to get domain column back
pattern = r".*@"
people_df['domain'] = people_df['Email'].str.replace(pattern, '', regex=True)
print(people_df.head(3))

# a more precise pattern
pattern = r".*@([\w\.]+\.\w{2,3})"
people_df['domain'] = people_df['Email'].str.replace(pattern, '\\1', regex=True)
print(people_df.head(3))

# moving the extension (x78776) out from the phone numbers 
the_extension_pattern = r"x\d*"
people_df['clean_phone'] = people_df['Phone'].str.replace(the_extension_pattern, '', regex=True)
print(people_df.head(3))

# moving the hyphens and dots out from the numbers
othercharts_pattern = r"[\-\. \(\)]*"
people_df['clean_phone'] = people_df['clean_phone'].str.replace(othercharts_pattern, '', regex=True)
print(people_df.head(3))

# moving the international numbers (001) out from the numbers
prefix_pattern = r"^([^\+0].*)"
people_df['clean_phone'] = people_df['clean_phone'].str.replace(prefix_pattern, '+1\\1', regex=True)
print(people_df.head(3))

# replacing the 00s at the start with +
prefix_pattern = r"^00(.*)"
people_df['clean_phone'] = people_df['clean_phone'].str.replace(prefix_pattern, '+\\1', regex=True)
print(people_df.head(3))

# copy any extension to another column / the problem : it will return the whole number
# if there is no extension
extension_pattern = r"^.*x"
people_df['extension'] = people_df['Phone'].str.replace(extension_pattern, '', regex=True)
print(people_df.head(3))

# extract the extension str.extract(pattern)
extension_pattern = r"x(\d+)"
people_df['extension'] = people_df['Phone'].str.extract(extension_pattern)
print(people_df.head(3))

# to filter rows on a regular expression
people_df[people_df['Phone'].str.contains(r'^\+|^00')]
print(people_df.head(3))