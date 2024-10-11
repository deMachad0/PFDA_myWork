# read csv file as a dict
# Author: Andre

import csv

FILENAME= "data.csv"
DATADIR = "../../../datafiles/"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_ALL)
    total = 0
    for line in reader:
        total += int(line['id'])
        print(line)
