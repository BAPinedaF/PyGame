from pygame import * 
import random
import Obstaculo as h

class ControladorObstaculo:
    
    controladoraparicion = 0

    def __init__(self, escala, rangoaparicion):
        self.img = transform.scale(image.load('obstaculo.png'), (7 * escala, 15 * escala))
        self.rangoaparicion = rangoaparicion
        self.obstaculoList = []
        self.escala = escala

    def actualizar(self, dificultad,aparecer, velocidadmovimiento, ventanaX, suelo, ventana):
        if aparecer:
            if dificultad == 2:
                self.cambioescala()
                self.img = transform.scale(image.load('obstaculo.png'), (7 * self.escala, 15 * self.escala))
            self.agregar(ventanaX, suelo)
        self.controlar(velocidadmovimiento, ventana)

    def controlar(self, velocidadmovimiento, ventana):
        obstaculos2 = []
        for obstaculo in self.obstaculoList:
            obstaculo.actualizar(velocidadmovimiento, ventana)

            if obstaculo.estaenpantalla():
                obstaculos2.append(obstaculo)

        self.obstaculoList = obstaculos2

    def agregar(self, ventanaX, suelo):
        if self.controladoraparicion >= self.rangoaparicion[1]:
            newobstaculo = h.ObstaculoClass(ventanaX, self.img, 7 * self.escala, 15 * self.escala, suelo)
            self.obstaculoList.append(newobstaculo)
            self.controladoraparicion = 0

        elif self.controladoraparicion > self.rangoaparicion[0]:
            if random.randint(0, self.rangoaparicion[1] - self.rangoaparicion[0]) == 0:
                newobstaculo = h.ObstaculoClass(ventanaX, self.img, 7 * self.escala, 15 * self.escala, suelo)
                self.obstaculoList.append(newobstaculo)
                self.controladoraparicion = 0

        self.controladoraparicion = self.controladoraparicion + 1

    def cambioescala(self):
        self.escala=round(random.uniform(3,5))
