#Matriz test en lo que encuentro la manera de usar la del CSV
matrizAdyacencia = [[0, 4876.89, 0, 0, 0, 0, 0, 8972.0136, 0], 
		[4876.89, 0, 8972.0136, 0, 0, 0, 0, 12854, 0], 
		[0, 8972.0136, 0, 6967.212, 0, 4876.89, 0, 0, 2546.22], 
		[0, 0, 6967.212, 0, 10265.5446, 16884.026456, 0, 0, 0], 
		[0, 0, 0, 10265.5446, 0, 11352.15654, 0, 0, 0], 
		[0, 0, 4876.89, 16884.026456, 11352.15654, 0, 2546.22, 0, 0], 
		[0, 0, 0, 0, 0, 2546.22, 0, 1500.65, 6704.556], 
		[8972.0136, 12854, 0, 0, 0, 0, 1500.65, 0, 6967.212], 
		[0, 0, 2546.22, 0, 0, 0, 6704.556, 6967.212, 0]] 

class FuncionesMatriz: 
	def distanciaMin(self,distancia,cola): #Self-explanatory
		valorMin = float("Inf") #Inicializar en ∞
		indice = -1
		for i in range(len(distancia)): 
			if distancia[i] < valorMin and i in cola: 
				valorMin = distancia[i] 
				indice = i 
		return indice
	def mostrarCamino(self, valorPadre, j): #Imprime recorrido 
		if valorPadre[j] == -1: 
			print (j),
			return
		self.mostrarCamino(valorPadre , valorPadre[j]) 
		print (j),
	def imprimirFinal(self, distancia, valorPadre,referencia): #Imprime distancia mínima por cada nodo y camino que debe de realizar
		print("Punto de Orígen y Dirección \t\tCosto Mínimo") 
		for i in range(0, len(distancia)): 
			print("\n\t  %d --> %d \t\t\t%.2f Km\n" % (referencia, i, distancia[i])), 
			#self.mostrarCamino(valorPadre,i) '''No se imprime correctamente, por corregir'''
		print("\n")
	def buscarCostoMin(self, matrizAdyacencia, referencia): 
		distancia = [float("Inf")] * len(matrizAdyacencia)  #Inicializar en ∞
		valorPadre = [-1] * len(matrizAdyacencia)  
		distancia[referencia] = 0
		cola = [] 
		for i in range(len(matrizAdyacencia)): 
			cola.append(i) 
		while cola: 
			c = self.distanciaMin(distancia,cola) 	 
			cola.remove(c) 
			for i in range(len(matrizAdyacencia[0])): 
				if matrizAdyacencia[c][i] and i in cola: 
					if distancia[c] + matrizAdyacencia[c][i] < distancia[i]: 
						distancia[i] = distancia[c] + matrizAdyacencia[c][i] 
						valorPadre[i] = c 
		self.imprimirFinal(distancia,valorPadre,referencia) 
objetoMatrizAdyacencia = FuncionesMatriz()
for i in range (len(matrizAdyacencia[0])):
    objetoMatrizAdyacencia.buscarCostoMin(matrizAdyacencia,i)
