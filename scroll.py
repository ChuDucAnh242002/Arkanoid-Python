import pygame

class Scroll:
    def __init__(self, x, y, image, scale = 1) :
        self.width = image.get_width() * scale
        self.height = image.get_height() *scale
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def scroll(self, mouse_pos, max_x_left, max_x_right, music = None):

        if self.rect.collidepoint(mouse_pos) and self.rect.x >= max_x_left and self.rect.x <= max_x_right:
            volume = (self.rect.x - 300) / 100
            new_volume = volume + (mouse_pos[0] - self.width // 2 - self.rect.x)/100
            music.set_volume(new_volume)
            self.rect.x = mouse_pos[0] - self.width // 2

        if self.rect.x < max_x_left:
            self.rect.x = max_x_left
        
        if self.rect.x > max_x_right:
            self.rect.x = max_x_right

