import time
from numpy import *
from functools import wraps
import time
import logging

def reactionSleepTime(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
        timeout = random.randint(450, 1000) / 1000
        time.sleep(timeout)
    return wrapper
def logs(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
        logging.info(f'{fn.__name__}')
        print(f'{fn.__name__}')
        # logsFunction(LogsFileName, fn)
    return wrapper
def WinActive(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
        
        
    return wrapper