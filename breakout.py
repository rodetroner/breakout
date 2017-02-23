import pygame

FPS = 60
BALL_RADIUS = 10

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

class Ball(pygame.Rect):
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.width = 2 * BALL_RADIUS
        self.height = 2 * BALL_RADIUS

while True:
    clock.tick(FPS)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                exit(0)
