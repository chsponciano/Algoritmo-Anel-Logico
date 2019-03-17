from logicalRing import LogicalRing                                           
from process import Process 
import functools 
import time  


class CreateProcess(LogicalRing): 

	def run(self):
		while(True):
			LogicalRing.threadLock.acquire()

			if self.isEmptyProcess():
				self.addProcess(True)
			else:
				self.addProcess(False)

			print('%s - Processo %d criado' % (time.ctime(time.time()), self.getProcess(-1).identification))

			LogicalRing.threadLock.release()

			time.sleep(self.constTimeCreate)