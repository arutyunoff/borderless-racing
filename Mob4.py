import random
import pygame
from functions import load_image


class Mob4(pygame.sprite.Sprite):
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
        self.rect.x = 130
        self.rect.y = random.randrange(-2000, -500)
        self.speedy = 5
        self.mask = pygame.mask.from_surface(self.image)
        self.passed = 0
        self.level = 1
        self.stat = 0
        self.check = 0

    def update(self):
        self.rect.y += self.speedy
        self.check += 1
        HEIGHT = 650
        if self.rect.top > HEIGHT + 10:
            self.image = random.choice(self.CARS)
            self.rect.y = random.randrange(-2000, -40)
            self.mask = pygame.mask.from_surface(self.image)
            self.passed += 1
            self.level += 0.1
            self.stat += 1
