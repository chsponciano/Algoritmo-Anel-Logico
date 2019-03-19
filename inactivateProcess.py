from logicalRing import LogicalRing
import time   
import random

'''
Classe de inativacao de processos
Onde herda a classe que controle da fila de processos
essas classe tem apenas o metodo Run() para execução da thread
onde possui o lock de sincronismo
'''
class InactivateProcess(LogicalRing):

	def run(self):
		while(True):
			#Controle de tempo com base na constante
			time.sleep(LogicalRing.constTimeInactivateProcess())
			
			#Bloqueia a entrada de novos processos
			LogicalRing.threadLock.acquire()

			'''
			1° Verifica a lista nao esta vazia
			2° Chama o metodo de inativacao
				- Busca um indice aleatorio conforme o tamanho da lista
				- Busca processo pelo indice
				- Verifica se o processo buscado não é o coordenador
				- Caso for executa novamente o metodo recursivamente
				- se não remove o processo na da lista
			'''
			if not self.isEmptyProcess():
				self.inativate()

			#Desbloqueia a entrada de novos processos
			LogicalRing.threadLock.release()
				

	def inativate(self):
		index = random.randrange(self.lenActiveProcesses())
		process = self.getProcess(index)

		if not process.isCoordiantor:
			self.removeProcess(index)
			print('%s - Processo %d inativado' % (time.ctime(time.time()), process.identification))
		else:
			self.inativate()