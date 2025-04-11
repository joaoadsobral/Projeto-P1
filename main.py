import pygame
import pygame.time
from Personagem.personagem import Personagem
from Coletáveis.moedas import Moeda
from Coletáveis.moedas import Rubi
from Coletáveis.moedas import Esmeralda
from Colisões.pedra import Pedra
from Colisões.Avião import Aviao

pygame.init()
pygame.mixer.init()

# Musica de fundo
pygame.mixer.music.set_volume(0.2) #Ajustar volume da musica
musica_fundo = pygame.mixer.music.load('Música e Sons/Fundo.mp3')
pygame.mixer.music.play(-1)
# Sons colisões
som_moedas = pygame.mixer.Sound('Música e Sons/smw_coin.wav')
som_GameOver = pygame.mixer.Sound('Música e Sons/game_over.wav')
som_pedras = pygame.mixer.Sound('Música e Sons/pedra_collect.wav')
clock = pygame.time.Clock()

### Tela, formato, + carregando o cenário
largura = 840
altura = 620
tamanho = 840, 620
imagem = pygame.image.load('Sprites/Cenário/img.png')

tela_start = pygame.image.load('Sprites/Cenário/start.png')

### Adequar a imagem com o tamanho da tela do pygame
fundo = pygame.transform.scale(imagem, tamanho)

display = pygame.display.set_mode([largura, altura])
nome_jogo = pygame.display.set_caption('Laele Jones')

# instancia Obstaculo
obstaculo_Pedra = Pedra(2000, 450)
obstaculo_Aviao = Aviao(5000, 300)
### Crie um grupo de obstaculos

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(obstaculo_Pedra, obstaculo_Aviao)
### Crie um grupo de sprites

sprites = pygame.sprite.Group()
personagem = Personagem(250, 430)
moedas = pygame.sprite.Group()
rubis = pygame.sprite.Group()
esmeraldas = pygame.sprite.Group()
sprites.add(personagem)
sprites.add(obstaculo_Pedra)
sprites.add(obstaculo_Aviao)

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
intervalo_criacao_moedas = 10000
tempo_anterior = pygame.time.get_ticks()

# Imagem das moedas
imagem_contador_moedas = pygame.image.load("Sprites/Coletaveis/moeda.png")
imagem_contador_moedas = pygame.transform.scale(imagem_contador_moedas, (50, 55))

# Rubis
imagem_contador_rubis = pygame.image.load("Sprites/Coletaveis/ruby.png")
imagem_contador_rubis = pygame.transform.scale(imagem_contador_rubis, (50, 55))

# Esmeraldas
imagem_contador_esmeraldas = pygame.image.load("Sprites/Coletaveis/esmeralda.png")
imagem_contador_esmeraldas = pygame.transform.scale(imagem_contador_esmeraldas, (50, 55))

### Tela de Start
def tela_start():
    start_image = pygame.image.load('Sprites/Cenário/start.png')
    start_image = pygame.transform.scale(start_image, (largura, altura))
    display.blit(start_image, (0, 0))
    pygame.display.update()

    esperando_inicio = True
    while esperando_inicio:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT and esperando_inicio == True:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                esperando_inicio = False

def tela_game_over():
    gameOver_image = pygame.image.load('Sprites/Cenário/final.png')
    gameOver_image = pygame.transform.scale(gameOver_image, (largura, altura))
    display.blit(gameOver_image, (0, 0))
    pygame.display.update()
    som_GameOver.play()

    esperando_final = True
    while esperando_final:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT and esperando_final == True:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                esperando_final = False

def main():

    ### Loop do jogo, que só vai terminar quando fechar a aba
    # instancia Obstaculo
    obstaculo_Pedra = Pedra(2000, 450)
    obstaculo_Aviao = Aviao(5000, 300)

    ### Grupo de obstaculos
    grupo_obstaculos = pygame.sprite.Group()
    grupo_obstaculos.add(obstaculo_Pedra, obstaculo_Aviao)
    ### Crie um grupo de sprites

    sprites = pygame.sprite.Group()
    personagem = Personagem(250, 430)
    moedas = pygame.sprite.Group()
    rubis = pygame.sprite.Group()
    esmeraldas = pygame.sprite.Group()
    sprites.add(personagem)
    sprites.add(obstaculo_Pedra)
    sprites.add(obstaculo_Aviao)

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
    intervalo_criacao_moedas = 10000
    tempo_anterior = pygame.time.get_ticks()

    # Imagem das moedas
    imagem_contador_moedas = pygame.image.load("Sprites/Coletaveis/moeda.png")
    imagem_contador_moedas = pygame.transform.scale(imagem_contador_moedas, (50, 55))

    # Rubis
    imagem_contador_rubis = pygame.image.load("Sprites/Coletaveis/ruby.png")
    imagem_contador_rubis = pygame.transform.scale(imagem_contador_rubis, (50, 55))

    # Esmeraldas
    imagem_contador_esmeraldas = pygame.image.load("Sprites/Coletaveis/esmeralda.png")
    imagem_contador_esmeraldas = pygame.transform.scale(imagem_contador_esmeraldas, (50, 55))
    i = 0

    tela_start()
    vel_clock = 30
    gameLoop = True

    while gameLoop:
        #a velocidade do jogo vai aumentar conforme o tempo passar, mas tem um limite
        if vel_clock >= 60:
            vel_clock += 0
        else:
            vel_clock += 0.01
        clock.tick(vel_clock)

        ### Parar o jogo quando fechar a aba
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                gameLoop = False
        ## Colisões com os obstaculos
        colisoes = pygame.sprite.spritecollide(personagem, grupo_obstaculos, False, pygame.sprite.collide_mask)
        ### Imagem do cenário entrar em looping
        if not colisoes:  ### se colidir com os obstaculos ele vai parar o looping

            display.blit(fundo, (i, 0))
            display.blit(fundo, (840 + i, 0))
            if i == -840:
                display.blit(fundo, (840 + i, 0))
                i = 0
            i -= 10

            ### Loop para o contador de moedas
            for moeda in moedas:
                display.blit(moeda.image, moeda.rect)
                if pygame.sprite.collide_rect(moeda, personagem):
                    moedas.remove(moeda)
                    som_moedas.play()
                    contador_moedas += 1
            for rubi in rubis:
                display.blit(rubi.image, rubi.rect)
                if pygame.sprite.collide_rect(rubi, personagem):
                    rubis.remove(rubi)
                    som_pedras.play()
                    contador_rubis += 1
            for esmeralda in esmeraldas:
                display.blit(esmeralda.image, esmeralda.rect)
                if pygame.sprite.collide_rect(esmeralda, personagem):
                    esmeraldas.remove(esmeralda)
                    som_pedras.play()
                    contador_esmeraldas += 1

            ### Fazer os coletáveis se mexerem
            for moeda in moedas:
                moeda.movimento()
            for rubi in rubis:
                rubi.movimento()
            for esmeralda in esmeraldas:
                esmeralda.movimento()

            # Fazer obstaculo fixo no mapa
            obstaculo_Pedra.movimento()
            obstaculo_Aviao.movimento()

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
            display.blit(imagem_contador_moedas, (10, 10))
            texto_contador_moeda = fonte.render(f": {contador_moedas}", True, (255, 255, 255))
            display.blit(texto_contador_moeda, (55, 28))

            ### Contador Rubis
            display.blit(imagem_contador_rubis, (120, 10))
            texto_contador_rubis = fonte.render(f": {contador_rubis}", True, (255, 255, 255))
            display.blit(texto_contador_rubis, (175, 28))

            ### Contador Esmeraldas
            display.blit(imagem_contador_esmeraldas, (230, 10))
            texto_contador_esmeraldas = fonte.render(f": {contador_esmeraldas}", True, (255, 255, 255))
            display.blit(texto_contador_esmeraldas, (295, 28))

            # Desenha os sprites na tela
            sprites.update()
            sprites.draw(display)
            personagem.atualiza_personagem()
            display.blit(obstaculo_Pedra.image, obstaculo_Pedra.rect)
            display.blit(obstaculo_Aviao.image, obstaculo_Aviao.rect)
            pygame.display.flip()

        else:
            tela_game_over()
            main()

main()