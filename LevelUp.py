import pygame
from functions import load_image


class LevelUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("level_up.png", -1, 130, 50)
        self.rect = self.image.get_rect()
        self.rect.y = -30
        self.rect.x = -30

    def update(self):
        self.rect.y = -100
        self.rect.x = -100
