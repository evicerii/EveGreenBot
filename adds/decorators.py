import time
from numpy import *
from functools import wraps
import datetime
import time

# LogsFileName = time.strftime("%d.%m.%Y-%H.%M.%S")
# open(f'./logs/{LogsFileName}.txt','w').close()

def logsFunction(LogsFileName, fn='', txt=''):
    with open(f'logs/{LogsFileName}.txt','a') as f:
            if fn != '':
                f.write(f'{datetime.datetime.now()} function {fn.__name__}\n')
            else:
                f.write(f'{datetime.datetime.now()} action {txt}\n')

def reactionSleepTime(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
        timeout = random.randint(450, 1000) / 1000
        time.sleep(timeout)
    return wrapper
def logs(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
        print(f'{datetime.datetime.now()}  {fn.__name__}')
        # logsFunction(LogsFileName, fn)
    return wrapper