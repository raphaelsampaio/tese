import os
for filename in os.listdir("."):
    if(filename.endswith(".csv")):
        with open(filename, 'r+') as file:
            lines = file.readlines()
        with open(filename, 'w') as file:
            line_number = 1
            for line in lines:
                line_no_spaces = "".join(line.split())
                if len(line_no_spaces) > 0 and line_number > 3:
                    file.write(line_no_spaces + '\n')
                line_number += 1
            
