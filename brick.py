import pygame

class Brick:
    def __init__(self, x, y, width, height, image, health):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height
        self.image = image
        self.cur_image = image[0]
        self.health = health
        self.rect = pygame.Rect(x + 28, y + 35, width , height)

    def draw(self, win):
        win.blit(self.cur_image, (self.x, self.y))
