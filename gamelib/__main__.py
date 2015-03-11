
import pygame
from pygame.locals import *
from gamelib.constants import *

def main():
    pygame.init()
    pygame.display.set_mode((S_WIDTH, S_HEIGHT))

    screen = pygame.display.get_surface()

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return

        pygame.display.update()

if __name__ == "__main__":
    main()
