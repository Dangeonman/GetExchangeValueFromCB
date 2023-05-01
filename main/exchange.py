import urllib.request
import xmltodict
import datetime
import argparse
import os.path

parser = argparse.ArgumentParser()

parser.add_argument("--list", action="store_true", help = "Вывод доступных валют")
subparsers = parser.add_subparsers()
parser_a = subparsers.add_parser('get', help='Для получения курса волют')
parser_a.add_argument('--code', help='Укажите код валюты',required=True)
parser_a.add_argument('--date', help='Укажите дату в формает 01/01/2020',required=True)

URL_EXCHANGE_DATE = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=%s"
URL_EXCHANGE_VAL_LIST = "http://www.cbr.ru/scripts/XML_val.asp?d=0"

def getDictFromUrl(URL):
    file = urllib.request.urlopen(URL)
    contentBody =file.read()
    file.close()
    return contentBody

def handlerGetContent(data):
    file_name = "./archive/%s.dt" % (data.strftime("%Y%m%d"))
    dir_name = "./archive"
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    if os.path.isfile(file_name):
        f = open(file_name, "r")
        contentBody = f.read()
        f.close()
        contentXml =xmltodict.parse(contentBody)
        return contentXml
    else:
        contentBody = getDictFromUrl(URL_EXCHANGE_DATE % (argument.date)) 
        contentXml =xmltodict.parse(contentBody)
        if "ValCurse" in contentXml:
            return False
        f_new = open(file_name, "wb")
        f_new.write(contentBody)
        f_new.close()
        return contentXml



def kyrs():
    if len(argument.code) == 6:
        ID = argument.code
    else:
        print("Не верно введен код валюты")
    DF = "%d/%m/%Y"
    
    try:
        dt = datetime.datetime.strptime(argument.date, DF)
    except:
        str1 = "Формат введёной даты не соответствует необходимому формату %s" % (DF)   
        print(str1)
        quit(-1) 
    
    dt_now = datetime.datetime.today()
    if dt_now < dt:
        print("Время еще не пришло")
        return
    contentXml = handlerGetContent(dt) 
    if not contentXml:
        print("Ошибка парсинга")
        return
    echostr="Код %s валюты заданна не верно" % (ID)
   
    
    for i in contentXml['ValCurs']['Valute']: 
        if i['@ID'] != ID:
            continue
        echostr = "Курс %s" % (i["Name"]) + " к рублю %s" % (i["Value"])
        break
            
    print(echostr)

def Name_Valuta():
    data =getDictFromUrl(URL_EXCHANGE_VAL_LIST)
    contentXml =xmltodict.parse(data)
    new_data = contentXml['Valuta']['Item']
    try:
        for i in new_data:
            print("Валюта:", i['Name'], "Код:", i['@ID'])
    except:
        str1 = "Ошибка"
        print(str1)
        quit(-1)

argument = parser.parse_args()


try:
    if argument.list:
        Name_Valuta()
    elif argument.code and argument.date:
        kyrs()
except:
    str0 = "Неверно введены данные"
    print(str0)

