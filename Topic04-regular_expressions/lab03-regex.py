# using regular expressions 
# Author: Andre

import re

regex = r"\[.*\]"
FILENAME = "smallerAccess.log"

with open(FILENAME) as input_file:
    for line in input_file:
        found_text_list = re.findall(regex, line)
        if (len(found_text_list) != 0):
            found_text = found_text_list[0]
            found_month = re.search(r"Feb", found_text)
            found_dots = re.sub(r"11", "=", found_text)
            print(found_dots)
            print(found_month)
            print(found_text)
            print(found_text[1:-1])
