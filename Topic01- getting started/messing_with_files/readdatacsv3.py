# Caculate average age from a csv file
# Author: Andre

import csv

FILENAME = "data.csv"
DATADIR = "../Topic01-representingData/"

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC) #QUOTE_NONNUMERIC TO READ AS FLOAT
    line_count = 0
    total = 0
    for line in reader:
        if not line_count:
            pass
        else:
            total += int(line[1]) # 1 assuming age is in the second column
        line_count += 1
    print(f"Average is {total/ (line_count -1)}") # -1 is to exclude the header row from the count


# Another way 

total_age = 0
count = 0

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp) # reads the first line automatically
    for row in reader:
        if "age" in row: # ensure age column exists
            total_age += int(row["age"])
            count += 1
if count > 0:
    average_age = total_age / count
    print(f"Average age: {average_age}")
else:
    print("no age data available")