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

	#Method Abstract
	def sendRequisition(self, coordiantor):
		if coordiantor is not None:
			return coordiantor.receiveRequisition(self.identification)

		print("Fim da requisição")
		return False

	def receiveRequisition(self, origin):
		print("Requisição do processo %d recebida" % origin)
		return True

