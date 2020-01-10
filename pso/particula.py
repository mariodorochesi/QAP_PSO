import random
import numpy as np
import math

''''
    @author : Mario Dorochesi Ollino
    @date   : 09-01-2019
    
    Clase que contiene la información, y comportamiento de una 
    particula del enjambre.
    e537c28ce659274c37335cc911d089f2
'''

class Particula:

    def __init__(self, diccionario_particulas, arreglo_original):
        # Arreglo que representa la solucion actual de la particula
        self.solucion_tentativa =np.copy(arreglo_original)
        # Arreglo que representa la velocidad actual de la particula
        self.velocidad = np.zeros(len(arreglo_original))
        # Arreglo que representa la mejor posicion alcanzada por la particula
        self.mejor_posicion_personal = np.zeros(len(arreglo_original))
        # Fitness de la particula
        self.particle_fitness = math.inf

        # Coeficientes de impacto
        self.c1 = 1
        self.c2 = 1
        self.velocidad_maxima = 100

        random.shuffle(self.solucion_tentativa)
        while diccionario_particulas.get(self.generar_identificador(),None) is not None:
            random.shuffle(self.solucion_tentativa)
        diccionario_particulas[self.generar_identificador()] = self.solucion_tentativa

    def generar_identificador(self):
        id = ''
        for i in range(0, len(self.solucion_tentativa)):
            id = id + str(self.solucion_tentativa[i])
        return id

    def actualizar_velocidad(self, mejor_posicion_global):
        for i in range(0, len(self.velocidad)):
            velocidad_parcial = self.velocidad[i] + random.random() * self.c1 * (self.mejor_posicion_personal[i] - self.solucion_tentativa[i]) + random.random() * self.c2 * (mejor_posicion_global[i] - self.solucion_tentativa[i])
            if abs(velocidad_parcial) <= self.velocidad_maxima:
                self.velocidad[i] = velocidad_parcial
        #print(self.velocidad)
    def actualizar_posicion(self):
        for i in range(0, len(self.solucion_tentativa)):
            if random.random() < float(self.velocidad[i])/100.0:
                if int(self.velocidad[i]) > 0 and i  < len(self.solucion_tentativa)-1:
                    aux = self.solucion_tentativa[i]
                    self.solucion_tentativa[i] = self.solucion_tentativa[i+1]
                    self.solucion_tentativa[i+1] = aux
                    velocidad_aux = self.velocidad[i]
                    self.velocidad[i] = self.velocidad[i+1]
                    self.velocidad[i+1] = velocidad_aux
                elif int(self.velocidad[i]) < 0 and i > 0:
                    aux = self.solucion_tentativa[i]
                    self.solucion_tentativa[i] = self.solucion_tentativa[i-1]
                    self.solucion_tentativa[i-1] = aux
                    velocidad_aux = self.velocidad[i]
                    self.velocidad[i] = self.velocidad[i-1]
                    self.velocidad[i-1] = velocidad_aux

    def actualizar_mejor_personal(self, fitness):
        if fitness < self.particle_fitness:
            self.particle_fitness = fitness
            self.mejor_posicion_personal = self.solucion_tentativa