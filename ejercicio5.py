class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def agregar_arista(self, u, v, w):
        self.grafo.append([u, v, w])

    def buscar(self, parent, i):
        if parent[i] == i:
            return i
        return self.buscar(parent, parent[i])

    def unir(self, parent, rank, x, y):
        xroot = self.buscar(parent, x)
        yroot = self.buscar(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskalMST(self):
        result = []
        i, e = 0, 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2], reverse=True)
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.buscar(parent, u)
            y = self.buscar(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.unir(parent, rank, x, y)

        return result


personajes = ['Iron Man', 'The Incredible Hulk', 'Khan', 'Thor', 'Captain America', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']
conexiones = [
  [0, 6, 0, 1, 8, 7, 3, 2],
  [6, 0, 0, 6, 1, 8, 9, 1],
  [0, 0, 0, 1, 2, 1, 5, 0],
  [1, 6, 1, 0, 1, 5, 9, 3],
  [8, 1, 2, 1, 0, 2, 4, 5],
  [7, 8, 1, 5, 2, 0, 1, 6],
  [3, 9, 5, 9, 4, 1, 0, 1],
  [2, 1, 0, 3, 5, 6, 1, 0]
]

g = Grafo(len(personajes))

for i in range(len(conexiones)):
    for j in range(i+1, len(conexiones[i])):
        if conexiones[i][j] != 0:
            g.agregar_arista(i, j, conexiones[i][j])

mst = g.kruskalMST()


# if __name__ == "__main__":

print("Árbol de expansión máximo: ")
for u, v, w in mst:
    print(f"{personajes[u]} -- {personajes[v]} == {w}")

# Cargar todos los personajes
print("Personajes cargados:")
for personaje in personajes:
  print(personaje)

# Determinar cuál es el número máximo de episodios que comparten dos personajes
print("Número máximo de episodios que comparten dos personajes:")
for u, v, w in mst:
    print(f"{personajes[u]} -- {personajes[v]} == {w}")
    print(f"{personajes[u]} y {personajes[v]} tienen {w} episodios en común.")
