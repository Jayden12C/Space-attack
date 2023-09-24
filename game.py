import pygame
import cv2
import time
import random
from background import Background
from resource import *
from alien import Alien


class Game:
    def __init__(self, surface):
        self.time_left = 0
        self.surface = surface
        self.background = Background()

    def reset(self):
        self.insects = []
        self.insects_spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()

    def spawn_insects(self):
        t = time.time()
        if t > self.insects_spawn_timer:
            self.insects_spawn_timer = t + ALIENS_SPAWN_TIME * 1.25
            self.insects.append(Alien())
            if self.time_left < GAME_DURATION / 2:
                self.insects.append(Alien())


    def draw(self):
        self.background.draw(self.surface)
        for insect in self.insects:
            insect.draw(self.surface)

    def game_time_update(self):
        self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)


    def update(self):
        self.draw()
        self.game_time_update()
        if self.time_left > 0:
            self.spawn_insects()
        for insect in self.insects:
            insect.move()
        cv2.waitKey(1)

