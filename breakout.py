import pygame
import math
from pygame.locals import *

FPS = 60
DEFAULT_BALL_RADIUS = 3 
DEFAULT_BALL_COLOR = (255, 0, 0)
DEFAULT_PADDLE_COLOR = (255, 0, 0)
SCREEN_X = 1024
SCREEN_Y = 768

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
clock = pygame.time.Clock()


class Ball(pygame.Rect):

    # starting direction = 60 degrees
    direction = math.pi / 3
    speed = 7 

    def __init__(self, x, y, radius):
        self.centerx = x
        self.centery = y
        self.width = 2 * radius
        self.height = 2 * radius

    def setX(self, x):
        self.centerx = x 

    def setY(self, y):
        self.centery = y


class Paddle(pygame.Rect):

    speed = 10

    def __init__(self, x, y, length):
        self.centerx = x
        self.centery = y
        self.width = length
        self.height = 5

    def setX(self, x):
        self.centerx = x 

    def setY(self, y):
        self.centery = y


screen_rect = screen.get_rect()

b = Ball(120, 40, DEFAULT_BALL_RADIUS)
paddle = Paddle(200, 700, 100)

x_paddle_offset = 0

pygame.display.init()

while True:

    screen.fill((0,0,0))

    pygame.draw.rect(screen, DEFAULT_BALL_COLOR, b)
    pygame.draw.rect(screen, DEFAULT_PADDLE_COLOR, paddle)

    if (b.top <= screen_rect.top or b.bottom >= screen_rect.bottom):
        b.direction = -b.direction
    if (b.left <= screen_rect.left or b.right >= screen_rect.right):
        b.direction = math.pi - b.direction

    if paddle.colliderect(b):
        b.direction = -b.direction

    if paddle.left <= screen_rect.left:
        paddle.setX(screen_rect.left + paddle.width/2)

    if paddle.right >= screen_rect.right:
        paddle.setX(screen_rect.right - paddle.width/2)

    keys = pygame.key.get_pressed()

    if keys[K_LEFT]:
        x_paddle_offset = -paddle.speed
    elif keys[K_RIGHT]:
        x_paddle_offset = paddle.speed
    else:
        x_paddle_offset = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.display.quit()
                exit(0)

    x_ball_offset = round(b.speed * math.cos(b.direction))
    y_ball_offset = round(b.speed * math.sin(b.direction))
    b.move_ip(x_ball_offset, y_ball_offset)
    paddle.move_ip(x_paddle_offset, 0)

    pygame.display.flip()

    clock.tick(FPS)
