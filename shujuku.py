import pygame
import sys
from pygame.locals import *

class puke(pygame.sprite.Sprite):
    def __init__(self,image,position,speed):
        pygame.sprite.Sprite.__init__(self)
        