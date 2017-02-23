import pygame

FPS = 60

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                exit(0)