import urllib.request
import xmltodict
import datetime
import argparse
import os

# Настройка парсера аргументов командной строки
parser = argparse.ArgumentParser()

parser.add_argument("--list", action="store_true", help="Вывод доступных валют")
subparsers = parser.add_subparsers()

# Подпарсер для получения курса валют
parser_get = subparsers.add_parser('get', help='Для получения курса валют')
parser_get.add_argument('--code', help='Укажите код валюты', required=True)
parser_get.add_argument('--date', help='Укажите дату в формате 01/01/2020', required=True)

URL_EXCHANGE_BY_DATE = "http://www.cbr.ru/scripts/XML_daily.asp?date_req=%s"
URL_EXCHANGE_VAL_LIST = "http://www.cbr.ru/scripts/XML_val.asp?d=0"

def get_dict_from_url(url):
    """Получить словарь из URL."""
    response = urllib.request.urlopen(url)
    content = response.read()
    response.close()
    return content

def get_content_by_date(date):
    """Получить и кэшировать контент по дате."""
    file_name = "./archive/%s.dt" % (date.strftime("%Y%m%d"))
    dir_name = "./archive"
    
    # Создаем директорию, если она не существует
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    # Читаем из файла, если он существует
    if os.path.isfile(file_name):
        with open(file_name, "r") as file:
            content = file.read()
        content_xml = xmltodict.parse(content)
        return content_xml
    else:
        content = get_dict_from_url(URL_EXCHANGE_BY_DATE % (args.date)) 
        content_xml = xmltodict.parse(content)
        if "ValCurs" not in content_xml:
            return False
        
        with open(file_name, "wb") as file:
            file.write(content)
        return content_xml

def get_exchange_rate():
    """Получить курс валюты."""
    currency_code = args.code
    
    # Проверка длины кода валюты
    if len(currency_code) != 6:
        print("Неверно введен код валюты")
        return
    
    date_format = "%d/%m/%Y"
    
    try:
        date = datetime.datetime.strptime(args.date, date_format)
    except ValueError:
        print(f"Формат введённой даты не соответствует необходимому формату {date_format}")
        return
    
    current_date = datetime.datetime.today()
    if current_date < date:
        print("Время еще не пришло")
        return
    
    content_xml = get_content_by_date(date)
    if not content_xml:
        print("Ошибка парсинга")
        return
    
    exchange_rate_message = f"Код {currency_code} валюты задан неверно"
    
    for currency in content_xml['ValCurs']['Valute']: 
        if currency['@ID'] != currency_code:
            continue
        exchange_rate_message = f"Курс {currency['Name']} к рублю {currency['Value']}"
        break
            
    print(exchange_rate_message)

def list_currencies():
    """Вывести список доступных валют."""
    data = get_dict_from_url(URL_EXCHANGE_VAL_LIST)
    content_xml = xmltodict.parse(data)
    currencies = content_xml['Valuta']['Item']
    
    try:
        for currency in currencies:
            print("Валюта:", currency['Name'], "Код:", currency['@ID'])
    except KeyError:
        print("Ошибка")
        return

args = parser.parse_args()

try:
    if args.list:
        list_currencies()
    elif args.code and args.date:
        get_exchange_rate()
except Exception as e:
    print(f"Неверно введены данные: {e}")
