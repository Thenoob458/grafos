from Grafo import Grafo

if __name__ == "__main__":
    g = Grafo(True)
    g.adicionar_vertice('A')
    g.adicionar_vertice('B')
    g.adicionar_vertice('C')

    g.adicionar_aresta(0, 1, 15)
    g.adicionar_aresta(0, 2)
    g.adicionar_aresta(1, 2)

    g.vetorial()
    g.matricial()
