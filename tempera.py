import random
import matplotlib.pyplot as plt
import numpy
from geracao_caminho import *

lista_arestas = []
ITERACOES = 10000

prob_inicial = 0.8
prob_final = 0.001
reducao = (prob_final / prob_inicial) ** (1 / ITERACOES)

temperatura_atual = prob_inicial

def mostrar_caminho(caminho):
	plt.clf()

	anterior = caminho[0]
	for aresta in caminho [1:]:
		plt.plot([aresta.x, anterior.x], [aresta.y, anterior.y])
		anterior = aresta
	plt.show()

def calcular_distancia(caminho):
	distancia = 0.0
	anterior = caminho[0]
	for cidade in caminho[1:]:
		distancia += anterior.distancia(cidade)
		anterior = cidade
	return distancia


def reposicionamento_subconjuntos(caminho_original):
	caminho = caminho_original.copy()

	tamanho_caminho = len(caminho) - 1
	index_1 = random.randint(1, tamanho_caminho - 1)
	index_2 = random.randint(1, tamanho_caminho - 1)

	upper = max(index_1, index_2)
	lower = min(index_1, index_2)

	corte = caminho[lower : upper]
	for cidade in corte:
		caminho.remove(cidade)

	index_glu = random.randint(1, len(caminho) - 1)
	for i in range (0, len(corte)):
		caminho.insert(i + index_glu, corte[i])

	return caminho

def inversao_subconjuntos(caminho_original):
	caminho = caminho_original.copy()
	tamanho_caminho = len(caminho) - 1

	index_1 = random.randint(1, tamanho_caminho - 1)
	index_2 = random.randint(1, tamanho_caminho - 1)

	upper = max(index_1, index_2)
	lower = min(index_1, index_2)

	toSwap = caminho[lower: upper]
	toSwap.reverse()

	for cidade in toSwap:
		caminho.remove(cidade)
	for i in range (0, len(toSwap)):
		caminho.insert(i + lower, toSwap[i])
	return caminho

def tempera_simulada(caminho, index):
	global temperatura_atual

	temperatura_atual *= reducao

	distancia_1 = calcular_distancia(caminho)
	caminho_2 = reposicionamento_subconjuntos(caminho)
	distancia_2 = calcular_distancia(caminho_2)

	if (distancia_2 < distancia_1):
		return (caminho_2, distancia_2)
	else:
		probabilidade_variada = numpy.exp(-(distancia_2 - distancia_1 ) / temperatura_atual )

		if(random.random() < probabilidade_variada):
			return (caminho_2, distancia_2)

	return (caminho, distancia_1)

def main():
	global lista_arestas, temperatura_atual, ITERACOES
	lista_arestas = inicializar_grafo()

	inicio = lista_arestas[0]	

	caminho = caminho_guloso(inicio, lista_arestas)
	menor = (caminho, calcular_distancia(caminho))

	for i in range(0, 50):
		is_stable = 0
		caminho = caminho_guloso(inicio, lista_arestas)
		caminho = (caminho, calcular_distancia(caminho))
		ultima_distancia = caminho[1]

		while(is_stable < 3):
			temperatura_atual = prob_inicial
			for iteracao in range(1, ITERACOES):
				caminho = tempera_simulada(caminho[0], iteracao)

			if (caminho[1] == ultima_distancia):
				is_stable += 1
			else:
				is_stable = 0
			if (caminho[1] < menor[1]):
				menor = caminho
			ultima_distancia = caminho[1]

		print (f'{menor[1]}', end=", ")

if __name__ == '__main__':
	main()
