class Graph:
    def __init__(self, size):
        self.adj_matriz = [[None]*size for _ in range(size)]
        self.size = size
        self.nombre_nodos = [''] * size

    def agregar_nodo(self, nombre, posicion):
        self.nombre_nodos[posicion] = nombre
    
    def agregar_arista(self, origen, destino, peso):
        self.adj_matriz[origen][destino] = peso
    
    def print_graph(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.adj_matriz[i][j] is not None:
                    print(f"{self.nombre_nodos[i]}:{self.nombre_nodos[j]}={self.adj_matriz[i][j]}", end=' ')

    def print_adj_matriz(self):
        for i in range(self.size):
            print(self.adj_matriz[i])


graph = Graph(4)
graph.agregar_nodo('A', 0)
graph.agregar_nodo('B', 1)
graph.agregar_nodo('C', 2)
graph.agregar_nodo('D', 3)
graph.agregar_arista(0, 1, 2)
graph.agregar_arista(1, 2, 3)
graph.agregar_arista(2, 3, 1)
graph.agregar_arista(0, 2, 4)
graph.agregar_arista(3, 3, 10)
graph.print_graph()
print()
graph.print_adj_matriz()