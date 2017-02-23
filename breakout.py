import pygame
from pygame.locals import *

FPS = 60
DEFAULT_BALL_RADIUS = 10
DEFAULT_BALL_COLOR = (255, 0, 0)

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

class Ball(pygame.Rect):
    def __init__ (self, x, y, radius):
        self.centerx = x
        self.centery = y
        self.width = 2 * radius
        self.height = 2 * radius

b = Ball(40, 40, DEFAULT_BALL_RADIUS)

while True:
    clock.tick(FPS)

    pygame.draw.rect(screen, DEFAULT_BALL_COLOR, b);

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                exit(0)

    pygame.display.flip()
