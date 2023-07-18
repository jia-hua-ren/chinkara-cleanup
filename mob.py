import pygame
from config import *
from utility import *
from abc import ABC, abstractmethod


class Mob(pygame.sprite.Sprite, ABC):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0  

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    @abstractmethod
    # updates sprites on screen
    def update():
        pass

    @abstractmethod
    def movement():
        pass

    @abstractmethod
    def animate():
        pass
