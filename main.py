import pygame
import pygame.time
from Personagem.personagem import Personagem
from Coletáveis.moedas import Moeda
from Coletáveis.moedas import Rubi
from Coletáveis.moedas import Esmeralda

pygame.init()

clock = pygame.time.Clock()

### Tela, formato, + carregando o cenário
largura = 840
altura = 620
tamanho = 840, 620
imagem = pygame.image.load('Sprites/Cenário/img.png')

### Adequar a imagem com o tamanho da tela do pygame
fundo = pygame.transform.scale(imagem, tamanho)
display = pygame.display.set_mode([largura, altura])

### Crie um grupo de sprites
sprites = pygame.sprite.Group()
personagem = Personagem(100, 500)
moedas = pygame.sprite.Group()
rubis = pygame.sprite.Group()
esmeraldas = pygame.sprite.Group()
sprites.add(personagem)

### Carregue uma fonte para o texto do contador de moedas
pygame.font.init()
fonte = pygame.font.Font(None, 36)
contador_moedas = 0
contador_rubis = 0
contador_esmeraldas = 0

### Crie uma instância da classe Moeda
moeda = Moeda(imagem, 10, 10)
rubi = Rubi(imagem, 10, 10)
esmeralda = Esmeralda(imagem, 10, 10)


### Inicialize as moedas
moedas_lista = moeda.inicializar_moedas()
moedas.add(moedas_lista)  # Adicione as moedas ao grupo de moedas
rubis_lista = rubi.inicializar_rubis()
rubis.add(rubis_lista)
esmeraldas_lista = esmeralda.inicializar_esmeraldas()
esmeraldas.add(esmeraldas_lista)

### Parametros para as moedas entrarem em Loop
tempo_decorrido = 0
intervalo_criacao_moedas = 5000
tempo_anterior = pygame.time.get_ticks()

### Tela de Start
def tela_start():
    start_image = imagem
    start_image = pygame.transform.scale(start_image, (largura, altura))
    display.blit(start_image, (0, 0))
    pygame.display.update()

    esperando_inicio = True
    while esperando_inicio:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                esperando_inicio = False

tela_start()

### Loop do jogo, que só vai terminar quando fechar a aba
i = 0
gameLoop = True
while gameLoop:
    clock.tick(30)

    ### Parar o jogo quando fechar a aba
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            gameLoop = False

    ### Imagem do cenário entrar em looping

    display.blit(fundo, (i, 0))
    display.blit(fundo, (840 + i, 0))
    if i == -840:
        display.blit(fundo, (840 + i, 0))
        i = 0
    i -= 5

    ### Loop para o contador de moedas
    for moeda in moedas:
        display.blit(moeda.image, moeda.rect)
        if pygame.sprite.collide_rect(moeda, personagem):
            moedas.remove(moeda)
            contador_moedas += 1
    for rubi in rubis:
        display.blit(rubi.image, rubi.rect)
        if pygame.sprite.collide_rect(rubi, personagem):
            rubis.remove(rubi)
            contador_rubis += 1
    for esmeralda in esmeraldas:
        display.blit(esmeralda.image, esmeralda.rect)
        if pygame.sprite.collide_rect(esmeralda, personagem):
            esmeraldas.remove(esmeralda)
            contador_esmeraldas += 1

    ### Fazer os coletáveis se mexerem
    for moeda in moedas:
        moeda.movimento()
    for rubi in rubis:
        rubi.movimento()
    for esmeralda in esmeraldas:
        esmeralda.movimento()

    tempo_atual = pygame.time.get_ticks()
    tempo_decorrido += tempo_atual - tempo_anterior
    tempo_anterior = tempo_atual

    if tempo_decorrido >= intervalo_criacao_moedas:
        # Crie uma nova sequência de moedas e adicione-as ao grupo de moedas
        moedas_lista = moeda.inicializar_moedas()
        moedas.add(moedas_lista)
        rubis_lista = rubi.inicializar_rubis()
        rubis.add(rubis_lista)
        esmeraldas_lista = esmeralda.inicializar_esmeraldas()
        esmeraldas.add(esmeraldas_lista)

        # Zere o tempo decorrido
        tempo_decorrido = 0

    ### Contador de Moedas
    texto_contador_moedas = fonte.render(f"Moedas: {contador_moedas}", True, (255, 255, 255))
    posicao_texto_contador_moedas = (10, 10)
    display.blit(texto_contador_moedas, posicao_texto_contador_moedas)

    ### Contador Rubis
    texto_contador_rubis = fonte.render(f"Rubis: {contador_rubis}", True, (255, 255, 255))
    posicao_texto_contador_rubis = (150, 10)
    display.blit(texto_contador_rubis, posicao_texto_contador_rubis)

    ### Contador Esmeraldas
    texto_contador_esmeraldas = fonte.render(f"Esmeraldas: {contador_esmeraldas}", True, (255, 255, 255))
    posicao_texto_contador_esmeraldas = (270, 10)
    display.blit(texto_contador_esmeraldas, posicao_texto_contador_esmeraldas)
    ### Atualiza os sprites e Desenha os sprites (personagem) na tela
    sprites.update()
    sprites.draw(display)
    pygame.display.update()
    personagem.atualiza_personagem()

### Encerrar o jogo caso feche a tela
pygame.quit()
