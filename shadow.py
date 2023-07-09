import pygame
from terrain import *
from config import *


class Shadow(Terrain):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.shadow
        image = self.game.terrain_spritesheet.get_sprite(32, 143, TILESIZE, TILESIZE)
        
        super().__init__(x, y, image)