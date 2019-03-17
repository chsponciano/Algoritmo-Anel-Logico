from logicalRing import LogicalRing                                           
from process import Process
import functools 
import time   
import random

class InactivateProcess(LogicalRing):

	def run(self):
		while(True):
			time.sleep(self.constTimeInactivateProcess)
			
			LogicalRing.threadLock.acquire()

			if not self.isEmptyProcess():
				self.inativate()

			LogicalRing.threadLock.release()
				

	def inativate(self):
		index = random.randrange(self.lenActiveProcesses())
		process = self.getProcess(index)

		if process is not None and not process.isCoordiantor:
			self.removeProcess(index)
			print('%s - Processo %d inativado' % (time.ctime(time.time()), process.identification))
		else:
			self.inativate()