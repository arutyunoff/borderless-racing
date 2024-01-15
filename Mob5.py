import pygame
import random
from functions import load_image


class Mob5(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        COIN1 = load_image("an_coin1.png", -1, 50, 50)
        COIN2 = load_image("an_coin2.png", -1, 50, 50)
        COIN3 = load_image("an_coin3.png", -1, 50, 50)
        COIN4 = load_image("an_coin4.png", -1, 50, 50)
        COIN5 = load_image("an_coin5.png", -1, 50, 50)
        COIN6 = load_image("an_coin6.png", -1, 50, 50)
        self.sprites = [COIN1, COIN2, COIN3, COIN4, COIN5, COIN6, COIN1]
        self.speedy = 5
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([130, 315, 220, 405])
        self.rect.y = random.randrange(-200, -10)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += self.speedy
        self.current_sprite += 0.1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.image = self.sprites[int(self.current_sprite)]
        HEIGHT = 650
        if self.rect.top > HEIGHT + 50:
            self.rect.x = random.choice([130, 315, 220, 405])
            self.rect.y = random.randrange(-200, -100)
            self.mask = pygame.mask.from_surface(self.image)
