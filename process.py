import copy
import time

class Process:
	
	def __init__(self, identification, isCoordiantor):
		self.__identification = identification
		self.__isCoordiantor = isCoordiantor
	
	#Getter
	@property
	def identification(self):
		return self.__identification

	@property
	def isCoordiantor(self):
		return self.__isCoordiantor
	
	#Setter
	@identification.setter
	def identification(self, identification):
		self.__identification = identification
	
	@isCoordiantor.setter
	def isCoordiantor(self, isCoordiantor):
		self.__isCoordiantor = isCoordiantor

	def sendRequisition(self, coordiantor):
		status = False
		if coordiantor is not None:
			status = coordiantor.receiveRequisition(self.identification)

		print("%s - Fim da requisição - status: %s" % (time.ctime(time.time()), str(status)))
		return status

	def receiveRequisition(self, origin):
		print("%s - Requisição do processo %d recebida" % (time.ctime(time.time()), int(origin)))
		return True