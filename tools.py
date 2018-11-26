from math import cos, radians, sqrt
from tabulate import tabulate
class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.group = 0
        self.visited = False
        self.x = x
        self.y = y
        self.connections = {}
class Grafo:
    def __init__(self):
        self.grafo = {}
        self.abarcador = []
        
    def distancia(self, coordinates1, coordinates2):
        return sqrt(abs(coordinates1[0] - coordinates2[0])**2 + abs(coordinates1[1] - coordinates2[1])**2)

    def poblar(self, archivo):
        with open(archivo) as csv:
            i = 0
            for line in csv:
                if i == 0:
                    i += 1
                    continue
                datos = line.split(',')
                # Guardar coordenadas en km (no lat y lon): 1 grado latitud = 110574, 1 grado de longitud = 111320*cos(latitud)
                latitud = float(datos[datos.__len__() - 3])
                # Hay que pasarlo de grados a radianes
                latitud_radianes = radians(latitud)
                longitud = float(datos[datos.__len__() - 2] )
                self.grafo.update({datos[0]: Node(datos[0], latitud * 110574, longitud * (111320 * cos(latitud_radianes)))})
                nuevo = self.grafo[datos[0]]
                for nodo in self.grafo.values():
                    if nodo == nuevo:
                        continue
                    d = self.distancia((nuevo.x, nuevo.y), (nodo.x, nodo.y))
                    if d < 10000:
                        nodo.connections.update({nuevo.id: d})
                        nuevo.connections.update({nodo.id: d})
    
    def join_clusters(self):
        stack = []
        completo = list(self.grafo.keys())
        clusters = []
        # Generar clusters
        i = 1
        while completo:
            stack.append(completo[0])
            cluster = []
            while stack:
                node_i = stack.pop()
                cluster.append(node_i)
                self.grafo[node_i].group = i
                self.grafo[node_i].visited = True
                completo.remove(node_i)
                for node in self.grafo[node_i].connections:
                    if not self.grafo[node].visited:
                        self.grafo[node].visited = True
                        stack.append(node)                        
            clusters.append(cluster)
            i+=1
        self.set_visited(False)
        for i in range(len(clusters) - 1):
            nodo1 = self.grafo[clusters[i][0]]
            nodo2 = self.grafo[clusters[i + 1][0]]
            d = self.distancia((nodo1.x, nodo1.y), (nodo2.x, nodo2.y))
            nodo1.connections.update({nodo2.id: d})
            nodo2.connections.update({nodo1.id: d})
        
    def set_visited(self, boolean):
        for node in self.grafo.values():
            node.visited = boolean

    def mst(self):
        nodo_inicio = self.grafo[list(self.grafo.keys())[0]]
        stack = [(nodo_inicio,'', 0)]
        while stack:
            nodo_i = stack.pop(0)
            self.abarcador.append(nodo_i)
            nodo_i[0].visited = True
            for connection, value in nodo_i[0].connections:
                if not self.grafo[connection].visited:
                    stack.append((self.grafo[connection], nodo_i[0], value + nodo_i[-1]))
            stack = sorted(stack, key=lambda x: x[-1])
                
        

# g = Grafo()
# g.poblar('estaciones.csv')
# g.join_clusters()
# g.join_clusters()
