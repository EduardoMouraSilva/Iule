# Funcoes do jogo
import pygame as pg
from const import *


def movimento(event, iule):

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                iule.speedx -= SPEED_X
            elif event.key == pg.K_RIGHT:
                iule.speedx += SPEED_X
            elif event.key == pg.K_UP or event.key == pg.K_SPACE:
                iule.pulo()

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                iule.speedx += SPEED_X
            elif event.key == pg.K_RIGHT:
                iule.speedx -= SPEED_X



def sprites_no_grupo(mundo, sprites, blocks, solos_img, Solo):
    mundo = mundo
    sprites = sprites
    blocks = blocks
    for l, linhas in enumerate(mundo):
        cont = 0
        for c, linha in enumerate(linhas):
            if linha == '_':
                solo = Solo(solos_img[cont], l, c)
                sprites.add(solo)
                blocks.add(solo)
                cont += 1
                if cont > 2:
                    cont = 0

    return sprites, blocks
