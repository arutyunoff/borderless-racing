import pygame
import random
from functions import draw_text, load_image
from Player import Player
from Mob import Mob
from Mob2 import Mob2
from Mob3 import Mob3
from Mob4 import Mob4
from Mob5 import Mob5
from LevelUp import LevelUp


def show_go_screen():
    screen.blit(game_over_icon, (180, 110))
    pygame.mixer.music.load("sounds//bg_menu.wav")
    pygame.mixer.music.play(-1)
    draw_text(screen, "Press space to restart", 30, WIDTH / 2, 615, GREEN)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = 0


def show_menu():
    screen.blit(MENU, (0, 0))
    pygame.mixer.music.load("sounds//bg_menu.wav")
    pygame.mixer.music.play(-1)
    draw_text(screen, "Press a key to begin", 30, WIDTH / 2, 585, WHITE)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


pygame.init()
screen = pygame.display.set_mode((600, 650,))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()
pygame.mixer.init()
# load
BG = load_image("road650.jpg")
MENU = load_image("menu.jpg")

COIN_BUT = load_image("an_coin1.png", -1, 40, 40)
tree_but = load_image("tree_but.png", -1, 80, 35)
level_up_icon = load_image("level_up_icon.png", -1, 40, 43)
game_over_icon = load_image("game_over.png", -1, 250, 250)
prix = load_image("prix.png", -1, 40, 40)
WIDTH = 600
HEIGHT = 650
FPS = 60
font = pygame.font.SysFont('Arial', 40)
objects = []
SCORE = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
passed = 0
coin_pos = [130, 315, 220, 405]
CRASH = pygame.mixer.Sound('sounds//crash.mp3')
coin_sound = pygame.mixer.Sound('sounds//coin_drop.mp3')
coin_sound.set_volume(0.5)
level_up_sound = pygame.mixer.Sound("sounds//level_up.mp3")
level = 0
menu = 1
pause = 0
game_over = 0
running = True
# game loop
while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                draw_text(screen, "PAUSED", 60, WIDTH / 2, 200, BLACK)
                pygame.display.flip()
                pygame.mixer.music.unpause()
                pause = not pause
    if pause == 1:
        pygame.mixer.music.pause()
        continue
    if game_over:
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        player = Player()
        coins = pygame.sprite.Group()
        all_sprites.add(player)
        m = Mob()
        m1 = Mob2()
        m2 = Mob3()
        m3 = Mob4()
        m4 = Mob5()
        l = LevelUp()
        all_sprites.add(m, m1, m2, m3, m4, l)
        mobs.add(m, m1, m2, m3)
        i = 0
        level = 0
        passed = 0
        SCORE = 0
        show_go_screen()
        game_over = False
        pygame.mixer.music.load("sounds//bg_main.mp3")
        pygame.mixer.music.play(-1)
    if menu:
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        player = Player()
        coins = pygame.sprite.Group()
        all_sprites.add(player)
        m = Mob()
        m1 = Mob2()
        m2 = Mob3()
        m3 = Mob4()
        m4 = Mob5()
        l = LevelUp()
        all_sprites.add(m, m1, m2, m3, m4, l)
        mobs.add(m, m1, m2, m3)
        i = 0
        level = 0
        passed = 0
        SCORE = 0
        show_menu()
        pygame.mixer.music.load("sounds//bg_main.mp3")
        pygame.mixer.music.play(-1)
        menu = 0

    # UPDATE
    all_sprites.update()
    if pygame.sprite.collide_mask(player, m4):
        SCORE += 1
        coin_sound.play()
        m4.rect.x = random.choice(coin_pos)
        m4.rect.y = random.randrange(-200, -10)

    if pygame.sprite.spritecollide(m4, mobs, 0):
        m4.rect.x = random.choice(coin_pos)
        m4.rect.y = random.randrange(-200, -10)

    if pygame.sprite.spritecollide(player, mobs, 0, pygame.sprite.collide_mask):
        pygame.mixer.music.pause()
        CRASH.play()
        pygame.time.delay(2000)
        game_over = True

    # RENDER
    screen.fill(BLACK)
    screen.blit(BG, (0, i))
    screen.blit(BG, (0, -HEIGHT + i))
    # looping background
    if i == HEIGHT:
        screen.blit(BG, (0, -10 * HEIGHT + i))
        i = 0
    i += 10
    passed = (m.passed + m1.passed + m2.passed + m3.passed) * 15
    screen.blit(tree_but, (520, 3))
    screen.blit(tree_but, (520, 44))
    screen.blit(tree_but, (520, 90))
    screen.blit(COIN_BUT, (510, 0))
    screen.blit(level_up_icon, (510, 87))
    screen.blit(prix, (510, 43))
    draw_text(screen, str(SCORE), 21, 575, 10, WHITE)
    draw_text(screen, str(passed), 18, 570, 50, WHITE)
    if m3.check % 2000 == 0:
        level += 1
        m.speedy += 1
        m1.speedy += 1
        m2.speedy += 1
        m4.speedy += 1
        m3.speedy += 1
    if len(str(m3.check)) == 4:
        if int(str(m3.check)[-3:]) < 200 and int(str(m3.check)[0:1]) % 2 == 0:
            l.rect.y = 10
            l.rect.x = 230
            level_up_sound.play()
    elif len(str(m3.check)) == 5:
        if int(str(m3.check)[-3:]) < 200 and int(str(m3.check)[0:2]) % 2 == 0:
            l.rect.y = 10
            l.rect.x = 230
            level_up_sound.play()
    draw_text(screen, str(level), 21, 570, 97, WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
