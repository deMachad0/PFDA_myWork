# Creating a json file 
# Author: Andre 

import json

data = {
    'name': 'Joe',
    'age': 21,
    "student": True
}

file = open("simple.json", 'w') #open a file to writing
json.dump(data,file,indent=4)
jsonString = json.dumps(data)
print(jsonString)
