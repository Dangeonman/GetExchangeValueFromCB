import requests
import urllib.request
import xmltodict
import sys
import datetime
import argparse

URL_EXCHANGE_VAL_LIST = "http://www.cbr.ru/scripts/XML_val.asp?d=0"

def getDictFromUrl(URL):
    file = urllib.request.urlopen(URL)
    data =file.read()
    file.close()
    data =xmltodict.parse(data)
    return data

def Name_Valuta():
    data =getDictFromUrl(URL_EXCHANGE_VAL_LIST)
    new_data = data['Valuta']['Item']
    if len(sys.argv) >= 1:
        try:
            for i in new_data:
                print("Валюта:", i['Name'], "ID:", i['@ID'])
        except:
            str1 = "Ошибка"
            print(str1)
            quit(-1)
param_name = sys.argv[1]
if param_name == "list":
    Name_Valuta()