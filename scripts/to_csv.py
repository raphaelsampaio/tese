import os
for filename in os.listdir("."):
    if not filename.endswith('.csv'): continue
    with open(filename, 'r') as file:
        lines = file.readlines()
    print lines
    with open(filename, 'w') as file:
        for line in lines:
            newary = []
            for el in line.split(';'):
                if ',' in el:
                    newary.append('"' + el + '"')
                else:
                    newary.append(el)
            newline = ','.join(newary) + "\n"
            file.write(newline)
