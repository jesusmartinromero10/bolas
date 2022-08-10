from random import randint
import pygame as pg


class Cuadrado:
    def __init__(self, x, y, w = 25, h = 25, color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

        self.vx = 0
        self.vy = 0

    def velocidad(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def mover(self, xmax, ymax):
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= xmax - self.w:
            self.vx *= -1
        
        if self.y <= 0 or self.y >= ymax - self.h:
            self.vy *= -1

        

pg.init()

pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("Bolitas rebotando")


bolas = 0
cuadradi = []
while bolas <= randint(3, 1000):
    cuadrao = Cuadrado(400, 300, color= (randint(0, 255), randint(0, 255), randint(0, 255)))
    cuadrao.velocidad(randint(-10, 10), randint(-10, 10))
    cuadradi.append(cuadrao)
    
    bolas += 1

#cuadrado = Cuadrado(400, 300, color = (255, 255, 0))
#cuadrado.velocidad(5, 5)
#cuadrado2 = Cuadrado(300, 300, 35, 35, (0, 255, 0))
#cuadrado2.velocidad(randint(-10, 10), randint(-10, 10))
#for h in range(len(cuadradi)):
 #   cuadradi[h].velocidad(randint(-10, 10), randint(-10, 10))

game_over = False
while not game_over:
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0, 0, 255))
    #cuadrado.mover(800, 600)
    #cuadrado2.mover(800, 600)
    for a in range(len(cuadradi)):
        cuadradi[a].mover(800, 600)
    
    
    #pg.draw.rect(pantalla_principal, cuadrado.color, (cuadrado.x, cuadrado.y, cuadrado.w, cuadrado.h))
    #pg.draw.rect(pantalla_principal, cuadrado2.color, (cuadrado2.x, cuadrado2.y, cuadrado2.w, cuadrado2.h))
    for i in range(len(cuadradi)):
        pg.draw.rect(pantalla_principal, cuadradi[i].color, (cuadradi[i].x, cuadradi[i].y, cuadradi[i].w, cuadradi[i].h))
    pg.display.flip()

pg.quit()

