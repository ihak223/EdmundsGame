import pygame

class Chip:

    square = True
    state = True
    image = pygame.transform.scale(pygame.image.load('files\\BLACKSQUARE.png'), (64, 64))

    def __init__(self, type):
        if type == 'square':
            self.square = True
        elif type == 'circle':
            self.square = False
            self.image = pygame.transform.scale(pygame.image.load('files\\BLACKCIRCLE.png'))

    def flip(self):
        if self.square:
            if self.state:
                self.image = pygame.transform.scale(pygame.image.load('files\\WHITESQUARE.png'))
                self.state = False
            elif not self.state:
                self.image = pygame.transform.scale(pygame.image.load('files\\BLACKSQUARE.png'))
                self.state = True
        elif not self.square:
            if self.state:
                self.image = pygame.transform.scale(pygame.image.load('files\\WHITECIRCLE.png'))
                self.state = False
            elif not self.state:
                self.image = pygame.transform.scale(pygame.image.load('files\\BLACKCIRCLE.png'))
                self.state = True




