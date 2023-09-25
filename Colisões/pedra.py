import pygame
class Pedra(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Sprites/Colisões/Pedra.png") #Carrega a imagem da pedra que é o Obstaculo
        self.image = pygame.transform.scale(self.image, (100, 120))  #Diminui o tamanho da imagem
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # Criar uma mascara para a pedra
        self.mask = pygame.mask.from_surface(self.image)
    def movimento(self):
        #toda vez que o obstaculo sair por completo da tela ele reaparece novamente
        if self.rect.topright[0] < 0:
            self.rect.x = 1200
        self.rect.x -= 20

