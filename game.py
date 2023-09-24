import pygame
import cv2
import time
import random
from background import Background
from resource import *


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.game_start_time = time.time()
        self.insects = []
        self.cap = cv2.VideoCapture(0)

    def draw(self):
        self.background.draw(self.surface)
        for insect in self.insects:
            insect.draw(self.surface)


    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)


    def update(self):

        self.draw()
        self.game_time_update()
        cv2.waitKey(1)
