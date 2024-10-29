import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Configurações da paleta
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 7

# Configurações da bola
BALL_SIZE = 20
ball_speed_x = 5
ball_speed_y = 5

# Posições iniciais
paddle1_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle2_y = (HEIGHT - PADDLE_HEIGHT) // 2
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controle da paleta
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += paddle_speed

    # Atualiza a posição da bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Colisão com as paredes
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y

    # Colisão com as paletas
    if (ball_x <= PADDLE_WIDTH and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT) or \
       (ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT):
        ball_speed_x = -ball_speed_x

    # Redefinir a bola se sair da tela
    if ball_x < 0 or ball_x > WIDTH:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x = 5 * (-1 if ball_speed_x > 0 else 1)  # Troca a direção

    # Limpa a tela
    screen.fill(BLACK)

    # Desenha as paletas e a bola
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Atualiza a tela
    pygame.display.flip()
    pygame.time.delay(30)