import pygame
from config import *

# Various terrain classes that are used to create the map
# Terrain superclass
# Block, Shadow, Ground, Door

class Terrain(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# Block class
class Block(Terrain):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        image = self.game.terrain_spritesheet.get_sprite(33, 273, TILESIZE, TILESIZE)
        
        super().__init__(x, y, image)

# Shadow class
class Shadow(Terrain):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites, self.game.shadow
        image = self.game.terrain_spritesheet.get_sprite(32, 143, TILESIZE, TILESIZE)
        
        super().__init__(x, y, image)

# Door class
# what player needs to reach to enter next level
class Door(Terrain):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.door
        image = self.game.terrain_spritesheet.get_sprite(35, 384, TILESIZE, TILESIZE)
        
        super().__init__(x, y, image)

# Ground class
# specify type on construction
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