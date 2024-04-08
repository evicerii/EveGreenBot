import time
from numpy import *
from functools import wraps
import datetime
import asyncio

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
    return wrapper