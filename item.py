import pygame
from config import *
from levels import *
from utility import Text
from ui import Button
from abc import ABC, abstractmethod

class Item(pygame.sprite.Sprite, ABC):
    def __init__(self, x, y):

        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.item
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        
        # self.image = pygame.Surface([self.width, self.height])
        # self.image.fill((0, 0, 100))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    @abstractmethod
    def item_popup():
        pass
        
    # def collide_player(self):
    #     hits = pygame.sprite.spritecollide(self, self.game.player, False)
    #     if hits:
    #         self.kill() #remove item from all sprites
    #         self.game.item_aquired = True

    # def update(self):
    #     self.collide_player()



class Brochure(Item):
    def __init__(self, game, x, y) -> None:
        self.game = game
        self.width = TILESIZE / 2
        self.height = TILESIZE / 2

        self.id = 1

        self.image = self.game.terrain_spritesheet.get_sprite(184, 426, self.width, self.height)
        super().__init__(x, y)
        
        

    def item_popup(self):
        sentences = []
        finished_reading = False
        i = 0
        for text in gdptext:
            sentences.append(Text(text, (WIN_WIDTH/2, WIN_HEIGHT/6 + i * 25), 25, WHITE, False))
            sentences[i].update(text)
            i+=1
        
        back_button = Button(WIN_WIDTH/2, 4*WIN_HEIGHT/6, 300, 150, WHITE, BLACK, 'back', 50)

        while not finished_reading:
            self.game.events()
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if back_button.is_pressed(mouse_pos, mouse_pressed):
                finished_reading = True

            self.game.screen.blit(self.game.bg_img, (0,0))
            for sen in sentences:
                sen.draw(self.game.screen)
            self.game.screen.blit(back_button.image, back_button.rect)
            self.game.clock.tick(FPS)

            pygame.display.update()

class Key(Item):
    def __init__(self, game, x, y):
        self.game = game
        self.width = TILESIZE / 2
        self.height = TILESIZE / 2

        self.id = 0

        self.image = self.game.terrain_spritesheet.get_sprite(184, 490, self.width, self.height)
        super().__init__(x, y)

    def item_popup(self):
        pass