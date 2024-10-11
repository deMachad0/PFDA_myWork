# reading a data.csv file
# Author: Andre

import csv


FILENAME = "data.csv"
DATADIR = "../Topic01-representingData/"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_ALL)
    for line in reader:
      print(line)