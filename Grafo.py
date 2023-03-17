import numpy as np
from Vertice import Vertice


class Grafo:

    def __init__(self):
        #self.vertices = {}
        self.vertices = []

    def nomear_vertice(self, index):
        return (self.vertices[index].get_label())

    def adicionar_vertice(self, label):
        self.vertices.append(Vertice(label))
        '''
        if vertice not in self.vertices:
            self.vertices[vertice] = {}
        '''

    def excluir_vertice(self, vertice):
        self.vertices.remove(self.vertices[vertice])
        '''if vertice in self.vertices:
            for origem in self.vertices:
                if vertice in self.vertices[origem]:
                    del self.vertices[origem][vertice]
            del self.vertices[vertice]
        '''

    def adicionar_aresta(self, origem, destino, peso=1):
        if origem in self.vertices:
            self.vertices[origem][destino] = peso
        else:
            self.vertices[origem] = {destino: peso}

    def excluir_aresta(self, origem, destino):
        if origem in self.vertices:
            if destino in self.vertices[origem]:
                del self.vertices[origem][destino]

    def adjacencia(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            return vertice2 in self.vertices[
                vertice1] or vertice1 in self.vertices[vertice2]
        else:
            return False

    def existe_aresta(self, origem, destino):
        if origem in self.vertices:
            return destino in self.vertices[origem]
        else:
            return False

    def peso_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices[origem]:
            return self.vertices[origem][destino]
        else:
            return None

    def vizinhos(self, vertice):
        if vertice in self.vertices:
            return list(self.vertices[vertice].keys())
        else:
            return []

    def vetorial(self):
        for i in range(len(self.vertices)):
            print(f"{self.nomear_vertice(i)} → porra")

    def matricial(self):
        '''matriz = np.zeros((self.tamanho, self.tamanho))
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if i != j:
                    matriz[i][j] = self.vertices[i]
        '''

        for i in self.vertices:
            print()

        #print(matriz)
