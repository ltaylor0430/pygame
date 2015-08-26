import pygame
from pygame.locals import *


class Circle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)  # call parent constructor
        self.image = pygame.Surface([width, height])
        pygame.draw.circle(self.image, color, (
            width / 2, height / 2), width / 2)
        self.rect = self.image.get_rect()
