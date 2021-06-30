# Arquivo de constates

import pygame as pg
pg.init()

# Tela
ALTURA = 640
LARGURA = 992

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL_M = (0, 100, 200)
AZUL_CELES = (25, 230, 255)
RED = (255, 0, 0)

# Fontes
font1 = 'verdana'
font2 = 'Times New Roma'

pg.font.init()
vid = pg.font.SysFont(font1, 20)
vida = vid.render('VIDAS: 3', 1, PRETO)

# # # #
GRAVIDADE = 5
PULO_SIZE = 30
SPEED_X = 5
BLOCO = 32


# Estados do personagem
PARADO = 0
PULANDO = 1
CAINDO = 2

# Imagens
image_iule = pg.image.load('image/iule.png')
solo_img = pg.image.load('image/blocks_prev.png')
image_personagem = pg.image.load('image/iule_8x1_32x32.png')
image_bola = pg.image.load('image/fireball.bmp')
image_inimigo = pg.image.load('image/tin.png')
fundo = pg.image.load('image/BG.png')

# Sons
musica_fogo = pg.mixer.Sound('sound/foom_0.mp3')
monstro_morre = pg.mixer.Sound('sound/deathd.mp3')
pulo_som = pg.mixer.Sound('sound/jump_03.mp3')

