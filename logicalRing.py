from process import Process    
import threading                                                                
import time   
import operator                                                          

class LogicalRing(threading.Thread):
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.__activeProcesses = []
		self.__constTimeCreate = 3#30
		self.__constTimeRequest = 2.5#25
		self.__constTimeInactivateCoordiantor = 10#100
		self.__constTimeInactivateProcess = 8#80
		self.threadLock = threading.Lock()

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
		return (len(self.__activeProcesses) == 0)

	def nextProcess(self):
		if self.isEmptyProcess():
			return 1
		return int(self.__activeProcesses[-1].identification) + 1

	def addProcess(self, isCoordiantor):
		self.__activeProcesses.append(Process(self.nextProcess(), isCoordiantor))

	def removeProcess(self, index):
		self.__activeProcesses.pop(index)

	def getProcess(self, index):
		return self.__activeProcesses[index]

	def getProcessAll(self):
		return self.__activeProcesses

	def lenActiveProcesses(self):
		return len(self.__activeProcesses)

	def holdElection(self):
		print("Iniciado Eleições")
		
		newCoordiantor = self.__activeProcesses.sort(key = operator.attrgetter(identification), reverse = True)[0]
		status = self.updateCoordiantor(newCoordiantor)

		if status:
			print("Eleição concluida! Novo coordenador %d" % newCoordiantor.identification)
		else:
			print("Eleição falhou!")

	def updateCoordiantor(self, newCoordiantor):
		for c in self.__activeProcesses:
			if c.identification == newCoordiantor.identification:
				c.isCoordiantor(True)
			else:
				c.isCoordiantor(False)

		return True