import pygame
from terrain import *
from config import *
 
class Ground(Terrain):
    def __init__(self, game, x, y, restricted = False, type = 'ground'):
        # determine if this block is part of restricted area (where goats can move).
        # defaults false.
        self.restricted = restricted

        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        if not restricted:
            self.groups = self.game.all_sprites, self.game.grounds

        self.type = type #determine the type of ground image

        if self.type == 'grass':
            image = self.game.terrain_spritesheet.get_sprite(36, 647, TILESIZE, TILESIZE)
        elif self.type == 'metal':
            image = self.game.terrain_spritesheet.get_sprite(183, 23, TILESIZE, TILESIZE)
        elif self.type == 'ground':
            #default is the sandy dirt
            image = self.game.terrain_spritesheet.get_sprite(30, 23, TILESIZE, TILESIZE)

        super().__init__(x, y, image)

        
