import re
from node import Node
import math
import individuo
import random


def caminho_aleatorio(inicio, lista_arestas):
	caminho = [inicio]

	copia_arestas = lista_arestas.copy()
	copia_arestas.remove(inicio)

	tamanho_grafo = len(copia_arestas) - 1

	while (tamanho_grafo >= 0):
		prox_no = copia_arestas[random.randint(0, tamanho_grafo)]
		copia_arestas.remove(prox_no)
		caminho.append(prox_no)
		tamanho_grafo = len(copia_arestas) - 1

	caminho.append(inicio)

	return caminho


def caminho_guloso(inicio, lista_arestas):
	caminho = [inicio]

	copia_arestas = lista_arestas.copy()
	tamanho_grafo = len(copia_arestas) - 1

	ultimo_no_adicionado = inicio

	while (tamanho_grafo >= 0):
		menor_distancia = math.inf
		proxima_cidade = None

		for cidade in copia_arestas:
			if (cidade is ultimo_no_adicionado):
				continue
			if (ultimo_no_adicionado is None):
				print()
			distancia_atual = ultimo_no_adicionado.distancia(cidade)

			if (distancia_atual < menor_distancia):
				proxima_cidade = cidade
				menor_distancia = distancia_atual

		if (proxima_cidade is None):
			break

		copia_arestas.remove(ultimo_no_adicionado)
		caminho.append(proxima_cidade)

		ultimo_no_adicionado = proxima_cidade
		tamanho_grafo = len(copia_arestas) - 1

	caminho.append(inicio)

	return caminho


def inicializar_grafo(number_of_nodes=200):
	lista_arestas = []

	i = 0
	with open("coords.txt", "r") as file:
		for node in file:
			node_parts = re.search('(.*)?:\W(.*?),\W(.*?)$', node)
			lista_arestas.append(
			    Node(node_parts.group(1), float(node_parts.group(2)),
			         float(node_parts.group(3))))
			i += 1
			if (i > number_of_nodes):
				break

	return lista_arestas
