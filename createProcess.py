from logicalRing import LogicalRing
import time  

'''
Classe de criar processos
Onde herda a classe que controle da fila de processos
essas classe tem apenas o metodo Run() para execução da thread
onde possui o lock de sincronismo
'''
class CreateProcess(LogicalRing): 

	def run(self):
		while(True):
			#Bloqueia a entrada de novos processos
			LogicalRing.threadLock.acquire()

			'''
			Verifica se a lista esta vazia
			caso estaja cria um processo como coordenador
			se não cria uma processo normal
			'''
			if self.isEmptyProcess():
				self.addProcess(True)
			else:
				self.addProcess(False)

			print('%s - Processo %d criado' % (time.ctime(time.time()), self.getProcess(-1).identification))

			#Desbloqueia a entrada de novos processos
			LogicalRing.threadLock.release()

			#Controle de tempo com base na constante
			time.sleep(LogicalRing.constTimeCreate)