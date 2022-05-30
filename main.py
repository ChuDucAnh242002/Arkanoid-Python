import pygame
import os
from brick import Brick

pygame.init()

WIDTH, HEIGHT = 720, 720

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")


FPS = 60

# Size
BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT = 100, 100
BRICK_WIDTH_MARGIN, BRICK_HEIGHT_MARGIN = 28, 35
BRICK_WIDTH, BRICK_HEIGHT = 45, 25

BG_IMAGE = pygame.image.load(os.path.join('asset', 'Background', 'background.jpg'))
BG_IMAGE = pygame.transform.scale(BG_IMAGE, (WIDTH, HEIGHT))

BRICK_BLUE_SMALL= pygame.image.load(os.path.join('asset', 'Bricks', 'brick_blue_small.png'))
BRICK_GREEN_SMALL= pygame.image.load(os.path.join('asset', 'Bricks', 'brick_green_small.png'))
BRICK_PINK_SMALL= pygame.image.load(os.path.join('asset', 'Bricks', 'brick_pink_small.png'))
BRICK_VIOLET_SMALL= pygame.image.load(os.path.join('asset', 'Bricks', 'brick_violet_small.png'))
BRICK_YELLOW_SMALL= pygame.image.load(os.path.join('asset', 'Bricks', 'brick_yellow_small.png'))

BRICK_BLUE_SMALL_CRACKED = pygame.image.load(os.path.join('asset', 'Bricks', 'brick_blue_small_cracked.png'))
BRICK_GREEN_SMALL_CRACKED = pygame.image.load(os.path.join('asset', 'Bricks', 'brick_green_small_cracked.png'))
BRICK_PINK_SMALL_CRACKED = pygame.image.load(os.path.join('asset', 'Bricks', 'brick_pink_small_cracked.png'))
BRICK_VIOLET_SMALL_CRACKED = pygame.image.load(os.path.join('asset', 'Bricks', 'brick_violet_small_cracked.png'))
BRICK_YELLOW_SMALL_CRACKED = pygame.image.load(os.path.join('asset', 'Bricks', 'brick_yellow_small_cracked.png'))

BRICK_BLUE_SMALL = pygame.transform.scale(BRICK_BLUE_SMALL, (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_GREEN_SMALL = pygame.transform.scale(BRICK_GREEN_SMALL, (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_PINK_SMALL = pygame.transform.scale(BRICK_PINK_SMALL, (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_VIOLET_SMALL = pygame.transform.scale(BRICK_VIOLET_SMALL, (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_YELLOW_SMALL = pygame.transform.scale(BRICK_YELLOW_SMALL, (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))

BRICK_BLUE_SMALL_CRACKED = pygame.transform.scale(BRICK_BLUE_SMALL_CRACKED, (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_GREEN_SMALL_CRACKED = pygame.transform.scale(BRICK_GREEN_SMALL_CRACKED, (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_PINK_SMALL_CRACKED = pygame.transform.scale(BRICK_PINK_SMALL_CRACKED, (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_VIOLET_SMALL_CRACKED = pygame.transform.scale(BRICK_VIOLET_SMALL_CRACKED, (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_YELLOW_SMALL_CRACKED = pygame.transform.scale(BRICK_YELLOW_SMALL_CRACKED, (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))

BRICK_BLUE = [BRICK_BLUE_SMALL, BRICK_BLUE_SMALL_CRACKED]
BRICK_GREEN = [BRICK_GREEN_SMALL, BRICK_GREEN_SMALL_CRACKED]
BRICK_PINK = [BRICK_PINK_SMALL, BRICK_PINK_SMALL_CRACKED]
BRICK_VIOLET = [BRICK_VIOLET_SMALL, BRICK_VIOLET_SMALL_CRACKED]
BRICK_YELLOW = [BRICK_YELLOW_SMALL, BRICK_YELLOW_SMALL_CRACKED]

def draw_bg(win):
    win.blit(BG_IMAGE, (0, 0))
    # for i in range (16):
    #     for j in range (5):
    #         win.blit(BRICK_PINK_SMALL, (-BRICK_WIDTH_MARGIN + BRICK_WIDTH*i, 0 + j*BRICK_HEIGHT))

    # win.blit(BRICK_PINK_SMALL, (-BRICK_WIDTH_MARGIN, -BRICK_HEIGHT_MARGIN))

def init_bricks():

    bricks = []
    image = [BRICK_BLUE, BRICK_GREEN, BRICK_PINK, BRICK_VIOLET, BRICK_YELLOW]
    for i in range (16):        
        for j in range (5):
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*i, 0 + (4-j)*BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, image[j], 2)
            bricks.append(brick)
    return bricks


def main():

    bricks = init_bricks()

    run = True
    clock = pygame.time.Clock()
    while run == True:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_bg(WIN)
        for brick in bricks:
            brick.draw(WIN)

        pygame.display.update()

if __name__ == "__main__":
    main()