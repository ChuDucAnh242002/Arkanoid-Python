import pygame

pygame.init()
class Ball:
    MAX_VEL = 5

    def __init__(self, x, y, radius, image):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.image = image
        self.x_vel = self.original_x_vel = 0
        self.y_vel = self.original_y_vel = - self.MAX_VEL
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.rect.x = self.x
        self.rect.y = self.y

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.x_vel = self.original_x_vel
        self.y_vel = self.original_y_vel
        self.rect.x = self.original_x
        self.rect.y = self.original_y

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False


    