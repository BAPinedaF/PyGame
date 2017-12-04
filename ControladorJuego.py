from pygame import * 
import sys
import random
import Obstaculo as o
import ControladorObstaculo as co
import Jugador as j

init()

ventanaX = 720
ventanaY = 360
reloj = time.Clock()
ventana = display.set_mode((ventanaX, ventanaY))
display.set_caption('Juego Salto!')
suelo = ventanaY - 70
gravedad = 1
jugador = j.JugadorClass(5, 6, 10)
controladorobstaculo = co.ControladorObstaculo(4, (45, 90))
sueloImg = transform.scale(image.load('suelo.png'), (ventanaX, int(ventanaY - suelo)))
fondo=image.load('background.png').convert_alpha()

font1 = font.Font('SFPixelate.ttf', 40)
font2 = font.Font('SFPixelate.ttf', 30)
deathMessage1 = font1.render('Juego Terminado!', True, (255, 255, 255))
deathMessage1Shadow = font1.render('Juego Terminado!', True, (0, 0, 0))
deathMessage2 = font2.render('Presione "Espacio"', True, (255, 255, 255))
deathMessage2Shadow = font2.render('Presione "Espacio"', True, (0, 0, 0))
message1Rect = deathMessage1.get_rect()
message1x = ventanaX / 2 - message1Rect.width / 2
message2Rect = deathMessage2.get_rect()
message2x = ventanaX / 2 - message2Rect.width / 2

score = 0


def mostrarmensaje(y):
    ventana.blit(deathMessage1, (message1x, y))
    ventana.blit(deathMessage1Shadow, (message1x + 5, y + 5))
    ventana.blit(deathMessage2, (message2x, y + message1Rect.height))
    ventana.blit(deathMessage2Shadow, (message2x, message1Rect.height + 5 + y))

def evaluarcomandos():
    for events in event.get():
        if events.type == KEYDOWN:
            if events.key == K_ESCAPE:
                quit()



def obtener_puntuacion_mas_alta():
    # Puntuación más alta por defecto
    puntuacion_mas_alta = 0
    # Intentemos leer la puntuación más alta desde un archivo
    try:
        archivo_puntuacion_mas_alta = open("high_score.txt", "r")
        puntuacion_mas_alta = int(archivo_puntuacion_mas_alta.read())
        archivo_puntuacion_mas_alta.close()
    except IOError:
        # Error al leer el archivo, no existe una puntuación más alta
        print("Aún no existe una puntuación más alta.")
 
    return puntuacion_mas_alta
 
def guardar_puntuacion_mas_alta(nueva_puntuacion_mas_alta):
    try:
        # Escribimos el archivo en disco
        archivo_puntuacion_mas_alta = open("high_score.txt", "w")
        archivo_puntuacion_mas_alta.write(str(nueva_puntuacion_mas_alta))
        archivo_puntuacion_mas_alta.close()
    except IOError:
        # Um, no puedo escribirlo.
        print("No soy capaz de guardar la puntuación alta.")




def principal(dificultad):
    score= 0
    jugador.actualizar(suelo, gravedad, controladorobstaculo, ventana, ventanaY)
    while True:
        if jugador.muerto:
            caer(scoreStr)
            break
        evaluarcomandos()
        #ventana.fill((200, 240, 250))
        ventana.blit(fondo,(0,0))
        jugador.actualizar(suelo, gravedad, controladorobstaculo, ventana, ventanaY)
        if dificultad == 1:
            controladorobstaculo.actualizar(1,True, score / 50 + 5, ventanaX, suelo, ventana)
        elif dificultad == 2:
            controladorobstaculo.actualizar(2,True, score / 10 + 10, ventanaX, suelo, ventana)
        ventana.blit(sueloImg, (0, suelo))
        reloj.tick(60)
        scoreStr = font2.render(str(round(score)), True, (0, 0, 0))
        ventana.blit(scoreStr, (50, 50))
        display.update()
        score = score + 0.1


        puntuacion_mas_alta = obtener_puntuacion_mas_alta()
    # Obtenemos la puntuación del juego en curso            
     
        # Observa por si tenemos una nueva puntuación más alta
        if score > puntuacion_mas_alta:
            # Conseguido! Guardamos en disco
            guardar_puntuacion_mas_alta(int(score))



def caer(scoreStr):
    space = 0
    while True:
        pressedKeys = key.get_pressed()
        oldSpace = space
        space = pressedKeys[K_SPACE]
        evaluarcomandos()
        #ventana.fill((200, 240, 250))
        ventana.blit(fondo,(0,0))
        jugador.actualizar(suelo, gravedad, controladorobstaculo, ventana, ventanaY)
        controladorobstaculo.actualizar(0,False, score / 50 + 3, ventanaX, suelo, ventana)
        ventana.blit(sueloImg, (0, suelo))
        reloj.tick(60)
        mostrarmensaje(50)
        ventana.blit(scoreStr, (50, 50))
        display.update()
        spaceEvent = space - oldSpace

        if spaceEvent == 1:
            #Reset Everything
            controladorobstaculo.obstaculoList = []
            jugador.velocityY = 0
            jugador.muerto = False
            jugador.y = suelo - jugador.alto
            break
#principal()



