from datetime import datetime
from datetime import timedelta
import time

pomodoro=timedelta(minutes=2)

endtime=datetime.now()+pomodoro

print(endtime)
while endtime > datetime.now():
    print("Tik Tok",datetime.now())
    time.sleep(20)

print(pomodoro)
print(endtime)