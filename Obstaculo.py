from pygame import * 
import random

class ObstaculoClass:
    def __init__(self, x, img, ancho, alto, suelo):
        self.x = x
        self.img = img
        self.ancho = ancho
        self.alto = alto
        self.y = suelo - alto

    def actualizar(self, velocidadmovimiento, ventana):
        self.mover(velocidadmovimiento)
        self.mostrar(ventana)

    def mover(self, velocidadmovimiento):
        self.x = self.x - velocidadmovimiento

    def mostrar(self, ventana):
        ventana.blit(self.img, (self.x, self.y))

    def estaenpantalla(self):
        if self.x + self.ancho > 0:
            return True
        else:
            return False
