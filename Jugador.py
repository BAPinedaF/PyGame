from pygame import * 
import sys
import random

class JugadorClass:
    
    muerto = False
    x = 100
    y = 100
    velocidadY = 0
    momento = 0

    def __init__(self, escala, cambioimagen, terminalVelocity):
        self.run1 = transform.scale(image.load('run2.png'), (7 * escala, 14 * escala))
        self.run2 = transform.scale(image.load('run3.png'), (7 * escala, 14 * escala))
        self.run3 = transform.scale(image.load('run4.png'), (7 * escala, 14 * escala))
        self.run4 = transform.scale(image.load('run5.png'), (7 * escala, 14 * escala))
        '''self.run5 = transform.scale(image.load('run6.png'), (7 * escala, 14 * escala))'''
        self.escala = escala
        self.cambioimagen = cambioimagen
        self.terminalVelocity = terminalVelocity
        self.alto = 14 * escala
        self.ancho = 7 * escala

    def actualizar(self, suelo, gravedad, ControladorObstaculo, ventana, ventanaY):
        self.fisica(suelo, gravedad, ventanaY)

        if self.colisionobstaculo(ControladorObstaculo):
            self.muerto = True

        if not self.muerto:
            self.comandosjugador(suelo, gravedad)

        self.y = self.y + self.velocidadY
        self.mostrar(ventana)

    def colisionobstaculo(self, ControladorObstaculo):
        for obstaculo in ControladorObstaculo.obstaculoList:
            if self.x + self.ancho > obstaculo.x:
                if self.x < obstaculo.x + (obstaculo.ancho - 2*self.ancho/7):
                    if self.y + self.alto > obstaculo.y:
                        return True

    def comandosjugador(self, suelo, gravedad):
        pressedKeys = key.get_pressed()

        if pressedKeys[K_a]:
            sys.exit()
        if pressedKeys[K_SPACE]:
            if self.y + self.alto == suelo:
                self.velocidadY = self.velocidadY - 10
            else:
                self.velocidadY = self.velocidadY - gravedad / 2

    def fisica(self, suelo, gravedad, ventanaY):
        if self.muerto:
            if self.y < ventanaY:
                self.velocidadY = self.velocidadY + 1
        elif self.y + self.alto < suelo:
            if self.velocidadY < self.terminalVelocity:
                self.velocidadY = self.velocidadY + gravedad
        elif self.velocidadY > 0:
            self.velocidadY = 0
            self.y = suelo - self.alto

    def mostrar(self, ventana):
        if self.momento <= self.cambioimagen:
            img = self.run1
        elif self.momento <= self.cambioimagen * 2:
            img = self.run2
        elif self.momento <= self.cambioimagen * 3:
            img = self.run3
        else:
            img = self.run4
            
        self.momento = self.momento + 1

        if self.momento >= self.cambioimagen * 5:
            self.momento = 0

        ventana.blit(img, (self.x, self.y))
