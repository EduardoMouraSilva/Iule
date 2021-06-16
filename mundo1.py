# Esta é a class do iule.

import sys
import pygame as pg
from classes import Personagem, Solo
from funcoes import movimento, sprites_no_grupo
from const import *
from map_mundos import mundo1

mundo = mundo1
pg.init()

# Configurações da tela.
tela = pg.display.set_mode((LARGURA, ALTURA))
pg.display.set_caption('Iule')
image_iule = pg.image.load('image/iule.png')
pg.display.set_icon(image_iule)

contador = pg.time.Clock()

# O superficie
sprites = pg.sprite.Group()
blocks = pg.sprite.Group()

solo_img = pg.image.load('image/blocks_prev.png').convert_alpha()

solos_img = []
for i in range(3):
    solo = solo_img.subsurface(32*i, 0, 32, 32)
    solos_img.append(solo)

sprites, blocks = sprites_no_grupo(mundo, sprites, blocks, solos_img, Solo)

# Colocar o Iule na tela, instanciando ele.
image_p = pg.image.load('image/iule_8x1_32x32.png')

iule = Personagem(image_p, 8, 2, blocks)
sprites.add(iule)

# Música
musica = pg.mixer.Sound('sons/level_1.mp3')
musica.play(loops=-1)
musica.set_volume(0.5)

fundo = pg.image.load('image/BG.png')

while True:
    contador.tick(10)
    tela.fill(AZUL_CELES)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        movimento(event, iule)

    if pg.key.get_pressed()[pg.K_LEFT] or pg.key.get_pressed()[pg.K_RIGHT]:
        if pg.key.get_pressed()[pg.K_LEFT]:
            tecla = pg.K_LEFT
        elif pg.key.get_pressed()[pg.K_RIGHT]:
            tecla = pg.K_RIGHT
        elif pg.key.get_pressed()[pg.K_LEFT] and pg.key.get_pressed()[pg.K_RIGHT]:
            continue
        iule.sprites_jogo(tecla)

    sprites.update()
    tela.blit(fundo, (0, 0))
    sprites.draw(tela)

    pg.display.flip()
