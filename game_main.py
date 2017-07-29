import pygame,sys,time
from game_entities import *
from pygame.locals import *
from game_world import *
from pygame.time import *

width = 600
height = 600
display = pygame.display.set_mode((width,height))
pygame.display.set_caption('WAT?    TITLE??!?')

clock = pygame.time.Clock()
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WHAT = (125, 125, 0)


pygame.init()


player = Player(200,200,5,display, WHITE)
world = World()
world.load("world_or_whatever.txt")
walls = world.GetCollisionRects()
running = True
while running:
    clock.tick(FPS)
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    #top of display section
    display.fill(BLACK)
    world.draw(display)
    player.update(key, walls)
    player.Draw()

    pygame.display.update()
