from Grafo import *

arestas = [('A', 'B'), 
           ('B', 'C'), 
           ('B', 'D'), 
           ('C', 'B'), 
           ('C', 'E'), 
           ('D', 'A'), 
           ('E', 'B')]

if __name__ == "__main__":
    grafo = Grafo(arestas, direcionado=True)
    print(grafo.get_arestas())
    