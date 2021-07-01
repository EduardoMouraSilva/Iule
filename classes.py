# Class base para o personagem
from random import randint
import pygame as pg
from const import *




class Solo(pg.sprite.Sprite):
    def __init__(self, image, linha, coluna):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = BLOCO * coluna
        self.rect.y = BLOCO * linha



class Fireball(pg.sprite.Sprite):
    def __init__(self, image, rect_x, rect_bottom, rumo):
        pg.sprite.Sprite.__init__(self)

        imgs = image
        self.images = []
        for i in range(5):
            img = imgs.subsurface((0, 12*i, 7, 12))
            if rumo < 0:
                img = pg.transform.rotate(img, -180)
            img.set_colorkey((0, 0, 0))
            self.images.append(img)
        self.atual = 0
        self.image = self.images[self.atual]

        self.rect = self.image.get_rect()

        self.direcao(rect_x, rect_bottom, rumo)

    def update(self):
        self.rect.x += self.speedx

        self.atual += 0.25
        if self.atual > 4:
            self.atual = 1
        self.image = self.images[int(self.atual)]

        if self.speedx > 0 and self.rect.x > LARGURA:
            pg.sprite.Sprite.kill(self)
        elif self.speedx < 0 and self.rect.x < 0:
            pg.sprite.Sprite.kill(self)

    def direcao(self, rect_x, rect_bottom, rumo):

        if rumo < 0:
            self.speedx = -20
        else:
            self.speedx = 20

        self.rect.x = rect_x
        self.rect.bottom = rect_bottom -5



class Personagem(pg.sprite.Sprite):
    def __init__(self, image, linha, coluna, blocks, inimigos, fruta):
        pg.sprite.Sprite.__init__(self)
        self.estado = PARADO

        img = image
        img_a = pg.Surface.get_height(img)
        self.images = []
        for i in range(4, 8):
            ims = img.subsurface((img_a*i, 0, img_a-2, img_a-2))
            self.images.append(ims)

        self.atual = 2
        self.image = self.images[self.atual]
            
        self.rect = self.image.get_rect()

        self.blocks = blocks
        self.inimigos = inimigos
        self.fruta = fruta

        self.rect.x = coluna * BLOCO
        self.rect.bottom = linha * BLOCO

        self.speedx = 0
        self.speedy = 0

        self.rumo = 1
        self.lancou = 0

        self.vida = 3
        self.vidas_text = ['VIDAS: 0', 'VIDAS: 1', 'VIDAS: 2']

        self.energia = 5

        self.colidiu_fruta = False

    def update(self):

        colidiu_ini = pg.sprite.spritecollide(self, self.inimigos, False)
        for coli_ini in colidiu_ini:
            self.vida -= 1
            pg.sprite.Sprite.kill(coli_ini)

        colidiu_frutas = pg.sprite.spritecollide(self, self.fruta, False)
        for colidiu_fruta in colidiu_frutas:
            pg.sprite.Sprite.kill(colidiu_fruta)
            self.energia += 1
            self.colidiu_fruta = True

        if self.speedy < 50:
            self.speedy += GRAVIDADE

        if self.speedx != 0:
            if self.speedx > 0:
                self.rumo = 1
            else:
                self.rumo = -1
    
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
        if self.lancou:
            if self.lancou < 0:
                self.speedx += SPEED_X
            else:
                self.speedx -= SPEED_X
            self.lancou = 0

    def pulo(self):
        if self.estado == PARADO:
            self.speedy -= PULO_SIZE
            self.estado = PULANDO
        pulo_som.play()
        
            
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

    def bolafogo(self, image_bola, tecla, sprites, bolas):
        if self.energia <= 0:
            return
        if self.rumo > 0:
            pos = self.rect.x
            self.atual = 2
        else:
            pos = self.rect.right -5
            self.atual = 0

        if self.speedx != 0:
            if self.speedx > 0:
                self.speedx -= SPEED_X
                self.lancou = -1
            else:
                self.speedx += SPEED_X
                self.lancou = 1

        if tecla == pg.K_a:
            bola = Fireball(image_bola, pos,
                            self.rect.bottom, self.rumo)
        sprites.add(bola)
        bolas.add(bola)
        self.image = self.images[self.atual]
        musica_fogo.play()

        self.energia -= 1

    def vidas(self, vidas):
        vida = vid.render(self.vidas_text[self.vida], 1, PRETO)
        print(self.vida)

        return vida



class InimigoE(pg.sprite.Sprite):
    def __init__(self, image, linha, coluna, blocks, bolas):
        pg.sprite.Sprite.__init__(self)
        self.estado = PARADO

        img = image
        self.images = []
        for i in range(1, 3):
            for e in range(3):
                imgs = img.subsurface((e * 32, i * 32), (BLOCO, BLOCO))
                self.images.append(imgs)
        
        self.atual = 0
        self.image = self.images[self.atual]

        self.blocks = blocks
        self.bolas = bolas

        self.rect = self.image.get_rect()

        self.rect.x = coluna * BLOCO
        self.rect.bottom = linha * BLOCO

        self.speedy = 0
        self.speedx = 1

    def update(self):
        if self.speedy < 50:
            self.speedy += GRAVIDADE

        if self.speedy > 0:
            self.estado = CAINDO
        self.rect.y += self.speedy

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

        # para x
        self.rect.x += self.speedx
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = 1
        elif self.rect.right >= LARGURA:
            self.rect.right = LARGURA - 1
            self.speedx = -1

        colidius = pg.sprite.spritecollide(self, self.blocks, False)
        for colidiu in colidius:
            if self.speedx > 0:
                self.rect.right = colidiu.rect.left
            elif self.speedx < 0:
                self.rect.left = colidiu.rect.right


        colidius_b = pg.sprite.spritecollide(self, self.bolas, False)
        for coli_b in colidius_b:
            pg.sprite.Sprite.kill(self)
            pg.sprite.Sprite.kill(coli_b)
            musica_fogo.stop()
            monstro_morre.play()
            

        self.atual += 1
        if self.speedx < 0:
            if self.atual >= 3:
                self.atual = 0
        if self.speedx > 0:
            if self.atual < 3 or self.atual >= 6:
                self.atual = 3
        if self.atual >= 6:
            self.atual = 0

        self.image = self.images[int(self.atual)]



class Fruta(pg.sprite.Sprite):
    def __init__(self, image, linha, coluna, blocks):
        pg.sprite.Sprite.__init__(self)
        self.estado = PARADO
        
        img = image
        a = randint(0, 3)
        b = randint(0, 3)
        self.image = img.subsurface((a *16, b*16), (16, 16))

        self.rect = self.image.get_rect()
        self.rect.x = coluna * 16
        self.rect.bottom = linha * 16

        self.blocks = blocks

        self.speedy = 0

    def update(self):
        if self.speedy < 50:
            self.speedy += GRAVIDADE

        if self.speedy > 0:
            self.estado = CAINDO
        self.rect.y += self.speedy

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
