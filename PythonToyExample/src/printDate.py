import time 
import datetime

while True:
    d_date = datetime.datetime.now()
    reg_format_date = d_date.strftime("%Y-%m-%d %I:%M:%S %p")
    print(reg_format_date)
    time.sleep(5)
