# anonymise the sub domains of ip addresses
# Author: Andre

import re

regex = "(\d{1,3}\.\d{1,3}\.)\d{1,3}\.\d{1,3}"

replacement_text = "\\1XXX.XXX " # there is a space at the end to match above
FILENAME = "smallerAccess.log"
OUTPUT_FILENAME = "anonymisedIPs.txt"

with open(FILENAME) as input_file:
    with open(OUTPUT_FILENAME, "w") as output_file:
        for line in input_file:
            # re.search() finding the IPs and printing them 
            found_text = re.search(regex, line).group()
            print(found_text)
            new_line = re.sub(regex, replacement_text, line)
            output_file.write(new_line)