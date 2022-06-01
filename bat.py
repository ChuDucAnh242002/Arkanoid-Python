import pygame

pygame.init()

class Bat:
    VEL = 10
    def __init__(self, x, y, width, height, image):
        self.x = self.original_x =  x
        self.y = self.original_y =  y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x + 40, y + 40, width, height)
        self.image = image

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def move(self, right = True):
        if right == True:
            self.x += self.VEL
        else:
            self.x -= self.VEL
        self.rect.x = self.x

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.rect.x = self.original_x + 40
        self.rect.y = self.original_y + 40

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
