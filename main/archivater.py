from datetime import datetime, timedelta
from tqdm.auto import tqdm
import time
import subprocess

a = "1991/01/01"
dt = datetime.strptime(a, '%Y/%m/%d')
date_now = datetime.now()
days = (datetime.now() - dt).days
for i in tqdm(range(days)): 
    #time.sleep(3 / 1000)
    data = dt + timedelta(days=i)
    str = "C:/Users/vasa2/AppData/Local/Programs/Python/Python311/python.exe c:/Users/vasa2/MyProject/main/exchange.py get --date=%s --code=R01235" % (data.strftime("%d/%m/%Y"))
    a1=subprocess.run([
        "C:/Users/vasa2/AppData/Local/Programs/Python/Python311/python.exe",
        "c:/Users/vasa2/MyProject/main/exchange.py",
        "get",
        "--date="+data.strftime("%d/%m/%Y"),
        "--code=R01235"], 
        stdout=subprocess.DEVNULL)
    

