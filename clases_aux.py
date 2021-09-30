import pygame
import sys


class Cursor(pygame.Rect):                          # Hereda del modulo Rectangulo para tener sus atributos
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)          # constructor del rectangulo en (pos_x, pos_y, ancho, largo)

    # actualizar hace que el rectangulo se mueva tomando la posicion del mouse con mouse.get_pos()
    # left, top, son las posisciones x e y, correspondientes.
    def actualizar(self):
        self.left, self.top = pygame.mouse.get_pos()


class BotonSimple:
    def __init__(self, imagen, x, y):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.rect.left, self.rect.top = (x, y)
        
    def actualizar(self, ventana):
        ventana.blit(self.imagen, self.rect)


class BotonDoble(BotonSimple):
    def __init__(self, imagen, palabra, x, y):
        BotonSimple.__init__(self, imagen, x, y)
        self.palabra = palabra
        
    def actualizar(self, ventana, cursor):        
        if cursor.colliderect(self.rect):  # evalua si el rectangulo del cursor coliciona con el rectangulo del boton
            self.palabra.dibujar(ventana)
            
        ventana.blit(self.imagen, self.rect)


class Frases:
    def __init__(self, frase, tamanio, x, y):
        self.frase = frase
        self.tamanio = tamanio
        self.x = x
        self.y = y
        
    def dibujar(self, ventana):
        fuente = pygame.font.Font(None,self.tamanio)
        texto1 = fuente.render(self.frase,1,(0,0,0))
        ventana.blit(texto1,(self.x,self.y))


class Categoria:

    def __init__(self, categoria, ventana):
        self.categoria = categoria
        self.ventana = ventana
        self.correcto = 0
        self.incorrecto = 0
        self.indice = 0

    def getIndice(self):
        return self.indice

    def setIndice(self, indice):
        self.indice = indice

    def preguntar(self):
        self.ventana.fill((186,237,149))
        titulo = Frases(self.categoria[10:-4].upper(), 78, 350, 25)
        titulo.dibujar(self.ventana)
        archivo = open(self.categoria)
        self.lineas = archivo.readlines()  # Lista del todo el archivo de texto.
        a = pygame.image.load("Logos/A.jpg")
        b = pygame.image.load("Logos/B.jpg")
        c = pygame.image.load("Logos/C.jpg")
        self.boton_a = BotonSimple(a, 110, 525)
        self.boton_b = BotonSimple(b, 410, 525)
        self.boton_c = BotonSimple(c, 710, 525)
        self.boton_a.actualizar(self.ventana)
        self.boton_b.actualizar(self.ventana)
        self.boton_c.actualizar(self.ventana)
        pregunta = Frases(str(self.lineas[self.indice + 0][0:-1]), 40, 50, 250)
        if self.lineas[self.indice + 1][0] == "-":
            opcion1 = Frases(str(self.lineas[self.indice + 1][1:-1]), 25, 100, 500)
        else:
            opcion1 = Frases(str(self.lineas[self.indice + 1][0:-1]), 25, 100, 500)
        if self.lineas[self.indice + 2][0] == "-":
            opcion2 = Frases(str(self.lineas[self.indice + 2][1:-1]), 25, 400, 500)
        else:
            opcion2 = Frases(str(self.lineas[self.indice + 2][0:-1]), 25, 400, 500)
        if self.lineas[self.indice + 3][0] == "-":
            opcion3 = Frases(str(self.lineas[self.indice + 3][1:-1]), 25, 700, 500)
        else:
            opcion3 = Frases(str(self.lineas[self.indice + 3][0:-1]), 25, 700, 500)
        pregunta.dibujar(self.ventana)
        opcion1.dibujar(self.ventana)
        opcion2.dibujar(self.ventana)
        opcion3.dibujar(self.ventana)
    
    def cantPreguntas(self):
        archivo = open(self.categoria)
        return len(archivo.readlines())
    
    def evaluar(self, cursor, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and cursor.colliderect(self.boton_a):
            if self.lineas[self.indice + 1][0] == "-":
                self.correcto += 1
            else:
                self.incorrecto += 1
            return True
        if evento.type == pygame.MOUSEBUTTONDOWN and cursor.colliderect(self.boton_b):
            if self.lineas[self.indice + 2][0] == "-":
                self.correcto += 1
            else:
                self.incorrecto += 1
            return True
        if evento.type == pygame.MOUSEBUTTONDOWN and cursor.colliderect(self.boton_c):
            if self.lineas[self.indice + 3][0] == "-":
                self.correcto += 1
            else:
                self.incorrecto += 1
            return True
            
    def resultado(self):
        return self.correcto, self.incorrecto
