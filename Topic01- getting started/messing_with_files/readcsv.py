# simple program to read csv file
# Author: Andre

import csv

FILENAME= "data.csv"
DATADIR = "../../../datafiles/"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_ALL)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount:
           print(f"first row {line}\n------")
          # first row
        else: # all subsequent rows
          total += int(line[0])
          print(line)
        linecount += 1