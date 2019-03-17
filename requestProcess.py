from logicalRing import LogicalRing
import time   
import random

'''
Classe de envio de mensagem ao coordenador pelos processos
Onde herda a classe que controle da fila de processos
essas classe tem apenas o metodo Run() para execução da thread
onde possui o lock de sincronismo
'''
class RequestProcess(LogicalRing):

	def run(self):
		while(True):
			#Controle de tempo com base na constante
			time.sleep(LogicalRing.constTimeRequest)

			#Bloqueia a entrada de novos processos
			LogicalRing.threadLock.acquire()

			'''
			1° Verifica se a lista nao esta vazia
			2° Busca um indice aleatorio conforme o tamanho da lista
			3° Busca processo pelo indice
			4° Busca o coordenador atual
			5° Envia a mensagem
			6° Caso nao encontre o coordenador solicita a eleicao de um novo
			'''
			if not self.isEmptyProcess():
				process = self.getProcess(random.randrange(self.lenActiveProcesses()))
				coordiantor = self.getCoordiantor()[1]

				print("%s - Processo %d efetuado requisição" % (time.ctime(time.time()), process.identification))
				status = process.sendRequisition(coordiantor)

				if not status:
					self.holdElection()

			#Desbloqueia a entrada de novos processos
			LogicalRing.threadLock.release()