import os.path
import xmltodict
import urllib.request
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--list", action="store_true", help = "Вывод доступных валют")

URL_EXCHANGE_VAL_LIST = "http://www.cbr.ru/scripts/XML_val.asp?d=0"



file = urllib.request.urlopen(URL_EXCHANGE_VAL_LIST)
data =file.read()
file.close()
    
with open("list.xml", "w", encoding="utf-8") as out:
    out.write(str(data))

def Name_Valuta():
    data =open("list.xml", "r", encoding="utf-8")
    new_data = data['Valuta']['Item']
    try:
        for i in new_data:
            print("Валюта:", i['Name'], "Код:", i['@ID'])
    except:
        str1 = "Ошибка"
        print(str1)
        quit(-1)

argument = parser.parse_args()

if argument.list:
    Name_Valuta()
else:
    print("Неизвестная команда")




