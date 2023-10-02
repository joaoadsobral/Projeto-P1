import pygame
from pygame.locals import *
import pygame.mask

relogio = pygame.time.Clock()

### Baixar os Sprites correndo, pulo, deslize
sprite_sheet = pygame.image.load('Sprites/Movimentação - Personagem/spritesheet.png')
sprite_sheetSlide = pygame.image.load('Sprites/Movimentação - Personagem/spritesheetDeslizando.png')
sprite_sheetPulo = pygame.image.load('Sprites/Movimentação - Personagem/spritesheetPulo.png')


class Personagem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        ### Lista das sprites
        self.imagens_personagem = []
        self.imagens_personagemSlide = []
        self.imagens_personagemPulo = []

        ### Carrega as imagens para a animação padrão (correndo)
        for i in range(10):
            img = sprite_sheet.subsurface((i * 417, 0), (417, 509))
            img = pygame.transform.scale(img, (int(417 / 3), int(509 / 3)))
            self.imagens_personagem.append(img)

        ### Carrega as imagens para a animação de deslize
        for j in range(10):
            imgSlide = sprite_sheetSlide.subsurface((j * 396, 0), (396, 391))
            imgSlide = pygame.transform.scale(imgSlide, (int(396 / 3), int(391 / 3)))
            self.imagens_personagemSlide.append(imgSlide)

        ### Carrega as imagens para a animação de pulo
        for k in range(10):
            imgPulo = sprite_sheetPulo.subsurface((k * 409, 0), (409, 538))
            imgPulo = pygame.transform.scale(imgPulo, (int(409 / 3), int(538 / 3)))
            self.imagens_personagemPulo.append(imgPulo)

        self.index_lista = 0
        self.image = self.imagens_personagem[int(self.index_lista)]
        self.rect = self.image.get_rect()
        # Mascara para o personagem pra usar na colisão
        self.mask = pygame.mask.from_surface(self.image)

        ### Parametros pra posicionamento (chao, velocidade) e movimentação
        self.rect.center = (x, y)
        self.velocidade = 5
        self.pulando = False
        self.deslizando = False
        self.altura_pulo = 190
        self.velocidade_queda = 17
        self.velocidade_subida = 15
        self.tempo_deslizando = 0
        self.tempo_max_deslizando = 0.8
        self.tempo = 0
        self.chao = 410

    ### Eventos pra movimentar o personagem
    def atualiza_personagem(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.centerx -= self.velocidade
        if keys[K_RIGHT]:
            self.rect.centerx += self.velocidade
        if self.rect.centery == self.chao:
            if (keys[K_UP] or keys[K_SPACE]) and not self.pulando and not self.deslizando:
                self.pulando = True
            if keys[K_DOWN] and not self.deslizando:
                self.deslizando = True

    def update(self):

        if self.rect.centery == self.chao: ### Movimenta o personagem para os lados somente no caso dele estar no chão
            self.index_lista += 0.5
            if self.index_lista > 9:
                self.index_lista = 0
            self.image = self.imagens_personagem[int(self.index_lista)]

        ### Fazer o movimento do personagem pulando
        if self.pulando:  # pra fazer o movimento do personagem pular
            if self.rect.centery > (self.chao - self.altura_pulo):
                self.rect.centery -= self.velocidade_subida
                self.index_lista += 0.7
                if self.index_lista > 9:
                    self.index_lista = 0
                self.image = self.imagens_personagemPulo[int(self.index_lista)]
            else:
                self.pulando = False
                self.image = self.imagens_personagemPulo[int(self.index_lista)]
        else:
            if self.rect.centery < self.chao:
                self.rect.centery += self.velocidade_queda

            else:
                self.rect.centery = self.chao

        ### Fazer o movimento do personagem deslizando
        if self.deslizando:
            if self.rect.centery == self.chao:
                self.tempo_deslizando += 0.05
                self.index_lista += 0.7
                if self.index_lista > 9:
                    self.index_lista = 0
                self.image = self.imagens_personagemSlide[int(self.index_lista)]
                self.rect.y += 55

            if self.tempo_deslizando >= self.tempo_max_deslizando:
                self.deslizando = False
                self.tempo_deslizando = 0
        else:
            self.deslizando = False

    ### Função para desenhar o personagem no main
    def desenhar(self, tela):
        tela.blit(self.image, self.rect)

