from logicalRing import LogicalRing                                           
from process import Process
import functools 
import time   
import random

class RequestProcess(LogicalRing):

	def run(self):
		while(True):
			time.sleep(self.constTimeRequest)

			LogicalRing.threadLock.acquire()

			if not self.isEmptyProcess():
				index = random.randrange(self.lenActiveProcesses())
				process = self.getProcess(index)
				coordiantor = None
				for c in self.getProcessAll():
					if c.isCoordiantor:
						coordiantor = c

				print("%s - Processo %d efetuado requisição" % (time.ctime(time.time()), process.identification))
				status = process.sendRequisition(coordiantor)

				if not status:
					self.holdElection()

			LogicalRing.threadLock.release()