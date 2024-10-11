# reading json file 
# Author: Andre 

import json

DATADIR = "C:/Users/demac/OneDrive/Desktop/pands/programming-for-data-analytics/My-work/datafiles/"
FILENAME = "data.json"

with open(DATADIR + FILENAME, "rt") as fp:
    json_object = json.load(fp)
for employee in json_object['employees']:
    print(employee)