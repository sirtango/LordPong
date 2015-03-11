
import pygame
from pygame.locals import *
from gamelib.data import datafile

def main():
    pygame.init()
    pygame.display.set_mode((480, 640))

    background = pygame.image.load(datafile('edificio.bmp')).convert()
    screen = pygame.display.get_surface()
    screen.blit(background, (0, 0))

    clock = pygame.time.Clock()
    
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return

if __name__ == "__main__":
    main()
