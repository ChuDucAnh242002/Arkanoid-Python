class Brick:
    def __init__(self, x, y, width, height, image, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.cur_image = image[0]
        self.health = health

    def draw(self, win):
        win.blit(self.cur_image, (self.x, self.y))



