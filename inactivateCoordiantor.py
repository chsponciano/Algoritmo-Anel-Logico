from logicalRing import LogicalRing
import time   

'''
Classe de inativacao de Coordenador
Onde herda a classe que controle da fila de processos
essas classe tem apenas o metodo Run() para execução da thread
onde possui o lock de sincronismo
'''
class InactivateCoordiantor(LogicalRing):
    
    def run(self):
    	while(True):
            #Controle de tempo com base na constante
            time.sleep(LogicalRing.constTimeInactivateCoordiantor())

            #Bloqueia a entrada de novos processos
            LogicalRing.threadLock.acquire()

            #Pega o indice e o processo do coordenador
            index, coordiantor = self.getCoordiantor()

            #Verifica se o coordenador nao eh nulo e remove ele da lista pelo indice
            if coordiantor is not None:
                self.removeProcess(index)
                print("%s - Coordenador %d inativado" % (time.ctime(time.time()), coordiantor.identification))

            #Desbloqueia a entrada de novos processos
            LogicalRing.threadLock.release()
