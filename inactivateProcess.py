from logicalRing import LogicalRing                                           
from process import Process
import functools 
import time   
import random

class InactivateProcess(LogicalRing):

	def run(self):
		while(True):
			self.threadLock.acquire()

			print("InactivateProcess")
			if not self.isEmptyProcess():
				index = random.randrange(self.lenActiveProcesses())
				process = self.getProcess(index)

				if process is not None and not process.isCoordiantor:
					self.removeProcess(index)
					print('Processo %d inativado' % self.getProcess(-1).identification)

				self.threadLock.release()
				
			time.sleep(self.constTimeInactivateProcess)