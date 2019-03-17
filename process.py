import time

'''
Classe modelo dos processos
identification = ID de controle de processos
isCoordiantor = eh coordenador?
'''
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

	'''
	Envio de mensagem para o coordenador
	'''
	def sendRequisition(self, coordiantor):
		status = False
		if coordiantor is not None:
			status = coordiantor.receiveRequisition(coordiantor.identification, self.identification)

		print("%s - Fim da requisição - status: %s" % (time.ctime(time.time()), str(status)))
		return status

	'''
	Recebimento de mensagem informando a origem da requisicao
	'''
	def receiveRequisition(self, coordiantor, origin):
		print("%s - Requisição do processo %d recebida pelo coordenador %d" % (time.ctime(time.time()), int(origin), int(coordiantor)))
		return True