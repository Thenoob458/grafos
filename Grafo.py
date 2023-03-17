import numpy as np
from Vertice import Vertice


class Grafo(object):

    def __init__(self, direcionado=False):
        self.vertices = []
        self.direcionado = direcionado
        #falta fazer ser direcionado

    def nomear_vertice(self, index):
        return (self.vertices[index].get_label())

    def adicionar_vertice(self, label):
        self.vertices.append(Vertice(label))
        #falta verificar se ja existe

    def excluir_vertice(self, vertice):
        self.vertices.remove(self.vertices[vertice])
        #falta verificar se existe

    def adicionar_aresta(self, origem, destino, peso=1):
        self.vertices[origem].arestas[destino] = peso

    def excluir_aresta(self, origem, destino):
        self.vertices[origem].arestas.pop(destino)

    def existe_aresta(self, origem, destino):
        return self.vertices[origem].arestas.__contains__(destino)

    def peso_aresta(self, origem, destino):
        if self.existe_aresta(origem, destino):
            return self.vertices[origem].arestas[destino]
        return -1

    def vizinhos(self, vertice):
        return self.vertices[vertice].arestas

    def vetorial(self):
        for i in range(len(self.vertices)):
            print(f"{self.nomear_vertice(i)} → {self.vertices[i].arestas}")

    def matricial(self):
        matriz = np.zeros((len(self.vertices), len(self.vertices)))

        for i in range(len(self.vertices)):
            print(f"   {self.nomear_vertice(i)}", end=" ")

        print("\n")

        for i in range(len(self.vertices)):
            print(self.nomear_vertice(i), end=" ")

            for j in range(len(self.vertices)):
                if self.existe_aresta(i, j):
                    matriz[i, j] = self.peso_aresta(i, j)
                print(f"[{matriz[i][j]}]", end=" ")

            print()
        #print(matriz)
