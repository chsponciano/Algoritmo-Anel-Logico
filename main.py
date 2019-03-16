"""
FURB - SISTEMAS DISTRIBUIDOS
PROF.: Aurélio Hoppe
ACADEMICOS: Carlos Henrique Ponciano da Silva
			Vinicius Luis da Silva

TRABALHO PRÁTICO 01 - ALGORITMO DE ELEIÇÃO

Implementar  de  algoritmosdistribuídos  de  eleição  conforme  estudados  emsala  de  aula.  Em específico, a equipe deve focar no desenvolvimento dos algoritmos Bully e Anel.
Especificação:
	▪a cada 30 segundos um novo processo deve ser criado
	▪a cada 25 segundos um processo fazer uma requisiçãopara o coordenador
	▪a cada 100 segundos o coordenador fica inativo
	▪a cada 80 segundos um processo da lista de processos fica inativo
	▪dois processos não podem ter o mesmo ID
	▪dois processos de eleição não podem acontecer simultaneamente
"""
from threading import Thread
from createProcess import CreateProcess
from requestProcess import RequestProcess
from inactivateCoordiantor import InactivateCoordiantor
from inactivateProcess import InactivateProcess

threads = []
#threads.append(CreateProcess())
#threads.append(RequestProcess())
#threads.append(InactivateCoordiantor())
threads.append(InactivateProcess())

for t in threads:
	t.start()

for t in threads:
	t.join()

