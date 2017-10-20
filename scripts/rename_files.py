import os
import re
import json
ECONOMATICA_CODE_REGEX = "Economatica-(.*).txt"
with open("economatica_code_cnpj.json") as data_file:    
    ECONO_CNPJ_DICT = json.load(data_file)
    
for file in os.listdir("."):
    # print file
    file_found = re.search(ECONOMATICA_CODE_REGEX, file)
    if not file_found: continue
    economatica_code = file_found.group(1)
    cnpj = ECONO_CNPJ_DICT[economatica_code]
    if len(cnpj) > 0:
        print "renaming %s to %s.csv" % (file, cnpj)
        os.rename(file, "%s.csv" % cnpj)
    