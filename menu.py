import pygame
import sys
from resource import *
from background import Background



class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()



    def draw(self):
        self.background.draw(self.surface)
        # draw title
        draw_text(self.surface, GAME_TITLE, (SCREEN_WIDTH//2, 120), COLORS["title"], font=FONTS["big"],
                    shadow=True, shadow_color=(255,255,255), pos_mode="center")


    def update(self):
        self.draw()
        if button(self.surface, 320, "START"):
            return "game"

        if button(self.surface, 320+BUTTONS_SIZES[1]*1.5, "Quit"):
            pygame.quit()
            sys.exit()
