import pygame
import os


def draw_text(surf, text, size, x, y, color):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def load_image(name, colorkey=None, *args):
    fullname = os.path.join('img', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        image = image.convert_alpha()
    if args:
        return pygame.transform.scale(image, (args[0], args[1]))
    return image
