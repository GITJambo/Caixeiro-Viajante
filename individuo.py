import random

PROBABILIDADE_MUTACAO = 10 #porcentagem

class Individuo:
	fitness = 1
	def __init__(self, index, caminho):
		self.index = index
		self.caminho = caminho
		self.distancias = []

		self.distancia = self.calcular_distancia(caminho)

		if (random.randint(0, PROBABILIDADE_MUTACAO // 2) == 1):
			self.mutacao_swap()
		if (random.randint(0, PROBABILIDADE_MUTACAO) == 1):
			self.mutacao()

	def calcular_distancia(self, caminho):
		distancia = 0.0
		anterior = caminho[0]
		self.distancias.append(0.0)

		for cidade in caminho[1:]:
			mudanca_distancia = anterior.distancia(cidade)
			self.distancias.append(mudanca_distancia)
			distancia += mudanca_distancia
			anterior = cidade

		print(f'{self.index}: {distancia}')
		return distancia
	
	# def piores_nos(self):
	# 	return random.choices(self.caminho[1:-1], weights=(self.distancias[1:-1]), k=1)
	
	def mutacao_swap(self):
		caminho = self.caminho
		tamanho_caminho = len(self.caminho) - 1

		# pior_no = self.piores_nos()[0]
		# index_1 = caminho.index(pior_no)
		index_1 = random.randint(1, tamanho_caminho - 1)
		index_2 = random.randint(1, tamanho_caminho - 1)

		caminho[index_1], caminho[index_2] = caminho[index_2], caminho[index_1]

		self.distancia = self.calcular_distancia(self.caminho)

	def mutacao(self):
		novo_caminho = self.caminho.copy()

		tamanho_caminho = len(self.caminho) - 1

		tamanho_mutacao = random.randint(1, tamanho_caminho // 3) + 1
		posicao_mutacao = random.randint(1, tamanho_caminho - tamanho_mutacao - 1)

		caminho_mutado = novo_caminho[posicao_mutacao: posicao_mutacao + tamanho_mutacao]
		caminho_mutado.reverse()

		novo_caminho = novo_caminho[0: posicao_mutacao] + caminho_mutado + novo_caminho[posicao_mutacao + tamanho_mutacao: tamanho_caminho + 1]
		self.caminho = novo_caminho
		#reverse genes
		# caminho_sem_bordas = novo_caminho[1 : -1]
		# caminho_sem_bordas.reverse()
		# novo_caminho = [novo_caminho[0]] + caminho_sem_bordas + [novo_caminho[tamanho_caminho]]
		# self.caminho = novo_caminho

		self.distancia = self.calcular_distancia(self.caminho)
		return