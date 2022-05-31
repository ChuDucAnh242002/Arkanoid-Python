import pygame

class Button :
    def __init__(self, x, y, image, scale = 1) :
        self.width = image.get_width() * scale
        self.height = image.get_height() *scale
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        # print(self.x, self.y)
        # print(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        return False

    

    