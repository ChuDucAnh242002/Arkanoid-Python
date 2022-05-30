import pygame

class Ball:
    MAX_VEL = 5

    def __init__(self, x, y, radius, image):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.image = image
        self.x_vel = 0
        self.y_vel = - self.MAX_VEL

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y