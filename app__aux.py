from clases_aux import *
import pygame

pygame.init()
ventana = pygame.display.set_mode((1000,600))

cursor = Cursor()                                   # se crea un rectangulo que sigue la punta del mouse
titulo = Frases("Seleccione una categoria.",48,300,35)
deporte = pygame.image.load("Logos/deporte.png")
geografia = pygame.image.load("Logos/geografia.png")
historia = pygame.image.load("Logos/historia.png")
entretenimiento = pygame.image.load("Logos/entretenimiento.png")
pald = Frases("DEPORTE",58,400,200)
palg = Frases("GEOGRAFIA",58,400,200)
palh = Frases("HISTORIA",58,400,200)
pale = Frases("ENTRETENIMIENTO",58,400,200)
boton_deporte = BotonDoble(deporte,pald,100,400)
boton_geografia = BotonDoble(geografia,palg,300,400)
boton_historia = BotonDoble(historia,palh,500,400)
boton_entretenimiento = BotonDoble(entretenimiento,pale,700,400)
celeste = (149,208,237)

while True:
    jugando = False
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if cursor.colliderect(boton_deporte):
                jugando = True
                cat = "Preguntas/deporte.txt"
            if cursor.colliderect(boton_geografia):
                jugando = True
                cat = "Preguntas/geografia.txt"
            if cursor.colliderect(boton_historia):
                jugando = True
                cat = "Preguntas/historia.txt"
            if cursor.colliderect(boton_entretenimiento):
                jugando = True
                cat = "Preguntas/entretenimiento.txt"
    if jugando:
        rta = True
        respondio = False
        pregunta = Categoria(cat, ventana)
        cant_lineas = pregunta.cantPreguntas()
        indice = 0
        fin = Frases("FIN", 78, 450, 50)
        while rta:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
                if indice < cant_lineas and pregunta.resultado()[0] < 5:
                    cursor.actualizar()
                    pregunta.preguntar()
                    respondio = pregunta.evaluar(cursor, evento)
                    pygame.display.update()
                    if respondio:
                        indice += 4
                        pregunta.setIndice(indice)
                else:
                    ventana.fill(celeste)
                    correctos = Frases("Correctas: "+str(pregunta.resultado()[0]), 78, 150, 200)
                    incorrectos = Frases("Incorrectas: "+str(pregunta.resultado()[1]), 78, 550, 200)
                    correctos.dibujar(ventana)
                    incorrectos.dibujar(ventana)
                    fin.dibujar(ventana)
                    pygame.display.update()
    cursor.actualizar()
    ventana.fill(celeste)
    boton_deporte.actualizar(ventana, cursor)
    boton_geografia.actualizar(ventana, cursor)
    boton_historia.actualizar(ventana, cursor)
    boton_entretenimiento.actualizar(ventana, cursor)
    titulo.dibujar(ventana)
    pygame.display.update()
