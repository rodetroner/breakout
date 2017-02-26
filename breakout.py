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

    direction = math.pi / 3
    speed = 7

    def __init__(self, x, y, radius):
        self.centerx = x
        self.centery = y
        self.width = 2 * radius
        self.height = 2 * radius

    def setXY(self, x, y):
        self.centerx += x 
        self.centery += y

class Paddle(pygame.Rect):

    speed = 10

    def __init__(self, x, y, length):
        self.centerx = x
        self.centery = y
        self.width = length
        self.height = 5

screenRect = screen.get_rect()

b = Ball(120, 40, DEFAULT_BALL_RADIUS)
p = Paddle(200, 700, 100)

x_paddle_offset = 0

pygame.display.init()

while True:
    screen.fill((0,0,0))

    pygame.draw.rect(screen, DEFAULT_BALL_COLOR, b)
    pygame.draw.rect(screen, DEFAULT_PADDLE_COLOR, p)
    pygame.display.update(b)
    pygame.display.update(p)

    x_ball_offset = round(b.speed * math.cos(b.direction))
    y_ball_offset = round(b.speed * math.sin(b.direction))
    b.move_ip(x_ball_offset, y_ball_offset)
    p.move_ip(x_paddle_offset, 0)

    if (b.top <= screenRect.top or b.bottom >= screenRect.bottom):
        b.direction = -b.direction
    if (b.left <= screenRect.left or b.right >= screenRect.right):
        b.direction = math.pi - b.direction


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                x_paddle_offset = -p.speed
            if event.key == K_RIGHT:
                x_paddle_offset = p.speed
            if event.key == K_ESCAPE:
                pygame.display.quit()
                exit(0)
        elif event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                x_paddle_offset = 0

    pygame.display.flip()

    clock.tick(FPS)
