# O arquivo principal do jogo Iule. Aquele que deve ser aberto primeiro.
# Criado por Eduardo de Moura Silva.
# eduardobrmasd@gmail.com

import sys
import os
from time import sleep
import pygame
from const import *



pygame.init()
# Configurações da tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Iule')
image_iule = pygame.image.load('image/iule.png')
pygame.display.set_icon(image_iule)
tela.fill(BRANCO)

# Os textos
pygame.font.init()
pequen = pygame.font.SysFont(font2, 15)
versa = pequen.render('V:1.0.0', 1, PRETO)
nom_jogo = pygame.font.SysFont(font1, 60)
nome_jogo = nom_jogo.render('IULE', 1, PRETO)
jog = pygame.font.SysFont(font1, 20)
jogarb = jog.render('JOGAR', 1, BRANCO)

# Surface
posx_j = 140
posy_j = 70
jogar = pygame.Surface((posx_j, posy_j))
posx_s = LARGURA/2 - posx_j/2
posy_s = ALTURA/2 - posy_j/2

temporizador = pygame.time.Clock()

# Música
pygame.mixer.init()
abertura_m = pygame.mixer.Sound('sound/Title_Screen.mp3')
abertura_m.play(loops=-1, fade_ms=4)

fundo = pygame.image.load('image/BG.png')

continuar = True

while continuar:
    tela.fill(BRANCO)
    jogar.fill(AZUL_M)
    posx, posy = pygame.mouse.get_pos()
    temporizador.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if posx >= posx_s and posx <= (posx_s + posx_j):
        if posy > posy_s and posy <= (posy_s + posy_j):
            if event.type == pygame.MOUSEBUTTONDOWN:
                os.startfile('mundo1.py')
                abertura_m.stop()
                continuar = False
                sleep(2)


    tela.blit(fundo, (0, 0))
    
    tela.blit(versa, (10, ALTURA-10))
    tela.blit(nome_jogo, (LARGURA/2 - 70, 50))
    tela.blit(jogar, (posx_s, posy_s))
    tela.blit(jogarb, (LARGURA/2 - posx_j/4, ALTURA/2 - posy_j/5))
    
    pygame.display.flip()

print('fim')
