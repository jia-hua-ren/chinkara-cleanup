import pygame
from config import *
from terrain import *

class Block(Terrain):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        image = self.game.terrain_spritesheet.get_sprite(33, 273, TILESIZE, TILESIZE)
        
        super().__init__(x, y, image)

        
