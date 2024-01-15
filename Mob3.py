import random
import pygame
from functions import load_image


class Mob3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        amg = load_image("amg.png", -1, 65, 120)
        ferrari = load_image("ferrari.png", -1, 65, 120)
        corvette = load_image("corvette.png", -1, 65, 120)
        bugatty = load_image("bugatty.png", -1, 65, 120)
        dodge = load_image("dodge.png", -1, 65, 120)
        supra = load_image("supra.png", -1, 65, 120)
        self.CARS = [amg, corvette, supra, ferrari, dodge, bugatty]
        self.image = random.choice(self.CARS)
        self.rect = self.image.get_rect()
        self.rect.x = 315
        self.rect.y = random.randrange(-2500, -1000)
        self.speedy = 5
        self.passed = 0

    def update(self):
        self.rect.y += self.speedy
        HEIGHT = 650
        if self.rect.top > HEIGHT + 10:
            self.image = random.choice(self.CARS)
            self.rect.y = random.randrange(-3000, -2000)
            self.mask = pygame.mask.from_surface(self.image)
            self.passed += 1
