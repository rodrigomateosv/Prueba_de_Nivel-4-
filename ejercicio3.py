class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, nombre):
        if nombre not in self.vertices:
            self.vertices[nombre] = {}

    def agregar_arista(self, origen, destino, etiquetas):
        self.vertices[origen][destino] = etiquetas
    
    def arbol_expansion_maximo(self, plataforma):
        aristas = [(peso[plataforma], origen, destino) for origen, aristas in self.vertices.items() for destino, peso in aristas.items()]
        aristas.sort(reverse=True)  # Ordenamos las aristas en orden decreciente de peso
        arbol = Grafo()
        for heroe in self.vertices:
            arbol.agregar_vertice(heroe)
        conjuntos = {heroe: {heroe} for heroe in self.vertices}  # Un conjunto para cada nodo
        for peso, origen, destino in aristas:
            if destino not in conjuntos[origen]:  # Si los nodos no están ya conectados
                arbol.agregar_arista(origen, destino, {plataforma: peso})
                arbol.agregar_arista(destino, origen, {plataforma: peso})  # Como el grafo es no dirigido
                nuevo_conjunto = conjuntos[origen].union(conjuntos[destino])
                for nodo in nuevo_conjunto:
                    conjuntos[nodo] = nuevo_conjunto
        return arbol

    def existe_camino(self, inicio, fin):
        visitados = {inicio}
        pila = [inicio]
        while pila:
            nodo = pila.pop()
            if nodo == fin:
                return True
            for vecino in self.vertices[nodo]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    pila.append(vecino)
        return False
    
    def seguidores(self, persona, plataforma):
        return [nombre for nombre, conexion in self.vertices[persona].items() if conexion[plataforma] > 0]
    
    def mas_popular(self, plataforma):
        max_interacciones = 0
        mas_popular = None
        for heroe, conexiones in self.vertices.items():
            interacciones = sum(conexion[plataforma] for conexion in conexiones.values())
            if interacciones > max_interacciones:
                max_interacciones = interacciones
                mas_popular = heroe
        return mas_popular
    
# Carga los datos
heroes = ['Iron Man', 'The Incredible Hulk', 'Khan', 'Thor', 'Captain America', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']

twitter_matrix = [
    [0, 75, 40, 16, 80, 20, 99, 23],
    [75, 0, 50, 67, 79, 38, 99, 41],
    [40, 50, 0, 17, 75, 52, 85, 28],
    [16, 67, 17, 0, 11, 50, 90, 36],
    [80, 79, 75, 11, 0, 26, 12, 56],
    [20, 38, 52, 50, 26, 0, 55, 61],
    [99, 99, 85, 90, 12, 55, 0, 10],
    [23, 41,
