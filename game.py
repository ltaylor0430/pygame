""" A game always starts in an order similar to this (pseudo code):
initialize()
while running():
   game_logic()
   get_input()
   update_screen()
deinitialize()
"""
import pygame
import cevent
from pygame.locals import *
from os.path import join
import sys


class App(cevent.CEvent):

    def __init__(self, width=350, height=350, fps=30):
        self._running = True
        self._display_surf = None
        self.width = width
        self.height = height
        self.size = self.width, self.height
        self.fps = fps

    def on_init(self):
        # Create main display with hardware acceleration
        # Initialize pygame, window, background, font...
        pygame.init()  # Init pygame
        pygame.display.set_caption("LT's Game")
        self._display_surf = pygame.display.set_mode(
          self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.clock = pygame.time.Clock()
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)
        # Load Image - Convert the surface to make blitting faster
        self._background = pygame.Surface(
                              self._display_surf.get_size()).convert()
        self._image_surf = pygame.image.load(
          join("data/images", "hacker_symbol8x6.jpg")).convert()

    def on_loop(self):
        milliseconds = self.clock.tick(self.fps)
        self.playtime += milliseconds / 1000.0

    def on_render(self):
        # draw image on to background surface
        self._background.blit(self._image_surf, (
          self.width - self._image_surf.get_width(), 0))
        # draw background
        self._display_surf.blit(self._background, (0, 0))
        # Draw FPS
        self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
                       self.clock.get_fps(), " " * 5, self.playtime))
        pygame.display.flip()  # Update the contents of the entire display

    def draw_text(self, text):
        #determines the amount of space needed to render the text
        fontWidth, fontHeight = self.font.size(text)
        #render(text,antialias,color,background)
        surface = self.font.render(text, True, (0, 255, 0))
        # // makes integer division in python3 - center text
        self._display_surf.blit(surface, ((self.width-fontWidth) // 2, (
                                           self.height - fontHeight) // 2))

    def on_cleanup(self):
        # Before quiting, we will cleanup
        print("calling quit!")
        pygame.quit()

    def on_exit(self):
        print("exiting...")
        self._running = False

    def on_execute(self):
        # Call on_init()
        if self.on_init() == False:
            self._running = False
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == '__main__':
    theApp = App(640,480,30)
    # This function contains the game loop
    theApp.on_execute()
    sys.exit(0)
