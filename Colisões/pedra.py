import pygame
class Pedra(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        imagem_original = pygame.image.load("Sprites/Colisões/Pedra.png")
        imagem_redimensionada = pygame.transform.scale(imagem_original, (100, 100))
        posicao_Pedra = [(350, 350), (1525, 350)]