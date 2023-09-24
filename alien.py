import pygame
import random
import image
import time
from resource import *


class Alien:

    def __init__(self):
        random_size = random.uniform(ALIENS_SIZE_RANDOMIZE[0], ALIENS_SIZE_RANDOMIZE[1])
        size = (int(ALIENS_SIZES[0] * random_size), int(ALIENS_SIZES[1]*random_size))
        moving_direction, start_pos = self.define_spawn_pos(size)
        self.rect = pygame.Rect(start_pos[0],start_pos[1],size[0]//1.4,size[1]//1.4)
        self.images = [image.load("images/pngwing.com (1).png", size=size, flip=moving_direction == "right")]
        self.current_frame = 0
        self.animation_timer = 0

    def define_spawn_pos(self,size):
        global start_pos
        vel = random.uniform(ALIENS_MOVE_SPEED["min"], ALIENS_MOVE_SPEED["max"])
        moving_direction = random.choice(("left", "right", "down"))
        if moving_direction == "right":
            start_pos = (-size[0], random.randint(size[1], SCREEN_HEIGHT - size[1]))
            self.vel = [vel, 0]
        if moving_direction == "left":
            start_pos = (SCREEN_WIDTH + size[0], random.randint(size[1], SCREEN_HEIGHT - size[1]))
            self.vel = [-vel, 0]
        if moving_direction == "down":
            start_pos = (random.randint(size[0], SCREEN_WIDTH - size[0]), -size[1])
            self.vel = [0, vel]
        return moving_direction, start_pos

    def move(self):
        self.rect.move_ip(self.vel)

    def animate(self):
        t = time.time()
        if t > self.animation_timer:
            self.animation_timer = t + ANIMATION_SPEED
            self.current_frame += 1
            if self.current_frame > len(self.images)-1:
                self.current_frame = 0

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)

    def draw(self, surface):
        self.animate()
        image.draw(surface, self.images[self.current_frame], self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)