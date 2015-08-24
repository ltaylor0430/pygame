""" A game always starts in an order similar to this (pseudo code):
initialize()
while running():
   game_logic()
   get_input()
   update_screen()
deinitialize()
"""
import pygame
from pygame.locals import *


class App:

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400

    def on_init(self):
        # Create main display with hardware acceleration
        pygame.init()  # Init pygame
        self._display_surf = pygame.display.set_mode(
          self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        # Before quiting, we will cleanup
        pygame.quit()

    def on_event(self, event):
        # Quit game event set flag to false to exit game loop
        if event.type == pygame.QUIT:
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
    theApp = App()
    # This function contains the game loop
    theApp.on_execute()
