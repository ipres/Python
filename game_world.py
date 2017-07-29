import pygame, sys

xlen = 80
ylen = 80

tilelen = 20

class World:
    def __init__(self):
        self.Tiles = [[0 for x in range(xlen)] for x in range(ylen)]

    def load(self, fileName):
        x = 0
        y = 0
        f = open(fileName, 'r')

        for line in f:
            while x < len(line):
                self.Tiles[x][y] = line[x]
                if line[x] == 's':
                    self.spawnrect = pygame.Rect(tilelen*x, tilelen*y, tilelen, tilelen)
                x += 1
            x = 0
            y += 1

    def GetCollisionRects(self):
        rects = []
        for y in range(ylen):
            for x in range(xlen):
                colour = (0,0,0)
                if self.Tiles[x][y] == '1':
                    rects.append(pygame.Rect(tilelen*x, tilelen*y, tilelen, tilelen))
        return rects

    def draw(self, screen):

        for y in range(ylen):
            for x in range(xlen):
                colour = (0,0,0)
                if self.Tiles[x][y] == '0':
                    colour = (0,0,0)
                elif self.Tiles[x][y] == '1':
                    colour = (105,175,10)

                sprite = pygame.Surface([tilelen, tilelen])
                sprite.fill(colour)
                # (tilelen*x, tilelen*y, tilelen, tilelen)

                screen.blit(sprite, (x*tilelen,y*tilelen))
