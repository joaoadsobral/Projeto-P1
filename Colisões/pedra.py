import pygame
sprite_sheet = pygame.image.load('Sprites/Colisões/Pedra2.png')

class Pedra(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        ### Lista das sprites
        self.imagens_pedra = []

        ### Carrega as imagens para a animação padrão (correndo)
        for i in range(12):
            img = sprite_sheet.subsurface((i * 4903, 0), (4903, 4488))
            img = pygame.transform.scale(img, (int(4903 / 30), int(4488 / 30)))
            self.imagens_pedra.append(img)
        self.index_lista = 0
        self.image = self.imagens_pedra[int(self.index_lista)]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # Mascara para o personagem pra usar na colisão
        self.mask_pedra = pygame.mask.from_surface(self.image)
    def update(self):
        self.index_lista += 0.5
        if self.index_lista > 11:
            self.index_lista = 0
        self.image = self.imagens_pedra[int(self.index_lista)]

    def movimento(self):
        # toda vez que o obstaculo sair por completo da tela ele reaparece novamente
        if self.rect.topright[0] < 0:
            self.rect.x = 2000
        self.rect.x -= 20
