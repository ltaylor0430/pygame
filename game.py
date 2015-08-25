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

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 350, 350

    def on_init(self):
        # Create main display with hardware acceleration
        pygame.init()  # Init pygame
        self._display_surf = pygame.display.set_mode(
          self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        # Load Image - Convert the surface to make blitting faster
        self._image_surf = pygame.image.load(
          join("data/images", "hacker_symbol8x6.jpg")).convert()

    def on_loop(self):
        pass

    def on_render(self):
        # Update Screen
        self._display_surf.blit(self._image_surf, (0, 0))
        pygame.display.flip()  # Update the contents of the entire display

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
    theApp = App()
    # This function contains the game loop
    theApp.on_execute()
    sys.exit(0)
