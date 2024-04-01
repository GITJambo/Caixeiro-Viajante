import math
import matplotlib
import matplotlib.pyplot as plt


class Node(object):
	# matplotlib.use('TkAgg',force=True)
	matplotlib.use('TkAgg')
	 
	def __init__(self, nome, x, y):
		self.nome = nome
		self.x = x
		self.y = y
		self.arestas = []
		self.custo_ate_este_no = 0.0

		self.caminho = [] 
		self.caminho.append(self)
		plt.plot(self.x, self.y, marker = 'o', label=self.nome)
		plt.text(self.x, self.y, self.nome, ha='center', va='bottom')

	def adicionar_aresta(self, aresta):
		if aresta not in self.arestas:
			self.arestas.append(aresta)
			plt.plot([self.x, aresta.x], [self.y, aresta.y], label=f"{self.nome} > {aresta.nome}")
			aresta.adicionar(self)

	def adicionar(self, aresta):
		if aresta not in self.arestas:
			self.arestas.append(aresta)

	def remover_aresta(self, aresta):
		self.arestas.remove(aresta)
		return aresta.remover(self)

	def remover(self, aresta):
		self.arestas.remove(aresta)
		return self


	def __str__(self):
		return f'{self.nome}: {self.x}, {self.y}'

	def imprimir_arestas(self):
		for aresta in self.arestas:
			print(aresta)

	def get(self, index):
		return list(self.arestas)[index]

	def distancia(self, aresta):
		# print(math.dist((self.x, self.y), (aresta.x, aresta.y)))
		return math.dist((self.x, self.y), (aresta.x, aresta.y))

	def imprimir_distancias(self):
		print (f'[{self.nome}]')
		for aresta in self.arestas:
			print(f'{aresta.nome}: {self.distancia(aresta)}')
			
	def mostrar_grafo():
		plt.legend()
		plt.show()
