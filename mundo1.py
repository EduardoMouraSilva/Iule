# Esta é a class do iule.

import sys
from random import randint
import pygame as pg
from classes import Personagem, Solo, InimigoE, Fireball
from funcoes import movimento, sprites_no_grupo
from const import *
from map_mundos import mundo1

mundo = mundo1
pg.init()

# Configurações da tela.
tela = pg.display.set_mode((LARGURA, ALTURA))
pg.display.set_caption('Iule')
pg.display.set_icon(image_iule)
contador = pg.time.Clock()

# Colocando os sprites nos groups
sprites = pg.sprite.Group()
blocks = pg.sprite.Group()
bolas = pg.sprite.Group()
inimigos = pg.sprite.Group()

sprites, blocks = sprites_no_grupo(mundo, sprites, blocks, solo_img, Solo)

for i in range(6):
    a = randint(5, 18)
    b = randint(5, 30)
    inimigo = InimigoE(image_inimigo, a, b, blocks, bolas)
    sprites.add(inimigo)
    inimigos.add(inimigo)
iule = Personagem(image_personagem, 8, 2, blocks, inimigos)
sprites.add(iule)

# Música
musica = pg.mixer.Sound('sound/level_1.mp3')
musica.play()
musica.set_volume(0.5)
musica_fogo = pg.mixer.Sound('sound/foom_0.mp3')

# Textos
pg.font.init()
vid = pg.font.SysFont(font1, 20)
vida = vid.render('VIDAS: 3', 1, PRETO)
vidas = 3
cont = 10
continuar = True

energias = iule.energia
energia = vid.render(f'ENERGIAS: {energias}', 1, PRETO)

pontos = 1000
ponto = vid.render(f'PONTOS: {pontos}', 1, PRETO)

while continuar:
    contador.tick(10)
    tela.fill(AZUL_CELES)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
        movimento(event, iule)

        if event.type == pg.KEYDOWN:
            musica.stop()
            if event.key == pg.K_a:
                iule.bolafogo(image_bola, pg.K_a, sprites, bolas)
                energias = iule.energia
                if energias == 0:
                    cor = RED
                else:
                    cor = PRETO
                energia = vid.render(f'ENERGIAS: {energias}', 1, cor)

    if pg.key.get_pressed()[pg.K_LEFT] or pg.key.get_pressed()[pg.K_RIGHT]:
        if pg.key.get_pressed()[pg.K_LEFT]:
            tecla = pg.K_LEFT
        elif pg.key.get_pressed()[pg.K_RIGHT]:
            tecla = pg.K_RIGHT
        elif pg.key.get_pressed()[pg.K_LEFT] and pg.key.get_pressed()[pg.K_RIGHT]:
            continue
        iule.sprites_jogo(tecla)

    if vidas != iule.vida:
        vida = iule.vidas(iule.vida)
        vidas = iule.vida
        if vidas == 0:
            continuar = False

    if pontos != 0:
        pontos = int(pontos - 0.05)
        ponto = vid.render(f'PONTOS: {pontos}', 1, PRETO)
        


    if len(inimigos) == 0:
        for i in range(cont):
            a = randint(5, 18)
            b = randint(5, 30)
            inimigo = InimigoE(image_inimigo, a, b, blocks, bolas)
            sprites.add(inimigo)
            inimigos.add(inimigo)

    sprites.update()
    tela.blit(fundo, (0, 0))
    tela.blit(vida, (LARGURA-150, 10))
    tela.blit(energia, (LARGURA-150, 30))
    tela.blit(ponto, (LARGURA-150, 50))
    sprites.draw(tela)
    

    pg.display.flip()
