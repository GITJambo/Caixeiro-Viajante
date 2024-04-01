import re
from node import Node
import matplotlib.pyplot as plt
import math
from geracao_caminho import *


def plotar_caminho(caminho):
	anterior = caminho[0]
	for aresta in caminho[1:]:
		plt.plot([aresta.x, anterior.x], [aresta.y, anterior.y])
		anterior = aresta
	plt.show()
	plt.clf()


def calcular_distancia(caminho):
	distancia = 0.0
	anterior = caminho[0]
	for cidade in caminho[1:]:
		print(cidade.nome)
		distancia += anterior.distancia(cidade)
		anterior = cidade

	# print(f'{distancia}')
	return distancia


def main():
	global lista_arestas

	lista_arestas = inicializar_grafo()
	inicio = lista_arestas[0]

	caminho = caminho_guloso(inicio, lista_arestas)
	print(calcular_distancia(caminho))
	plotar_caminho(caminho)

	return
	# aresta.


if __name__ == '__main__':
	main()
