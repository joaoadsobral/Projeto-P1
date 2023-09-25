import pygame

class Moeda(pygame.sprite.Sprite):
    ### Parametros iniciais das moedas
    def __init__(self, imagem, x, y):
        super().__init__()
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def inicializar_moedas(self):
        ### Carrega a imagem da moeda e muda o tamanho
        imagem_original = pygame.image.load("Sprites/Coletaveis/moeda.png")
        imagem_redimensionada = pygame.transform.scale(imagem_original, (50, 50))
        posicoes_moedas = [(1300, 500), (1450, 500), (1600, 500)]
        moedas = []

        for posicao in posicoes_moedas:
            moeda = Moeda(imagem_redimensionada, posicao[0], posicao[1])
            moedas.append(moeda)

        return moedas

    ### Atualizar o Contador de Moedas
    def atualizar_contador(contador_moedas):
        ### Atualiza o contador de moedas
        contador_moedas += 1
        return contador_moedas

    def movimento(self):
        self.rect.x -= 20


class Rubi(pygame.sprite.Sprite):
    ### Parametros iniciais dos Rubis
    def __init__(self, imagem, x, y):
        super().__init__()
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def inicializar_rubis(self):
        ### Carrega a imagem da moeda e muda o tamanho
        imagem_original = pygame.image.load("Sprites/Coletaveis/ruby.png")
        imagem_redimensionada = pygame.transform.scale(imagem_original, (50, 50))
        posicoes_rubis = [(2375, 350), (2525, 350)]
        rubis = []

        for posicao in posicoes_rubis:
            rubi = Rubi(imagem_redimensionada, posicao[0], posicao[1])
            rubis.append(rubi)

        return rubis

    ### Atualizar o Contador de Moedas
    def atualizar_contador(contador_rubis):
        ### Atualiza o contador de moedas
        contador_rubis += 1
        return contador_rubis

    def movimento(self):
        self.rect.x -= 20

class Esmeralda(pygame.sprite.Sprite):
    ### Parametros iniciais das moedas
    def __init__(self, imagem, x, y):
        super().__init__()
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def inicializar_esmeraldas(self):
        ### Carrega a imagem da moeda e muda o tamanho
        imagem_original = pygame.image.load("Sprites/Coletaveis/esmeralda.png")
        imagem_redimensionada = pygame.transform.scale(imagem_original, (50, 50))
        posicoes_esmeraldas = [(3450, 500), (3600, 500), (3750, 500)]
        esmeraldas = []

        for posicao in posicoes_esmeraldas:
            esmeralda = Esmeralda(imagem_redimensionada, posicao[0], posicao[1])
            esmeraldas.append(esmeralda)

        return esmeraldas

    ### Atualizar o Contador de Moedas
    def atualizar_contador(contador_esmeraldas):
        ### Atualiza o contador de moedas
        contador_esmeraldas += 1
        return contador_esmeraldas

    def movimento(self):
        self.rect.x -= 20


