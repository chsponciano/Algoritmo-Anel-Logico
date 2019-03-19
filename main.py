"""
FURB - SISTEMAS DISTRIBUIDOS
PROF.: Aurélio Hoppe
ACADEMICOS: Carlos Henrique Ponciano da Silva
			Vinicius Luis da Silva

TRABALHO PRÁTICO 01 - ALGORITMO DE ELEIÇÃO

Implementar  de  algoritmos distribuídos  de  eleição  conforme  estudados em sala  de  aula.  
Em específico, a equipe deve focar no desenvolvimento dos algoritmo Anel.

Especificação:
	▪ a cada 30 segundos um novo processo deve ser criado
	▪ a cada 25 segundos um processo fazer uma requisição para o coordenador
	▪ a cada 100 segundos o coordenador fica inativo
	▪ a cada 80 segundos um processo da lista de processos fica inativo
	▪ dois processos não podem ter o mesmo ID
	▪ dois processos de eleição não podem acontecer simultaneamente
"""
from createProcess import CreateProcess
from requestProcess import RequestProcess
from inactivateCoordiantor import InactivateCoordiantor
from inactivateProcess import InactivateProcess

threads = [CreateProcess(), RequestProcess(), InactivateCoordiantor(), InactivateProcess()]

for t in threads:
	t.start()

for t in threads:
	t.join()

