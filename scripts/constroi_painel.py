import locale
import csv
from datetime import datetime
import os
import json

locale.setlocale(locale.LC_ALL, 'pt_BR')

with open('../dados_fundos.json') as fund_data_json:
    dados_fundos = json.load(fund_data_json)

def escape(string):
    return '"' + string + '"'

def format_number(number):
    return locale.format('%.2f', number)

def write_to_csv(csv, ary):
    csv.writerow(ary)

# data, fundo, cota, greenness
with open('../painel.csv', 'wb') as painel_csv_file:
    painel_csv = csv.writer(painel_csv_file)
    write_to_csv(painel_csv, ['Data', 'Fundo', 'Cota', 'Greenness', 'Propriedades certificadas'])
    for filename in os.listdir('../fiis'):
        if not(filename.endswith('.csv')): continue
        fund = filename.split('.csv')[0]
        
        print fund
        with open('../fiis/' + filename, 'rb') as stock_prices_file:
            csv_file = csv.reader(stock_prices_file)
            row_count = 0
            header = next(csv_file)
            filetype = "other" if header[1].lower() == "cota" else "bmf"
            previous_month = 0
            for row in csv_file:
                date = datetime.strptime(row[0], "%d/%m/%Y").date()
                month = date.month
                year = date.year
                if previous_month == month: continue
                previous_month = month
                
                stock_price = row[4] if filetype == "bmf" else row[1]
                fund_data = {
                    'greenness': 0.0,
                    'properties': 0
                }

                if str(year) in dados_fundos and fund in dados_fundos[str(year)]:
                    fund_data = dados_fundos[str(year)][fund]

                write_to_csv(painel_csv, [
                    date, 
                    fund, 
                    stock_price, 
                    format_number(fund_data['greenness']),
                    fund_data['properties']
                ])
            
