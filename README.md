# Projeto P1 : Laele Jones

Em sintonia com a emocionante saga de Indiana Jones, o jogo 2D intitulado "Laele Jones" foi desenvolvido como parte de um projeto para a disciplina de Programação 1 do Centro de Informática da Universidade Federal de Pernambuco. Neste jogo, os jogadores embarcam em uma aventura sem fim, em um estilo característico de runner, onde controlam um protagonista que corre incansavelmente, coletando valiosas moedas enquanto luta para sobreviver diante das pedras que surgem ao longo do caminho. Os elementos visuais e sonoros transportam os jogadores para o universo icônico de Indiana Jones, tornando essa experiência de jogo ainda mais envolvente.


## Como rodar o código na sua máquina

Para execução do código, é necessário que você possua Python e pygame instalados.
- Faça o download do branch main deste repositório e extraia o arquivo .zip.
- Abra a pasta Projeto P1 no editor a sua escolha.
- "Falar que precisa de python e pygame"
- Execute o arquivo main.py.

O movimento do jogador é controlado através das setas esquerda e direita. A barra de espaço controla seu pulo, e a seta para baixo o faz deslizar.


## Membros da equipe e suas colaborações :

Eduardo Matos (emfs )- criação e movimentação do persongaem, obstáculo

Fabio Farias (fjcff) - 
design do jogo e implementação da trilha sonora

João Antônio (jads) -  coletáveis e organização do código

Weldon Pereira (wpb) - contador dos coletáveis e fazer o "mapa andar"

## Organização do código

"bota nossa imagem"

![Hierarquia de pastas](https://i.imgur.com/amS0ZUW.jpeg)

*main.py* - Aontém  a função main, responsável por controlar o loop principal do jogo e instanciar as suas diferentes classes. Além de possuir algumas constantes como largura e altura da tela.

*Coletáveis* - Contém as classes de cada um dos coletáveis.

*Colisões* - Contém o código da classe obstáculo. 

*Personagem* - Contém o código da classe persongagem, onde ele vai receber os comandos de movimentação e processar os sprites.

*Sons, Músicas e Sprites* - o primeiro possui os aúdios do jogo e o segundo os sprites de cada elemento do jogo, dividido em subpastas.

## Ferramentas e  Bibliotecas

Como ferramentas utilizamos o Vscode para nos auxiliar na hora de fazer o código, além do Github Desktop para atualizar nosso repositório através dos commits.

Como bibliotecas utilizamos o Pygame, umas vez que o mesmo proporciona diversos benefícios ao desenvolver um jogo, como simplificar a manipulação de gráficos 2D, oferecer recursos para lidar com colisões e interações de objetos, além de permitir a integração de áudio e música para criar uma experiência de jogo envolvente e imersiva.

## Conceitos utilizados

"Detalhar mais isso aqui tudo"

Utilizamos os conceitos ensinados no início da disciplina como a noção de listas, estruturas de repetição, funções, até as partes mais avançadas, como noções iniciais de POO.

Outra noção de extrema importância para o projeto foi a introdução a classes e objetos. Além do fato de que toda a estrutura do código tem como base a divisão por classes e suas funções, poder gerenciar cada objeto de maneira independente tornou o processo de escrita do código mais fácil e melhorou sua legibilidade de forma significante.
  
## Desafios, erros e aprendizados

"Detalhar bastante
  
Os problemas iniciais surgiram com a dificuldade de compreensão, tanto de programação orientada a objetos, quanto ao funcionamento e uso do pygame, e também em relação ao uso do git e github. Esses problemas foram resolvidos com o estudo e experiência que se adquiriu ao longo do processo de desenvolvimento do jogo.

Quanto a desafios, podem ser citados a dificuldade de escrever um código em conjunto pela primeira vez e o processo de adaptação ao estilo de escrita de um grande grupo de diferentes pessoas. Uma melhor comunicação, tanto dentro do código, em forma de comentários, quanto fora dele, permitiu que esse desafio fosse superado.

Um dos maiores erros cometidos ao desenvolver esse projeto foi subestimar a importância da organização do código. Houve um momento em que diversas funções, referentes a diferentes classes, foram condensadas em uma só, algo que dificultou a identificação de erros (e suas eventuais correções) e que poderia ter sido evitado se tivessemos focado em manter o código limpo desde o início.

Foi a primeira vez de grande parte da equipe desenvolvendo algo em conjunto e, assim, todas as partes que estão envolvidas nas etapas de escrever um código com outras pessoas serviram de aprendizado. Em especial, destacam-se o novo entendimento adquirido quanto a necessidade de separar um código em diferentes pastas e de comentar um código, ambos essenciais no processo de desenvolvimento desse projeto. Também foram adquiridos conhecimentos iniciais em relação a programação orientada a objetos e github.

"Colocar nossas imagens do jogo Tela inicial, rodando e game over"
