import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--list", action="store_true", help = "Вывод доступных валют")

subparsers = parser.add_subparsers()
parser_a = subparsers.add_parser('get', help='Для получения курса волют')
parser_a.add_argument('--code', help='Укажите код валюты',required=True)
parser_a.add_argument('--date', help='Укажите дату в формает 01/01/2020',required=True)
args = parser.parse_args()
print(args)