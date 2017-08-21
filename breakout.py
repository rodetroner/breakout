import pygame
import math
from pygame.locals import *

FPS = 60
DEFAULT_BALL_RADIUS = 3 
DEFAULT_BALL_COLOR = (255, 0, 0)
DEFAULT_PADDLE_COLOR = (255, 0, 0)
DEFAULT_TILE_COLOR = (0, 255, 0)
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

class Tile(pygame.Rect):
    
    def __init__(self, x, y, width, height):
        self.centerx = x
        self.centery = y
        self.width = width
        self.height = height

''' End the game '''
def endGame():
    pygame.display.quit()
    exit(0)

screen_rect = screen.get_rect()

# Create instances of balls, tiles and paddle
balls = []
balls.append(Ball(120, 40, DEFAULT_BALL_RADIUS))
tiles = []
tiles.append(Tile(20, 600, 20, 200))
for i in range(0, 400, 100):
    for j in range(0, 1000, 100):
        tiles.append(Tile(j, i, 90, 90))
paddle = Paddle(200, 700, 100)

x_paddle_offset = 0

pygame.display.init()

while True:

    screen.fill((0,0,0))

    pygame.draw.rect(screen, DEFAULT_PADDLE_COLOR, paddle)

    for t in tiles:
        pygame.draw.rect(screen, DEFAULT_TILE_COLOR, t)

    # Control direction of balls after bounce
    for b in balls:
        pygame.draw.rect(screen, DEFAULT_BALL_COLOR, b)
        # Collision with top border
        if b.top <= screen_rect.top:
            b.direction = -b.direction
        # If ball touches the ground, stop the game
        if b.bottom >= screen_rect.bottom:
            endGame()
        # Collision with side border
        if b.left <= screen_rect.left or b.right >= screen_rect.right:
            b.direction = math.pi - b.direction
        # Collision with tiles
        for t in tiles:
            if b.bottom > t.top and b.bottom < t.bottom and b.left > t.left and b.right < t.right:
                b.direction = -b.direction
            elif b.top < t.bottom and b.top > t.top and b.left > t.left and b.right < t.right:
                b.direction = -b.direction
            elif b.right > t.left and b.right < t.right and b.top > t.top and b.bottom < t.bottom:
                b.direction = math.pi - b.direction
            elif b.left < t.right and b.left > t.left and b.top > t.top and b.bottom < t.bottom:
                b.direction = math.pi - b.direction
            if t.colliderect(b):
                tiles.remove(t)
        # Collision with paddle
        if paddle.colliderect(b):
            b.direction = -b.direction

    # Prevent the paddle from crossing window border
    if paddle.left <= screen_rect.left:
        paddle.setX(screen_rect.left + paddle.width/2)
    if paddle.right >= screen_rect.right:
        paddle.setX(screen_rect.right - paddle.width/2)

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Controls of the paddle
    if keys[K_LEFT]:
        x_paddle_offset = -paddle.speed
    elif keys[K_RIGHT]:
        x_paddle_offset = paddle.speed
    else:
        x_paddle_offset = 0

    # Check if the player wants to exit by pressing Esc
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                endGame()

    # Update positions of balls and paddle
    for b in balls:
        x_ball_offset = round(b.speed * math.cos(b.direction))
        y_ball_offset = round(b.speed * math.sin(b.direction))
        b.move_ip(x_ball_offset, y_ball_offset)
    paddle.move_ip(x_paddle_offset, 0)

    pygame.display.flip()

    clock.tick(FPS)
