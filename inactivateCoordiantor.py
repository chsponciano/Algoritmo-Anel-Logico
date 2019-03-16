from logicalRing import LogicalRing                                           
from process import Process
import functools 
import time   
import random

class InactivateCoordiantor(LogicalRing):
    
    def run(self):
    	while(True):
            time.sleep(self.constTimeInactivateCoordiantor)

            self.threadLock.acquire()
            print("InactivateCoordiantor")
            coordiantor = None
            index = 0

            for c in self.getProcessAll():
                if c.isCoordiantor:
                    print(c)
                    coordiantor = c
                    break
                index += 1
            if coordiantor is not None:
                self.removeProcess(index)
                print("Coordenador %d inativado" % index)

            self.threadLock.release()
