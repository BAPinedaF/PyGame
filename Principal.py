import dumbmenu as dm
from pygame import * 
import ControladorJuego as j



while (True):
    # Just a few static variables
    red = 255, 0, 0
    green = 0, 255, 0
    blue = 0, 0, 255
    black = 0, 0, 0

    size = width, height = 720, 360	
    screen = display.set_mode(size)
    #screen.fill(black)
    fondo = image.load('background.png').convert_alpha()
    screen.blit(fondo, (0, 0))
    display.update()
    key.set_repeat(500, 30)

    choose = dm.dumbmenu(screen, [
                        'Comenzar juego', 
                        'Puntaje más alto', 
                        'Salir del juego'], 64, 64, None, 32, 1.4, black, red)


    if choose == 0:
        print("Seleccionar dificultad")
        size = width, height = 720, 360 
        screen = display.set_mode(size)
        #screen.fill(black)
        fondo = image.load('background.png').convert_alpha()
        screen.blit(fondo, (0, 0))
        display.update()
        key.set_repeat(500, 30)
        chooseD = dm.dumbmenu(screen, [
                        'Fácil', 
                        'Avanzado', 
                        'Volver'], 64, 64, None, 32, 1.4, black, red)
        if chooseD == 0:
            j.principal(1); 
        elif chooseD == 1:
            j.principal(2); 
    elif choose == 1:
        size = width, height = 720, 360 
        screen = display.set_mode(size)
        #screen.fill(black)
        fondo = image.load('background.png').convert_alpha()
        screen.blit(fondo, (0, 0))
        display.update()
        key.set_repeat(500, 30)
        chooseH = dm.dumbmenu(screen, [
                        str(j.obtener_puntuacion_mas_alta()), 
                        'Volver'], 64, 64, None, 32, 1.4, black, red)
        print ("You choose 'Show Highscore'.", j.obtener_puntuacion_mas_alta())
    elif choose == 2:
        print ("You choose 'Quit Game'.")
        exit()
        break
