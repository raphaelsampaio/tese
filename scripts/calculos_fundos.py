import os
import csv

funds_greenness = {}

with open("../portfolios.csv", 'rb') as portfolios_file:
    portfolios_csv = csv.reader(portfolios_file)
    next(portfolios_csv, None) # ignore header
    for row in portfolios_csv:
        year = row[0]
        fund = row[1]
        prop_id = row[2]
        greenness = row[4]

        if year not in funds_greenness:
            funds_greenness[year] = {}
        if fund not in funds_greenness[year]:
            funds_greenness[year][fund] = {}
        if "greenness" not in funds_greenness[year][fund]:
            funds_greenness[year][fund]['greenness'] = 0.0
        if "properties" not in funds_greenness[year][fund]:
            funds_greenness[year][fund]['properties'] = 0
        
        funds_greenness[year][fund]['properties'] = funds_greenness[year][fund]['properties'] + 1

        funds_greenness[year][fund]['greenness'] = funds_greenness[year][fund]['greenness'] + float(greenness)

        if funds_greenness[year][fund]['greenness'] == 0:
            del(funds_greenness[year][fund])

    
print funds_greenness

