import pygame
sprite_sheet = pygame.image.load('Sprites/Colisões/Aviao.png')
class Aviao(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        ### Lista das sprites
        self.imagens_aviao = []

        ### Carrega as imagens para a animação padrão (correndo)
        for i in range(7):
            img = sprite_sheet.subsurface((i * 445, 0), (445, 304))
            img = pygame.transform.scale(img, (int(445 / 2), int(304 / 2)))
            self.imagens_aviao.append(img)
        self.index_lista = 0
        self.image = self.imagens_aviao[int(self.index_lista)]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # Mascara para o personagem pra usar na colisão
        self.mask_Aviao = pygame.mask.from_surface(self.image)
    def update(self):
        self.index_lista += 0.5
        if self.index_lista > 6:
            self.index_lista = 0
        self.image = self.imagens_aviao[int(self.index_lista)]



    def movimento(self):
        # toda vez que o obstaculo sair por completo da tela ele reaparece novamente
        if self.rect.topright[0] < 0:
            self.rect.x = 9000
        self.rect.x -= 21
