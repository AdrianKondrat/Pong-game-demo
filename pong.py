import pygame
import sys
import random

pygame.init()

S_WIDTH, S_HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 80
BALL_SIZE = 15
PADDLE_SPEED = 6
BALL_SPEED = 4

WHITE= (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    
    def update(self, dy):
        self.rect.y += dy
        self.rect.y = max(0, min(S_HEIGHT - PADDLE_HEIGHT, self.rect.y))

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.dx, self.dy = BALL_SPEED, BALL_SPEED* random.choice([-1, 1])
    
    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.y <= 0 or self.rect.y >= S_HEIGHT - BALL_SIZE:
            self.dy = -self.dy

left_paddle = Paddle(10, S_HEIGHT//2 - PADDLE_HEIGHT//2)
right_paddle = Paddle(S_WIDTH - 20, S_HEIGHT//2 - PADDLE_HEIGHT//2)

ball = Ball(S_WIDTH//2 - BALL_SIZE//2, S_HEIGHT//2 - BALL_SIZE//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.update(-PADDLE_SPEED)
    if keys[pygame.K_s]:
        left_paddle.update(PADDLE_SPEED)

    if keys[pygame.K_k]:
        right_paddle.update(-PADDLE_SPEED)
    if keys[pygame.K_m]:
        right_paddle.update(PADDLE_SPEED)

    ball.update()

    if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
        ball.dx = -ball.dx
    
    if ball.rect.x <= 0 or ball.rect.x >= S_WIDTH - BALL_SIZE:
        ball.rect.x, ball.rect.y = S_WIDTH//2 - BALL_SIZE//2, S_HEIGHT//2 - BALL_SIZE//2
        ball.dx, ball.dy = BALL_SPEED, BALL_SPEED* random.choice([-1, 1])

    screen.fill(BLACK)
    screen.blit(left_paddle.image, left_paddle.rect)
    screen.blit(right_paddle.image, right_paddle.rect)
    screen.blit(ball.image, ball.rect)
    pygame.display.flip()

    clock.tick(60)


          

