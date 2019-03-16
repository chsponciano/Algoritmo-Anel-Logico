from logicalRing import LogicalRing                                           
from process import Process 
import functools 
import time  


class CreateProcess(LogicalRing): 
	def run(self):
		while(True):
			self.threadLock.acquire()

			if self.isEmptyProcess():
				self.addProcess(True)
			else:
				self.addProcess(False)

			print('Processo %d criado' % self.getProcess(-1).identification)
			self.threadLock.release()
			time.sleep(self.constTimeCreate)