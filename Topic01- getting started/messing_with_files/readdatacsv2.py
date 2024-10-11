# read csv file dealing with header line separately
# Author: Andre

import csv

FILENAME = "data.csv"
DATADIR = "../Topic01-representingData/"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_ALL)
    line_count = 0
    total = 0
    for line in reader:
        if not line_count:
            print(f"{line}\n----------")
        else:
            total =+ int(line[0])
            print(line)
        line_count += 1
