# Class base para o personagem
import pygame as pg
from const import *



class Solo(pg.sprite.Sprite):
    def __init__(self, image, linha, coluna):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = BLOCO * coluna
        self.rect.y = BLOCO * linha



class Personagem(pg.sprite.Sprite):
    def __init__(self, image, linha, coluna, blocks):
        pg.sprite.Sprite.__init__(self)
        self.estado = PARADO

        img = image
        img_a = pg.Surface.get_height(img)
        self.images = []
        for i in range(4, 8):
            ims = img.subsurface((img_a*i, 0, img_a, img_a))
            self.images.append(ims)

        self.atual = 0
        self.image = self.images[self.atual]
            
        self.rect = self.image.get_rect()

        self.blocks = blocks

        self.rect.x = coluna * BLOCO
        self.rect.bottom = linha * BLOCO

        self.speedx = 0
        self.speedy = 0

    def update(self):
        if self.speedy < 50:
            self.speedy += GRAVIDADE

        if self.speedy > 0:
            self.estado = CAINDO
        self.rect.y += self.speedy

        speedx = 0


        colidius = pg.sprite.spritecollide(self, self.blocks, False)
        for colidiu in colidius:
            if self.speedy > 0:
                self.rect.bottom = colidiu.rect.top
                self.speedy = 0
                self.estado = PARADO
            elif self.speedy < 0:
                self.rect.top = colidiu.rect.bottom
                self.speedy = 0
                self.estado = PARADO

        if self.estado != PARADO and self.speedx:
            speedx = self.speedx
            self.speedx = 0
            self.speedx = speedx + speedx

        print(self.speedx, self.speedy)

        # para x
        self.rect.x += self.speedx
        
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= LARGURA:
            self.rect.right = LARGURA - 1

        colidius = pg.sprite.spritecollide(self, self.blocks, False)
        for colidiu in colidius:
            if self.speedx > 0:
                self.rect.right = colidiu.rect.left
            elif self.speedx < 0:
                self.rect.left = colidiu.rect.right

        if speedx:
            self.speedx = speedx

    def pulo(self):
        if self.estado == PARADO:
            self.speedy -= PULO_SIZE
            self.estado = PULANDO
            
    def sprites_jogo(self, tecla):
        if tecla != pg.K_LEFT and tecla != pg.K_RIGHT:
            return
        self.atual += 1
        if tecla == pg.K_LEFT:
            if self.atual >= 2:
                self.atual = 0
        if tecla == pg.K_RIGHT:
            if self.atual < 2 or self.atual >= 4:
                self.atual = 2
        if self.atual >= 4:
            self.atual = 0

        self.image = self.images[int(self.atual)]

