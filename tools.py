from math import cos, radians, sqrt
from tabulate import tabulate

def distancia(coordinates1, coordinates2):
    return sqrt(abs(coordinates1[0] - coordinates2[0])**2 + abs(coordinates1[1] - coordinates2[1])**2)

def matriz_adyacencia():
    coordenadas = []
    m_adyacencia = []
    with open('estaciones.csv') as csv:
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

            coordenadas.append((datos[0], latitud * 110574, longitud * (111320 * cos(latitud_radianes))))
    # Generar la matriz de adyacencia...
    for i in range(len(coordenadas)):
        fila = []
        for j in range(len(coordenadas)):
            # Si es la misma estación la distancia es 0
            if i == j:
                fila.append(0)
            else:
                coordenadas1 = (coordenadas[i][1], coordenadas[i][2])
                coordenadas2 = (coordenadas[j][1], coordenadas[j][2])
                d = distancia(coordenadas1, coordenadas2)
                # Si la distancia es menor a 10,000 km entonces 1 de conexión
                if d < 10000:
                    fila.append(1)
                # Si no 10,000 de distancia máxima
                else:
                    fila.append(10000)
        m_adyacencia.append(fila)
    # Para imprimit la matriz (Ya está le ejemplo en el archivo de 'adyacencia')
    # print(tabulate(m_adyacencia, tablefmt='simple'))
    return m_adyacencia

matriz_adyacencia()
