import pygame
import time
import random

# Inicializar o Pygame
pygame.init()

# Definir as cores RGB
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Configurações da tela
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Jogo da Cobrinha')

# Define o relógio do jogo
clock = pygame.time.Clock()

# Define o tamanho da cobra
snake_block = 10

# Define a velocidade da cobra
snake_speed = 15

# Define a fonte do texto
font_style = pygame.font.SysFont(None, 30)


# Função para mostrar a pontuação
def Your_score(score):
    value = font_style.render("Pontuação: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


# Função para desenhar a cobra na tela
def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])


# Função do jogo principal
def gameLoop():
    # Define a posição inicial da cobra
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Define a mudança de posição inicial da cobra
    x1_change = 0
    y1_change = 0

    # Define o tamanho inicial da cobra
    snake_List = []
    Length_of_snake = 1

    # Define a posição inicial da comida
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Define variável para controlar se o jogo acabou ou não
    game_over = False

    # Loop principal do jogo
    while not game_over:
        # Loop para lidar com os eventos do jogo
        for event in pygame.event.get():
            # Se o usuário clicar no botão de fechar, o jogo acaba
            if event.type == pygame.QUIT:
                game_over = True
            # Se uma tecla for pressionada, verifica qual tecla foi pressionada e muda a direção da cobra de acordo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Verifica se a cobra atingiu as bordas da tela
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
