import sys, pygame, random
from pygame.locals import *

pygame.init()

class GameEntity(): #parent entity class
    def __init__(self, x, y,delta,surface, colour):
        self.surface = surface #define surface entity is drawn on

        #get entity image and associated rect
        self.sprite = pygame.Surface([20,20]) #forms a 20x20 square
        self.sprite.fill(colour)
        self.rect = self.sprite.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        #movement speed
        self.delta = delta

    def Move(self):
        #triggers entity movement
        #states should make it easier to detect collision with screen borders
        if self.dx != 0:
            self.rect.centerx += self.dx*self.delta
            self.dy = 0

        elif self.dy != 0:
            self.rect.centery += self.dy*self.delta
            self.dx = 0

    def CollisionDetect(self,walls):
        for wall in walls:
            if self.rect.colliderect(wall):
                if self.dy == -1:
                    self.rect.top = wall.bottom
                if self.dy == 1:
                    self.rect.bottom = wall.top
                if self.dx == -1:
                    self.rect.left = wall.right
                if self.dx == 1:
                    self.rect.right = wall.left

    def Draw(self):
        #no cam insert, do need?
        self.surface.blit(self.sprite,(self.rect.centerx,self.rect.centery))


class Player(GameEntity):
    def __init__(self,x,y,delta,surface,colour):
        GameEntity.__init__(self,x,y,delta,surface,colour)

        self.dx = 0
        self.dy = 0

        #define player specific variables here

    #def PlayerInput(self,key,walls):
    def PlayerInput(self,key, walls):
        self.dx, self.dy = 0,0
        if key [K_UP]:
            self.dy = -1
        if key [K_DOWN]:
            self.dy = 1
        if key [K_LEFT]:
            self.dx = -1
        if key [K_RIGHT]:
            self.dx = 1

        self.Move()
        self.CollisionDetect(walls)
        # self.CollisionDetect(walls)

    def Draw(self):
        GameEntity.Draw(self)

    #def update(self,key,walls):
    def update(self,key,walls):
        # self.playerInput(key,walls)
        self.PlayerInput(key,walls)
