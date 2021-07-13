# A janela de ganhador
import sys
import os
import pygame as pg
from const import *


tela = pg.display.set_mode((400, 200))
pg.display.set_caption('Ganhou')
pg.display.set_icon(image_iule)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    tela.blit(fundo, (0, 0))

    pg.display.flip()

    
