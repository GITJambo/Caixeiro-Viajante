import re
from node import Node
from individuo import Individuo
import numpy
import random
import matplotlib.pyplot as plt
import math
from geracao_caminho import *

lista_arestas = []

NUMERO_INDIVIDUOS = 12
individuo_index = 0


def batalhar(lutadores, num_lutadores):
	menor_caminho_batalhadores = math.inf
	vencedor = None

	for i in range(0, num_lutadores):
		lutador_escolhido = lutadores[random.randint(0, len(lutadores) - 1)]
		lutadores.remove(lutador_escolhido)

		if (lutador_escolhido.distancia < menor_caminho_batalhadores):
			menor_caminho_batalhadores = lutador_escolhido.distancia
			vencedor = lutador_escolhido

	return [vencedor] * num_lutadores

def torneio(lutadores):
	vitoriosos = []

	num_lutadores_por_batalha = 3
	for i in range(0, NUMERO_INDIVIDUOS, num_lutadores_por_batalha): #individuo in populacao_inicial:]
		vitoriosos += batalhar(lutadores, num_lutadores_por_batalha)
	# random.shuffle(vitoriosos) # reordenados para aumentar diversidade
	return vitoriosos

def ranking(populacao_inicial):
	pesos = []
	pressao_reprodutiva = 1.95
	for i in range(NUMERO_INDIVIDUOS, 0, -1): #individuo in populacao_inicial:]
		sp = 2 - pressao_reprodutiva + (2 * (pressao_reprodutiva - 1) * (i - 1) / (NUMERO_INDIVIDUOS - 1) )
		pesos.append(sp) 

	soma_pesos = sum(pesos)
	pesos = [p / soma_pesos for p in pesos]

	return numpy.random.choice(populacao_inicial, p=pesos)

def selecao(populacao_inicial):
	pesos = [1.0 / p.distancia for p in populacao_inicial] 
	soma_pesos = sum(pesos)
	pesos = [p / soma_pesos for p in pesos] 
	return numpy.random.choice(populacao_inicial, p=pesos)

def selecionar_populacao_aleatoriamente(populacao_inicial, distancia_total):
	selecionados = []

	populacao_inicial.sort(key=lambda x: x.distancia)
	# protegidos = 2 #int(NUMERO_INDIVIDUOS * 0.3)
	# selecionados += populacao_inicial[0:protegidos]

	for i in range(0, NUMERO_INDIVIDUOS):
		selecionados.append(ranking(populacao_inicial))

	return selecionados

def gerar_individuos(inicio):
	global individuo_index

	populacao_inicial = []
	for i in range(0, NUMERO_INDIVIDUOS):
		caminho = caminho_guloso(inicio, lista_arestas)
		novo_individuo = Individuo(individuo_index, caminho)

		individuo_index += 1
		populacao_inicial.append(novo_individuo)

	return populacao_inicial

def cross_over(selecionado_1, selecionado_2):
	global individuo_index
	tamanho_caminho = len(selecionado_1.caminho)

	corte = 3 #tamanho_caminho // 8 + 1
	posicao_corte = random.randint(1, tamanho_caminho - corte)
	selecionado_2_caminho = selecionado_2.caminho.copy()

	cross_over = []

	for index in range (posicao_corte, posicao_corte + corte):
		index_inicial = index
		index_troca  = selecionado_2_caminho.index(selecionado_1.caminho[index])

		selecionado_2_caminho[index_inicial], selecionado_2_caminho[index_troca] = selecionado_2_caminho[index_troca], selecionado_2_caminho[index_inicial]

	cross_over = selecionado_2_caminho[0: tamanho_caminho]

	individuo_index += 1
	novo_individuo = Individuo(individuo_index, cross_over)

	return novo_individuo


def prox_geracao(populacao):
	selecionados = torneio(populacao)
	cross_over_individuos = []

	while (len(selecionados) > 1):
		ind_1 = random.choice(selecionados)
		selecionados.remove(ind_1)
		ind_2 = random.choice(selecionados)
		selecionados.remove(ind_2)

		cross_over_individuos.append(cross_over(ind_1, ind_2))
		cross_over_individuos.append(cross_over(ind_2, ind_1))

	# distancia_total = sum(individuo.distancia for individuo in populacao)
	# selecionados = selecionar_populacao_aleatoriamente(populacao, distancia_total)
	# for i in range(0, NUMERO_INDIVIDUOS, 2):
	# 	cross_over_individuos.append(cross_over(selecionados[i], selecionados[i+1]))
	# 	cross_over_individuos.append(cross_over(selecionados[i+1], selecionados[i]))

	return cross_over_individuos

def encontrar_menor(menor, populacao):
	for peep in populacao:
		if peep.distancia < menor.distancia:
			menor = peep
	return menor

def	plotar_caminho(menor):
	plt.clf()

	anterior = menor.caminho[0]
	for aresta in menor.caminho [1:]:
		plt.plot([aresta.x, anterior.x], [aresta.y, anterior.y])
		anterior = aresta
	plt.show()

def main():
	global lista_arestas, individuo_index

	lista_arestas = inicializar_grafo()

	inicio = lista_arestas[0]

	populacao = gerar_individuos(inicio)
	menor = populacao[0]

	# for i in range(0, 50):
	# 	is_stable = 0
	# 	populacao = gerar_individuos(inicio)
	# 	menor = populacao[0]

	# 	while(is_stable < 1):
	# 		for i in range(0, 4000):
	# 			populacao = prox_geracao(populacao)
	# 			menor_atual = encontrar_menor(menor, populacao)

	# 		if (menor_atual.distancia == menor.distancia):
	# 			is_stable += 1
	# 		else:
	# 			is_stable = 0

	# 		menor = menor_atual

	# 	print(f'{menor.distancia}')

	while (True):
		populacao = gerar_individuos(inicio)
		menor = populacao[0]

		for i in range(0, 7800):
			populacao = prox_geracao(populacao)
			menor = encontrar_menor(menor, populacao)
		print(f'{menor.distancia}', end=', ')
		# plotar_caminho(menor)


if __name__ == '__main__':
	main()


	    
	    

	               
		                               



 
		    
		        

 
