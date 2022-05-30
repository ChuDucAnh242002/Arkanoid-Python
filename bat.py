import pygame

class Bat:
    VEL = 4
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x + 40, y + 60, width, height)
        self.image = image

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def move(self, right = True):
        if right == True:
            self.x += self.VEL
        else:
            self.x -= self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
