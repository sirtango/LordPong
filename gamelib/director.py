
from pygame import Surface
from pygame.image import load as load_image
from gamelib.data import scenefile
from gamelib.constants import *

class Scene(Surface):
    def __init__(self, name):
        super(Scene, self).__init__((S_WIDTH, S_HEIGHT))

        self.background = load_image(scenefile('background.bmp'))
        self.suscribed_events = {}
        self.director = None

    def update(self):
        self.blit(self.background)
