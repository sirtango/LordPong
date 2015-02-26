
import pygame
from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_mode((480, 640))

    clock = pygame.time.Clock()
    
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return

if __name__ == "__main__":
    main()
