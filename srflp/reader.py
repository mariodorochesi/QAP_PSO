import sys
import numpy as np

''''
    @author : Mario Dorochesi Ollino
    @date   : 09-01-2019
    
    Clase de utilidad que permite leer un archivo del problema segun el formato
    entregado por los profesores.
    
    Ademas incorpora un metodo que permite calcular la distancia dada una solucion
    tentativa como parametro.
'''


class SRFLP:

    def __init__(self, file_name):
        ''''
            @:param file_name : Nombre del archivo que se desea leer
        '''
        try:
            archivo = open(file_name , 'r')
            # Se lee el tamano de la instancia, y se asigna al atributo tamano_instancia
            self.tamano_instancia = int(archivo.readline())
            # Se lee la primera linea del archivo y se asigna al atribuo arreglo_tamanos como un arreglo de enteros
            self.arreglo_tamanos = np.array([int(x) for x in archivo.readline().strip().split(',')])
            # Se asigna una lista auxiliar donde se cargaran las filas de la matriz de pesos
            lista_pesos = []
            for linea in archivo:
                lista_pesos.append([int(x) for x in linea.strip().split(',')])
            # Se genera un arreglo multidimensional a partir de la lista auxiliar previamente creada
            self.matriz_pesos = np.array(lista_pesos)
            del lista_pesos
        except :
            print('Ha ocurrido un problema leyendo el archivo')
            sys.exit(1)


    def calcular_costo(self, solucion_parcial):
        ''''
            Calcula el Costo en bae a la formula presentada en el enunciado del problema.
        '''
        total = 0
        for i in range(0, len(solucion_parcial)-1):
            total_medio = 0
            for j in range(i+1, len(solucion_parcial)):
                total_medio = self.arreglo_tamanos[solucion_parcial[i]] + self.arreglo_tamanos[solucion_parcial[j]]
                for k in range(i+1,j-1):
                    total_medio = total_medio + self.arreglo_tamanos[solucion_parcial[i]]
                total = total + total_medio * self.matriz_pesos[solucion_parcial[i]][solucion_parcial[j]]
        return total
