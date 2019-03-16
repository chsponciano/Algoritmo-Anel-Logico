from logicalRing import LogicalRing                                           
from process import Process
import functools 
import time   
import random

class RequestProcess(LogicalRing):

	def run(self):
		while(True):
			time.sleep(self.constTimeRequest)

			self.threadLock.acquire()
			print("RequestProcess")

			if not self.isEmptyProcess():
				index = random.randrange(self.lenActiveProcesses())
				process = self.getProcess(index)
				coordiantor = (c for c in self.getProcessAll() if c.isCoordiantor)
				print("Processo %d efetuado requisição")
				status = process.sendRequisition(coordiantor)

			self.threadLock.release()