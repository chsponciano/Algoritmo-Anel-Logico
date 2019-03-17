from logicalRing import LogicalRing                                           
from process import Process
import functools 
import time   
import random

class InactivateCoordiantor(LogicalRing):
    
    def run(self):
    	while(True):
            time.sleep(self.constTimeInactivateCoordiantor)

            LogicalRing.threadLock.acquire()
            coordiantor = None
            index = 0

            for c in self.getProcessAll():
                if c.isCoordiantor:
                    coordiantor = c
                    break
                index += 1

            if coordiantor is not None:
                self.removeProcess(index)
                print("%s - Coordenador %d inativado" % (time.ctime(time.time()), coordiantor.identification))

            LogicalRing.threadLock.release()
