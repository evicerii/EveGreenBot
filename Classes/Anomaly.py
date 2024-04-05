from adds.coordinate import *
from adds.script import *
from adds.decorators import *

class Anomaly:
    def __init__(self, name, workTime):
        self.name = name
        self.workTime = workTime     

GuristasBurr=Anomaly('Guristas Burr', 2)