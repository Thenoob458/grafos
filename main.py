from Grafo import Grafo

arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'),
           ('D', 'A'), ('E', 'B')]

if __name__ == "__main__":
    g = Grafo()
    g.adicionar_vertice('A')
    g.adicionar_vertice('B')
    g.adicionar_vertice('C')

    g.adicionar_aresta(0, 1)
    '''
    g.adicionar_aresta('B', 'C')
    g.adicionar_aresta('C', 'A')
    g.adicionar_aresta('B', 'A')
    #print(g._str_())
    '''

    g.vetorial()
    #g.matricial()
