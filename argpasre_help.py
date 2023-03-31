import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--list", help="Для получения списка курса волют")
parser.add_argument("--data", help="Укажите дату в формате 01/01/2020")
parser.add_argument("--code", help="Укажите код валюты для получения")
args = parser.parse_args()
if args.code:
    print(args.code)


