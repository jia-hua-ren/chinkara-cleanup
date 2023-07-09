import pygame
from config import *
from utility import *

# Various UI elements for game interface
# Button, Textbox, Fadein
# Slideshow should be here, but it is too long, so it is just in another file

class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        """self, x, y, width, height, fg, bg, content, fontsize)"""
        self.font = pygame.font.Font(FONT_PATH, fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg =fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height)) 
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.center = (self.x, self.y)

        self.text = self.font.render(self.content, False, self.fg) #false antialiasing
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
    


class Textbox(pygame.sprite.Sprite):
    def __init__(self, game, text_list, size, clock):
        self.clock = clock
        self.text_list = text_list #all diologues to go through
        self.text_index = 0
        self.size = size - 1 # find maximum index for text_list

        self.game = game
        self._layer = TEXTBOX_LAYER
        self.groups = self.game.all_sprites, self.game.textbox
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = self.game.player.rect.x
        self.y = WIN_HEIGHT * 0.75
        self.width = WIN_WIDTH
        self.height = WIN_HEIGHT
        self.font = pygame.font.Font(FONT_PATH, 32)
        self.image = self.font.render(self.text_list[self.text_index], False, BLACK, RED)

        # self.image = self.game.wall_spritesheet.get_sprite(0, 0, self.width, self.height)
        # self.image = pygame.Surface([self.width, self.height])
        # self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()

        
        # self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.kill_on_release = False

        self.wait_seconds = 3.5
        self.wait_clock_cycles = FPS * self.wait_seconds
        self.clock_cycles = 0

    def events(self):
        key_pressed = pygame.key.get_pressed() 

        if key_pressed[pygame.K_SPACE]:
            self.kill_on_release = True
        elif self.kill_on_release == True and not key_pressed[pygame.K_SPACE]:
            # self.kill()
            if self.text_index == self.size:
                self.kill()
            else:
                self.text_index += 1
                self.image = self.font.render(self.text_list[self.text_index], False, BLACK, RED)
                self.rect = self.image.get_rect()
                self.kill_on_release = False

        if self.clock_cycles > self.wait_clock_cycles:
            if self.text_index == self.size:
                self.kill()
            else:
                self.text_index += 1
                self.image = self.font.render(self.text_list[self.text_index], False, BLACK, RED)
                self.rect = self.image.get_rect()
            self.clock_cycles = 0

    def update(self):
        self.events()
        self.rect.center = (self.game.player.rect.x, self.y)

        pygame.draw.rect(self.game.screen, WHITE, self.rect)

        self.clock_cycles += 1
        # self.clock.tick(FPS)


class Fadein():
    def __init__(self, image, pos, speed, screen):
        self.image = image
        self.pos = pos
        self.screen = screen
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.image.set_alpha(0)
        self.alph = 0
    
    def update(self):
        if self.alph <= 250:
            self.alph += self.speed
            self.image.set_alpha(self.alph)

    def draw(self):
        # print(self.alph)
        self.update()
        self.screen.fill(BLACK)
        self.screen.blit(self.image, self.rect)