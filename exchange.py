import requests
import urllib.request
import xmltodict
import sys
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--list", action="store_true", help = "Вывод доступных валют")
parser.add_argument("--data", help = "Укажите дату в формате 01/01/2001")
parser.add_argument("--code", help = "Введите код нужной валюты")

URL_EXCHANGE_DATE = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=%s"
URL_EXCHANGE_VAL_LIST = "http://www.cbr.ru/scripts/XML_val.asp?d=0"

def getDictFromUrl(URL):
    file = urllib.request.urlopen(URL)
    data =file.read()
    file.close()
    data =xmltodict.parse(data)
    return data

def kyrs():
    ID = argument.code
    DF =  "%d/%m/%Y"
    DD = "01/01/2020"

    if len(sys.argv) > 1:
        try:
            dt = datetime.datetime.strptime(argument.data, DF)
        except:
            str1 = "Формат введёной даты не соответствует необходимому формату %s" % (DF)   
            print(str1)
            quit(-1) 
        DD= argument.data
    data1 = getDictFromUrl(URL_EXCHANGE_DATE % (DD)) 

    for i in data1['ValCurs']['Valute']: 
        if i['@ID'] != ID:
            continue
        echostr = "Курс валюты к рублю %s" % (i["Value"])
        print(echostr)

def Name_Valuta():
    data =getDictFromUrl(URL_EXCHANGE_VAL_LIST)
    new_data = data['Valuta']['Item']
    if len(sys.argv) > 1:
        try:
            for i in new_data:
                print("Валюта:", i['Name'], "ID:", i['@ID'])
        except:
            str1 = "Ошибка"
            print(str1)
            quit(-1)

argument = parser.parse_args()

if argument.list:
    Name_Valuta()
elif argument.data:
    kyrs()
elif argument.code:
    ID = argument.code
    kyrs()