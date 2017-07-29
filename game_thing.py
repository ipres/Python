import sys, math, random, pygame
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (200, 150, 45)
RYAN = (35, 255, 145)
WHAT = (255,255,254)

screenwidth = screenheight = 800
FPS = 60


screen = pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption('GitHub hates me')
clock = pygame.time.Clock()

size = 10

class SquarePlayer:
    def __init__(self, position):
        self.position = position
        self.colour = BLACK
        self.x_delay = 0
        self.y_delay = 0
        self.k_up = self.k_down = self.k_left = self.k_right = 0
    def draw(self):
        pygame.draw.rect(screen, self.colour, (self.position,(10,10)), 0)
    def move(self):
        x,y = self.position
        x += self.k_right - self.k_left
        y += self.k_down - self.k_up
        self.position = (x,y)



player = SquarePlayer((400,400))
n = 0
key = {"up":False,"left":False,"right":False,"down":False}

while True:
    clock.tick(FPS)
    screen.fill(GREEN)
    if n >= 5:
        n=0
        player.k_up = key["up"]
        player.k_down = key["down"]
        player.k_right = key["right"]
        player.k_left = key["left"]

    else:
        n += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if hasattr(event,'key'):
            push = event.type == KEYDOWN
            if event.key == K_UP:
                key["up"] = push
            elif event.key == K_DOWN:
                key["down"] = push
            elif event.key == K_LEFT:
                key["left"] = push
            elif event.key == K_RIGHT:
                key["right"] = push
            if event.key == K_ESCAPE:
                sys.exit()

    player.move()
    player.draw()
    pygame.display.flip()
