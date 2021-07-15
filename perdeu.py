# A janela de perdedor
import sys
import os
import pygame as pg
from const import *

largura = 400
altura = 200
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Ganhou')
pg.display.set_icon(image_iule)

ganhou = gan.render('Você perdeu!!!!!', 1, PRETO)

lar = 80
alt = 40
menu = pg.Surface((lar, alt))
menu_text = vid.render('Menu', 1, PRETO)
m_x = largura/4
m_y = altura/2

sair = pg.Surface((lar, alt))
sair_text = vid.render('Sair', 1, PRETO)
s_x = largura/1.7
s_y = m_y

continuar = True
while continuar:
    menu.fill(AZUL_M)
    sair.fill(LARANJA)
    pos_x, pos_y = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


    if event.type == pg.MOUSEBUTTONDOWN:
        if pos_x >= m_x and pos_x <= (m_x + lar):
            if pos_y >= m_y and pos_y <= (m_y + alt):
                continuar = False
                os.startfile('principal.py')

        if pos_x >= s_x and pos_x <= (s_x + lar):
            if pos_y >= s_y and pos_y <= (s_y + alt):
                continuar = False
    

    tela.blit(fundo, (0, 0))
    tela.blit(ganhou, (35, altura/7))
    tela.blit(menu, (m_x, m_y))
    tela.blit(menu_text, (m_x+(lar/5), m_y+(alt/5)))
    tela.blit(sair, (s_x, s_y))
    tela.blit(sair_text, (s_x+(lar/5), s_y+(alt/5)))

    pg.display.flip()
