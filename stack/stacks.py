class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

nodos = []
for i in range(10):
    nodos.append(Node(i))

for i in range(9):
    nodos[i].next = nodos[i+1]

nodo_x = nodos[0]
while nodo_x:
    print(nodo_x.data)
    nodo_x = nodo_x.next