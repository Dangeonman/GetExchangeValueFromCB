import os.path
import xmltodict
import urllib.request


URL_EXCHANGE_VAL_LIST = "http://www.cbr.ru/scripts/XML_val.asp?d=0"


path = './list.xml'

def getDictFromUrl(URL):
    file = urllib.request.urlopen(URL)
    data =file.read()
    file.close()
    data =xmltodict.parse(data)
    return data

list_file = os.path.isfile(path)

if list_file == True:
    print("Такой файл существует")
else:
    list_file = open("list.xml", "w", encoding="utf-8")
    list_file.write(str(getDictFromUrl(URL_EXCHANGE_VAL_LIST)))
    print(list_file)

