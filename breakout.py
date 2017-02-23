import pygame
import math
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
        self.direction = math.pi / 3
        self.speed = 3
        self.x_offset = round(self.speed * math.cos(self.direction))
        self.y_offset = round(self.speed * math.sin(self.direction))

b = Ball(40, 40, DEFAULT_BALL_RADIUS)

pygame.display.init()

while True:
    clock.tick(FPS)

    pygame.display.update()
    pygame.draw.rect(screen, DEFAULT_BALL_COLOR, b);
    b.move_ip(b.x_offset, b.y_offset)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.display.quit()
                exit(0)

    pygame.display.flip()
