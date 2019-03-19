from process import Process    
import threading                                                                
import time   
import operator    
import random                                                      

'''
Classe de controle da fila de processos, herdando a classe thread 
'''
class LogicalRing(threading.Thread):
	
	#Lista de processos ativos
	activeProcesses = []
	
	#Lock de controle de processos ativos em execução
	threadLock = threading.Lock()

	#Contador de processos
	counter = 0
	
	#Constantes de tempo das acoes
	@staticmethod
	def constTimeCreate(): return 3 #30

	@staticmethod
	def constTimeRequest(): return 2.5 #25

	@staticmethod
	def constTimeInactivateCoordiantor(): return 10 #100

	@staticmethod
	def constTimeInactivateProcess(): return 8 #80

	def __init__(self):
		threading.Thread.__init__(self)

	#Verifica se a lista está vazia
	def isEmptyProcess(self):
		return (len(LogicalRing.activeProcesses) == 0)

	#Define o próximo ID do processo
	def nextProcess(self):
		LogicalRing.counter += 1
		return LogicalRing.counter

	#Cria um novo Processo na Lista
	def addProcess(self, isCoordiantor):
		LogicalRing.activeProcesses.append(Process(self.nextProcess(), isCoordiantor))

	#Remove o processo na Lista
	def removeProcess(self, index):
		LogicalRing.activeProcesses.pop(index)

	#Retorna um processo da lista pelo indice
	def getProcess(self, index):
		return LogicalRing.activeProcesses[index]

	#Retorna todos os processos da lista
	def getProcessAll(self):
		return LogicalRing.activeProcesses

	#Retorna o tamanho da lista
	def lenActiveProcesses(self):
		return len(LogicalRing.activeProcesses)

	#Retorna o coordenador
	def getCoordiantor(self):
		coordiantor = None
		index = 0
		for c in LogicalRing.activeProcesses:
			if c.isCoordiantor:
				coordiantor = c
				break
			index += 1
		return (index, coordiantor)

	'''
	Processo de eleição
	1° Ordena a lista de forma decresente pelo identificador
	2° Pega o primeiro processo da lista
	3° Chama o metodo de update do coordenador  
	'''
	def holdElection(self):
		print("%s - Iniciado Eleições" % time.ctime(time.time()))
		
		LogicalRing.activeProcesses.sort(key = operator.attrgetter('identification'), reverse = True)
		newCoordiantor = LogicalRing.activeProcesses[0]
		status = self.updateCoordiantor(newCoordiantor)

		if status:
			print("%s - Eleição concluida! Novo coordenador %d" % (time.ctime(time.time()), newCoordiantor.identification))
		else:
			print("%s - Eleição falhou!" % (time.ctime(time.time())))

	#Atualiza o coordenador em todos os processos
	def updateCoordiantor(self, newCoordiantor):
		if newCoordiantor is None:
			return False

		for c in LogicalRing.activeProcesses:
			c.isCoordiantor = (c.identification == newCoordiantor.identification)
		return True