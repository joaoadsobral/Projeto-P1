# Projeto P1 : Indiana Jones

Em sintonia com saga de Indiana Jones, nosso jogo foi desenvolvido como parte de um projeto para a disciplina de Programação 1 do Centro de Informática da Universidade Federal de Pernambuco. Neste jogo, os jogadores terão a missão de ir o mais longe possível no mapa, desviando dos obstáculos que surgirem pelo caminho, em um estilo característico de runner, os jogadores controlarão esse personagem que corre incansavelmente, assim, coletando valiosas moedas enquanto "luta" para sobreviver diante esses obstáculos que aparecem no caminho. Os elementos visuais e sonoros transportam os jogadores para o universo de Indiana Jones, tornando essa experiência de jogo ainda mais envolvente (não literalmente hehe).


## Como rodar o código na sua máquina

Para execução do código, é necessário que você possua Python e pygame instalados.
- Faça o download do branch main deste repositório e extraia o arquivo .zip.
- Abra a pasta Projeto P1 no editor a sua escolha.
- Execute o arquivo main.py.
- Para começar o jogo pressione espaço

O movimento do jogador é controlado através das setas esquerda e direita. A barra de espaço ou a seta para cima controla seu pulo, e a seta para baixo o faz deslizar.


## Membros da equipe e suas colaborações :

Eduardo Matos (emfs )- criação e movimentação do persongaem, obstáculo

Fabio Farias (fjcff) - 
design do jogo e implementação da trilha sonora

João Antônio (jads) -  coletáveis e organização do código

Weldon Pereira (wpb) - contador dos coletáveis e fazer o "mapa andar"

## Organização do código

![Flowchart Template (1)](https://github.com/joaoadsobral/Projeto-P1/assets/144624798/60961b27-af49-4da1-b817-9b05f9d1bd76)

*main.py* - Contém  a função main, responsável por controlar o loop principal do jogo e instanciar as suas diferentes classes. Além de possuir algumas constantes como largura e altura da tela.

*Coletáveis* - Contém as classes de cada um dos coletáveis.

*Colisões* - Contém o código da classe obstáculo. 

*Personagem* - Contém o código da classe persongagem, onde ele vai receber os comandos de movimentação e processar os sprites.

*Sons, Músicas* - Possui os aúdios do jogo.

*Sprites* - Sprites de cada elemento do jogo, dividido em subpastas.

## Ferramentas e  Bibliotecas

Como ferramentas utilizamos o Vscode para nos auxiliar na hora de fazer o código, além do Github Desktop para atualizar nosso repositório através dos commits.

Como bibliotecas utilizamos o Pygame, umas vez que o mesmo proporciona diversos benefícios ao desenvolver um jogo, como simplificar a manipulação de gráficos 2D, oferecer recursos para lidar com colisões e interações de objetos, além de permitir a integração de áudio e música para criar uma experiência de jogo envolvente e imersiva.

## Conceitos utilizados

Durante o desenvolvimento do jogo, utilizamos uma ampla variedade de conceitos de programação que foram abordados ao longo da disciplina. Isso inclui desde os fundamentos básicos, como listas, estruturas de repetição e de controle, funções, até conceitos mais avançados, como a introdução à POO.

Através da POO, pudemos utilizar classes para organizar e encapsular os elementos do jogo, como personagens e objetos, tornando o código mais modular e fácil de manter.

Além disso, a estrutura do código foi construída em torno da divisão em classes e funções, seguindo as melhores práticas de programação. Essa abordagem proporcionou uma organização lógica do código, facilitando o entendimento das diferentes partes do jogo e simplificando o processo de desenvolvimento.
  
## Desafios, erros e aprendizados

Os desafios iniciais surgiram devido às barreiras que encontramos ao tentar compreender os conceitos da programação orientada a objetos, o funcionamento do Pygame e a utilização do Git e GitHub. No entanto, ao longo do desenvolvimento do jogo, conseguimos superar esses obstáculos graças ao estudo e à experiência que adquirimos.

Quanto aos desafios, além da compreensão das funcionalidades do Pygame e do Git e GitHub, enfrentamos dificuldades ao escrever código em conjunto pela primeira vez e ao nos adaptar ao estilo de escrita em grupo. Tais desafios foram superados não apenas através da comunicação exercida pelo grupo, bem como os estudos que nos proporcionaram a experiência de lidar com essas ferramentas e bibliotecas.

Um dos principais erros que cometemos foi negligenciar a comunicação eficaz em nosso grupo de trabalho, o que levou a desafios significativos relacionados à organização do código. Adicionalmente, a alocação de tarefas entre a equipe levou algum tempo para ser estabelecida, o que acabou contribuindo para alguns revés no projeto. Resumindo, não só a organização do código, como também enfrentamos atrasos na clara definição das responsabilidades individuais ao longo do processo de desenvolvimento do jogo. Esses desafios nos ensinaram valiosas lições sobre a importância da colaboração eficiente e da comunicação constante em grupo.

Quanto ao aprendizado, a experiência em trabalhar coletivamente nos proporcionou um aprendizado valioso, acumulando conhecimentos introdutórios sobre programação orientada a objetos e o uso do GitHub.

![Tela  de final](https://github.com/user-attachments/assets/d64e73cf-a618-4f35-82f4-44ce182ff251)
![Captura de tela 2023-10-02 071939](https://github.com/joaoadsobral/Projeto-P1/assets/144624798/c55cfff2-e838-47ee-b894-e7faa63642b4)
![Captura de tela 2023-10-02 073456](https://github.com/joaoadsobral/Projeto-P1/assets/144624798/b7b2af88-ca69-45d4-9e01-b64facc475dc)
![Tela  de final (1)](https://github.com/user-attachments/assets/01ba8e6b-8389-496a-853f-302cc29f13fe)
