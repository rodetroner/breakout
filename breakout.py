import pygame
import math
from pygame.locals import *

FPS = 60
DEFAULT_BALL_RADIUS = 10
DEFAULT_BALL_COLOR = (255, 0, 0)
SCREEN_X = 1024
SCREEN_Y = 768

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
clock = pygame.time.Clock()

class Ball(pygame.Rect):
    direction = math.pi / 3
    speed = 7

    def __init__ (self, x, y, radius):
        self.centerx = x
        self.centery = y
        self.width = 2 * radius
        self.height = 2 * radius

b = Ball(120, 40, DEFAULT_BALL_RADIUS)

pygame.display.init()

screenRect = screen.get_rect()

while True:
    screen.fill((0,0,0))
    clock.tick(FPS)

    pygame.draw.rect(screen, DEFAULT_BALL_COLOR, b);
    pygame.display.update(b)

    x_offset = round(b.speed * math.cos(b.direction))
    y_offset = round(b.speed * math.sin(b.direction))
    b.move_ip(x_offset, y_offset)

    if (b.top <= screenRect.top or b.bottom >= screenRect.bottom):
        b.direction = -b.direction
    if (b.left <= screenRect.left or b.right >= screenRect.right):
        b.direction = math.pi - b.direction


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.display.quit()
                exit(0)

    pygame.display.flip()
