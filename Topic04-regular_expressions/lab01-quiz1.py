# this is code for the quiz

import re

regex = ".*"
FILENAME = r"C:\Users\demac\OneDrive\Desktop\pands\PFDA_myWork\Topic04-regular_expressions\\quiz.txt"


with open(FILENAME) as quiz_file:
    for line in quiz_file:
        search_result = re.search(regex, line)
        if (search_result):
            match_line = line
            print(match_line, end="")



# finding regular expressions

regex = r"^Hell?o" # r"hello", r"Hello", r"^Hello", r"^Hell*o", r"^Hell+o
# r"^Hell?o", r"^hello [A-Z]", r"=", r"#", r"[", r"^$"
FILENAME = r"C:\Users\demac\OneDrive\Desktop\pands\PFDA_myWork\Topic04-regular_expressions\\quiz.txt"

# Open the file and search for words matching the regex
with open(FILENAME) as quiz_file: #The opened file is assigned to 
    # the variable quiz_file for use within the block.
    for line in quiz_file:
        # Use re.findall() to find all words that match the pattern
        matches = re.findall(regex, line)
        if matches: #This checks if the matches list is not empty
            for match in matches: #Iterates over the matches list, 
                # where each match found in the line is stored in 
                # the variable match.
                print(match)