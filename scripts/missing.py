# -*- coding: utf-8 -*-
import os
import json
def print_collection(collection):
    print ", ".join(sorted(collection))
def load_json_into_set(json_file):
    with open(json_file) as file:
        return set(json.load(file))
expected_cnpjs = load_json_into_set("cnpjs_esperados.json")
print "É esperado que tenhamos cotações de %s fundos." % len(expected_cnpjs)
actual_cnpjs = set([filename.split(".csv")[0] for filename in os.listdir(".") if (filename.endswith(".csv") and filename != "IFIX.csv")])
print "Temos cotações de %s fundos." % len(actual_cnpjs)
not_found = expected_cnpjs - actual_cnpjs
if len(not_found) > 0:
    with open("ticker_cnpj.json") as ticker_cnpj_file:
        ticker_cnpj = json.load(ticker_cnpj_file)
        for ticker, cnpj in ticker_cnpj.items():
            for cnpj_nf in not_found:
                if cnpj_nf == cnpj:
                    not_found.add(ticker)
                    not_found.remove(cnpj)
    print "Não temos cotações de %s fundos: " % len(not_found)
    print_collection(not_found)
print ""
green_funds = load_json_into_set("fundos_verdes.json")
green_funds_no_data = not_found & green_funds
if len(green_funds_no_data) > 0:
    print "Os seguintes fundos são verdes e não têm cotações: "
    print_collection(green_funds_no_data)
not_expected = actual_cnpjs - expected_cnpjs
if len(not_expected) > 0:
    print "Cotações dos seguintes fundos foram encontradas, mas não eram esperadas: "
    print_collection(not_expected)
