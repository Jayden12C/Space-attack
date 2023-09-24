import pygame
import sys
import os
import image
from game import Game
from menu import Menu
from resource import *

pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)
state = "menu"

# Creation -------------------------------------------------------- #
game = Game(SCREEN)
menu = Menu(SCREEN)
mainClock = pygame.time.Clock()
def user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


def update():
    global state
    if state == "menu":
        if menu.update() == "game":
            game.reset()
            state = "game"
    elif state == "game":
        if game.update() == "menu":
            state = "menu"
    pygame.display.update()
    mainClock.tick(FPS)

while True:
    user_events()
    update()
    pygame.display.update()

