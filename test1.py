import xmltodict
import urllib.request

URL_EXCHANGE_VAL_LIST = "http://www.cbr.ru/scripts/XML_val.asp?d=0"


def getDictFromUrl(URL):
    file = urllib.request.urlopen(URL)
    data =file.read()
    file.close()
    data =xmltodict.parse(data)
    return data

print(getDictFromUrl(URL_EXCHANGE_VAL_LIST))