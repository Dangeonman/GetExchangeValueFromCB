from datetime import datetime, timedelta
from tqdm.auto import tqdm
import subprocess

# Исходная дата
start_date_str = "1991/01/01"
start_date = datetime.strptime(start_date_str, '%Y/%m/%d')

# Текущая дата
current_date = datetime.now()

# Количество дней между текущей датой и исходной датой
total_days = (current_date - start_date).days

# Итерация по каждому дню от исходной даты до текущей даты
for day in tqdm(range(total_days)):
    # Вычисление даты для текущей итерации
    current_iteration_date = start_date + timedelta(days=day)
    
    # Аргументы, для передачи в exchange.py
    # todo Надо убрать хардкор и вынести в аргументы как способ указания кода валюты
    args = ['get', f'--date={current_iteration_date.strftime("%d/%m/%Y")}', '--code=R01235']

    # Запуск exchange.py с аргументами, подавляя вывод в stdout
    subprocess.run(['python', 'exchange.py'] + args, stdout=subprocess.DEVNULL)
