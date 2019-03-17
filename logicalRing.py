from process import Process    
import threading                                                                
import time   
import operator                                                          

class LogicalRing(threading.Thread):
	
	activeProcesses = []
	threadLock = threading.Lock()
	counter = 0

	def __init__(self):
		threading.Thread.__init__(self)
		self.__constTimeCreate = 3#30
		self.__constTimeRequest = 2.5#25
		self.__constTimeInactivateCoordiantor = 10#100
		self.__constTimeInactivateProcess = 8#80

	@property
	def constTimeCreate(self):
		return self.__constTimeCreate

	@property
	def constTimeRequest(self):
		return self.__constTimeRequest

	@property
	def constTimeInactivateCoordiantor(self):
		return self.__constTimeInactivateCoordiantor

	@property
	def constTimeInactivateProcess(self):
		return self.__constTimeInactivateProcess

	def isEmptyProcess(self):
		return (len(LogicalRing.activeProcesses) == 0)

	def nextProcess(self):
		LogicalRing.counter += 1
		return LogicalRing.counter

	def addProcess(self, isCoordiantor):
		LogicalRing.activeProcesses.append(Process(self.nextProcess(), isCoordiantor))

	def removeProcess(self, index):
		LogicalRing.activeProcesses.pop(index)

	def getProcess(self, index):
		return LogicalRing.activeProcesses[index]

	def getProcessAll(self):
		return LogicalRing.activeProcesses

	def lenActiveProcesses(self):
		return len(LogicalRing.activeProcesses)

	def holdElection(self):
		print("%s - Iniciado Eleições" % time.ctime(time.time()))
		
		LogicalRing.activeProcesses.sort(key = operator.attrgetter('identification'), reverse = True)
		newCoordiantor = LogicalRing.activeProcesses[0]
		status = self.updateCoordiantor(newCoordiantor)

		if status:
			print("%s - Eleição concluida! Novo coordenador %d" % (time.ctime(time.time()), newCoordiantor.identification))
		else:
			print("%s - Eleição falhou!" % (time.ctime(time.time())))

	def updateCoordiantor(self, newCoordiantor):
		if newCoordiantor is None:
			return False

		for c in LogicalRing.activeProcesses:
			c.isCoordiantor = (c.identification == newCoordiantor.identification)
		return True