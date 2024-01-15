import pygame
from functions import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("supra.png", -1, 65, 120)
        self.rect = self.image.get_rect()
        self.WIDTH = 600
        self.HEIGHT = 650
        self.rect.centerx = self.WIDTH / 2
        self.rect.bottom = self.HEIGHT - 35
        self.speedx = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -9
        if keystate[pygame.K_RIGHT]:
            self.speedx = 9
        if keystate[pygame.K_UP]:
            self.speedy = -2
        if keystate[pygame.K_DOWN]:
            self.speedy = +4
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > 0.85 * self.WIDTH:
            self.rect.right = 0.85 * self.WIDTH
        if self.rect.left < 96:
            self.rect.left = 96
        if self.rect.bottom > 650:
            self.rect.bottom = 650
        if self.rect.top < 0:
            self.rect.top = 0
        self.mask = pygame.mask.from_surface(self.image)
