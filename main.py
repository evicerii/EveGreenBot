from multiprocessing import Process, Event
import time
from Green import *
from adds.script import *
def CheckLocal(event):
    while True:
        time.sleep(4)
        if cvName(general['CheckLocal'])=="Local":
            print(f'local normal')
            event.clear()
        else:
            event.set()
            print(f'local red')
def CheckFarm(event):
    while True:
        while True:
            if event.is_set():
                asyncio.run(runBot())
            else:
                break
        time.sleep(150)


startTime=datetime.datetime.now().hour*60 + datetime.datetime.now().minute

if __name__ == '__main__':
    CheckLocalEvent = Event()
    procs=[]
    Local = Process(target=CheckLocal, args=(CheckLocalEvent,), daemon=True)
    BotControl = Process(target=CheckFarm, args=(CheckLocalEvent,))
    procs.append(Local)
    procs.append(BotControl)
    [p.start() for p in procs]
    [p.join() for p in procs]