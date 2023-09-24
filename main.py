import pygame
import sys
import os
import image
from game import Game
from resource import *

pygame.init()
pygame.display.set_caption(WINDOW_NAME)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)
game = Game(SCREEN)


while True:

    game.update()
    pygame.display.update()

