import pygame
import os
import sys
from pygame import mixer

from brick import Brick
from bat import Bat
from ball import Ball
from button import Button
from scroll import Scroll

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 720, 720

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arkanoid")

CLOCK = pygame.time.Clock()
FPS = 60

LOSE_FONT = pygame.font.SysFont("comiscans", 50)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Size
BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT = 100, 100
BRICK_WIDTH_MARGIN, BRICK_HEIGHT_MARGIN = 28, 35
BRICK_WIDTH, BRICK_HEIGHT = 45, 25

BAT_IMAGE_WIDTH, BAT_IMAGE_HEIGHT = 120, 120
BAT_HEIGHT_BOTTOM_MARGIN, BAT_HEIGHT_TOP_MARGIN = BAT_IMAGE_HEIGHT /2, 40
BAT_HEIGHT = 20

BALL_WIDTH, BALL_HEIGHT = 20, 20
BALL_IMAGE_WIDTH, BALL_IMAGE_HEIGHT = 100, 100

BALL_RADIUS = 10
BALL_IMAGE_RADIUS = 100

LEVEL_WIDTH, LEVEL_HEIGHT = 600, 100

BUTTON_WIDTH, BUTTON_HEIGHT = 100, 100
MENU_WIDTH, MENU_HEIGHT = 150, 100
SETTING_BG_WIDTH, SETTING_BG_HEIGHT = 400, 550
OK_WIDTH , OK_HEIGHT = 70, 50
OPTIONS_WIDTH, OPTIONS_HEIGHT = 150, 100
PINK_BAR_WIDTH, PINK_BAR_HEIGHT = 200, 20
RED_BAR_WIDTH, RED_BAR_HEIGHT = 25, 17
BUY_BONUS_WIDTH, BUY_BONUS_HEIGHT = 200, 70
BUY_BONUS_BG_WIDTH, BUY_BONUS_BG_HEIGHT = 720, 500

# Load image
# Back ground
BG_IMAGE = pygame.image.load(os.path.join('asset', 'Background', 'background.jpg'))
BG_IMAGE = pygame.transform.scale(BG_IMAGE, (WIDTH, HEIGHT))

#Brick

BRICK_BLUE_SMALL = pygame.transform.scale(pygame.image.load(
                    os.path.join('asset', 'Bricks', 'brick_blue_small.png')), (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_GREEN_SMALL = pygame.transform.scale(pygame.image.load(
                    os.path.join('asset', 'Bricks', 'brick_green_small.png')), (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_PINK_SMALL = pygame.transform.scale(pygame.image.load( 
                    os.path.join('asset', 'Bricks', 'brick_pink_small.png')), (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_VIOLET_SMALL = pygame.transform.scale(pygame.image.load(
                    os.path.join('asset', 'Bricks', 'brick_violet_small.png')), (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_YELLOW_SMALL = pygame.transform.scale(pygame.image.load(
                    os.path.join('asset', 'Bricks', 'brick_yellow_small.png')), (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))

BRICK_BLUE_SMALL_CRACKED = pygame.transform.scale(pygame.image.load(
                    os.path.join('asset', 'Bricks', 'brick_blue_small_cracked.png')), (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_GREEN_SMALL_CRACKED = pygame.transform.scale(pygame.image.load(
                    os.path.join('asset', 'Bricks', 'brick_green_small_cracked.png')), (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_PINK_SMALL_CRACKED = pygame.transform.scale(pygame.image.load(
                    os.path.join('asset', 'Bricks', 'brick_pink_small_cracked.png')), (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_VIOLET_SMALL_CRACKED = pygame.transform.scale(pygame.image.load(
                    os.path.join('asset', 'Bricks', 'brick_violet_small_cracked.png')), (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))
BRICK_YELLOW_SMALL_CRACKED = pygame.transform.scale(pygame.image.load(
                    os.path.join('asset', 'Bricks', 'brick_yellow_small_cracked.png')), (BRICK_IMAGE_WIDTH, BRICK_IMAGE_HEIGHT))

BRICK_BLUE = [BRICK_BLUE_SMALL, BRICK_BLUE_SMALL_CRACKED]
BRICK_GREEN = [BRICK_GREEN_SMALL, BRICK_GREEN_SMALL_CRACKED]
BRICK_PINK = [BRICK_PINK_SMALL, BRICK_PINK_SMALL_CRACKED]
BRICK_VIOLET = [BRICK_VIOLET_SMALL, BRICK_VIOLET_SMALL_CRACKED]
BRICK_YELLOW = [BRICK_YELLOW_SMALL, BRICK_YELLOW_SMALL_CRACKED]

# Bat/ paddle
BAT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Bats', 'bat_black.png')), (BAT_IMAGE_WIDTH, BAT_IMAGE_HEIGHT))
BAT_BLACK_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Bats', 'bat_black.png')), (BAT_IMAGE_WIDTH, BAT_IMAGE_HEIGHT))
BAT_BLUE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Bats', 'bat_blue.png')), (BAT_IMAGE_WIDTH, BAT_IMAGE_HEIGHT))
BAT_ORANGE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Bats', 'bat_orange.png')), (BAT_IMAGE_WIDTH, BAT_IMAGE_HEIGHT))
BAT_PINK_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Bats', 'bat_pink.png')), (BAT_IMAGE_WIDTH, BAT_IMAGE_HEIGHT))
BAT_YELLOW_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Bats', 'bat_yellow.png')), (BAT_IMAGE_WIDTH, BAT_IMAGE_HEIGHT))
BAT_IMAGES = [BAT_BLACK_IMAGE, BAT_BLUE_IMAGE, BAT_ORANGE_IMAGE, BAT_PINK_IMAGE, BAT_YELLOW_IMAGE]

# Ball
BALL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Balls', 'ball_silver.png')), (BALL_WIDTH, BALL_HEIGHT))
BALL_BLUE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Balls', 'ball_blue.png')), (BALL_IMAGE_WIDTH, BALL_IMAGE_HEIGHT))
BALL_GREEN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Balls', 'ball_green.png')), (BALL_IMAGE_WIDTH, BALL_IMAGE_HEIGHT))
BALL_ORANGE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Balls', 'ball_orange.png')), (BALL_IMAGE_WIDTH, BALL_IMAGE_HEIGHT))
BALL_RED_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Balls', 'ball_red.png')), (BALL_IMAGE_WIDTH, BALL_IMAGE_HEIGHT))
BALL_SILVER_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Balls', 'ball_silver.png')), (BALL_IMAGE_WIDTH, BALL_IMAGE_HEIGHT))
BALL_YELLOW_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'Balls', 'ball_yellow.png')), (BALL_IMAGE_WIDTH, BALL_IMAGE_HEIGHT))
BALL_IMAGES = [BALL_BLUE_IMAGE, BALL_GREEN_IMAGE, BALL_ORANGE_IMAGE, BALL_RED_IMAGE, BALL_SILVER_IMAGE, BALL_YELLOW_IMAGE]

# UI
LEVEL_COMPLETE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'level.png')), (LEVEL_WIDTH, LEVEL_HEIGHT))
OK_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'ok.png')), (OK_WIDTH, OK_HEIGHT))
OPTIONS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'options.png')), (OPTIONS_WIDTH, OPTIONS_HEIGHT))
BUY_BONUS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'bonus.png')), (BUY_BONUS_WIDTH, BUY_BONUS_HEIGHT))

PLAY_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'b_7.png')), (BUTTON_WIDTH, BUTTON_HEIGHT))
SETTING_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'b_6.png')), (BUTTON_WIDTH, BUTTON_HEIGHT))
YES_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'b_1.png')), (BUTTON_WIDTH, BUTTON_HEIGHT))
NO_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'b_2.png')), (BUTTON_WIDTH, BUTTON_HEIGHT))

MENU = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'b_5.png')), (MENU_WIDTH, MENU_HEIGHT))
SETTING_BG = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', '1.png')), (SETTING_BG_WIDTH, SETTING_BG_HEIGHT))
BUY_BONUS_BG = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', '3.png')), (BUY_BONUS_BG_WIDTH, BUY_BONUS_BG_HEIGHT))

SOUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'sound.png')), (BUTTON_WIDTH, BUTTON_HEIGHT))
MUSIC_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'music.png')), (BUTTON_WIDTH, BUTTON_HEIGHT))
PINK_BAR = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'sl_2.png')), (PINK_BAR_WIDTH, PINK_BAR_HEIGHT))
RED_BAR = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'UI', 'sl_1.png')), (RED_BAR_WIDTH, RED_BAR_HEIGHT))
RED_BAR = pygame.transform.rotate(RED_BAR, 90)

# Music and Sound
MUSIC = pygame.mixer.Sound(os.path.join('asset', 'Music', 'Tobu - Candyland.mp3'))
MUSIC.play()
MUSIC.set_volume(0.6)

HIT_SOUND = pygame.mixer.Sound(os.path.join('asset', 'Sound', 'hit.wav'))
HIT_SOUND.set_volume(0.6)

LOSE_SOUND = pygame.mixer.Sound(os.path.join('asset', 'Sound', 'lose.wav'))
LOSE_SOUND.set_volume(0.6)

sound_move_bar = Scroll(WIDTH // 2 , HEIGHT //2 - 115, RED_BAR)
music_move_bar = Scroll(WIDTH // 2 , HEIGHT //2 - 15, RED_BAR)

def draw_bg(win):
    win.blit(BG_IMAGE, (0, 0))

def level1():
    bricks = []
    for i in range(16):
        brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*i, 4 * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_BLUE, 1 )
        bricks.append(brick)

    return bricks

def level2():
    bricks = []
    for i in range (16):
        if i % 2 == 0:
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*i, 4 * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_BLUE, 1 )
        else:
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*i, 3 * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_GREEN, 2 )
        bricks.append(brick)

    return bricks

def level3():
    bricks = []
    for i1 in range(1,4):
        for i2 in range(3):
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*i1, (i2+3) * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_BLUE, 1)
            bricks.append(brick)

    for j1 in range(6,9):
        for j2 in range(3):
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*j1, (j2+3) * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_GREEN, 2)
            bricks.append(brick)

    for k1 in range(12,15):
        for k2 in range(3):
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*k1, (k2+3) * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_PINK, 3)
            bricks.append(brick)

    return bricks

def level4():
    bricks = []
    for i1 in range(4, 12):
        for i2 in range(2):
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*i1, (i2+8) * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_BLUE, 1)
            bricks.append(brick)

    for j1 in range(5, 11):
        for j2 in range(2):
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*j1, (j2+6) * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_GREEN, 2)
            bricks.append(brick)

    for k1 in range(6, 10):
        for k2 in range(2):
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*k1, (k2+4) * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_PINK, 3)
            bricks.append(brick)
    
    for l1 in range(7, 9):
        for l2 in range(2):
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*l1, (l2+2) * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_VIOLET, 4)
            bricks.append(brick)

    return bricks

def level5():
    bricks = []

    for i1 in range(16):
        for i2 in range(3):
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*i1, (i2+15) * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, BRICK_YELLOW, 5)
            bricks.append(brick)

    return bricks

def level6():

    bricks = []
    image = [BRICK_BLUE, BRICK_GREEN, BRICK_PINK, BRICK_VIOLET, BRICK_YELLOW]
    for i in range (16):        
        for j in range (5):
            brick = Brick(-BRICK_WIDTH_MARGIN + BRICK_WIDTH*i, 0 + (10-j)*BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT, image[j], 1 + 1* j)
            bricks.append(brick)
    return bricks

def handle_bat_movement(bat, keys):
    if keys[pygame.K_a] and bat.x > 0:
        bat.move(False)
    if keys[pygame.K_d] and bat.x < WIDTH - BAT_IMAGE_WIDTH:
        bat.move(True)

def handle_collision(ball, bat, bricks):
    # top
    if ball.y <= 0:
        ball.y_vel *= -1
        HIT_SOUND.play()

    # # left
    if ball.x <= 0:
        ball.x_vel *= -1
        HIT_SOUND.play()

    # # right
    elif ball.x + ball.radius * 2 >= WIDTH:
        ball.x_vel *= -1
        HIT_SOUND.play()

    bottom_ball_x = ball.x + ball.radius
    bottom_ball_y = ball.y + ball.radius*2

    top_ball_x = ball.x + ball.radius
    top_ball_y = ball.y

    left_ball_x = ball.x 
    left_ball_y = ball.y + ball.radius

    right_ball_x = ball.x + ball.radius *2
    right_ball_y = ball.y + ball.radius

    if bat.rect.collidepoint(bottom_ball_x, bottom_ball_y):
        ball.y_vel *= -1
        middle_x = bat.x + bat.width/2
        difference_in_x = middle_x - bottom_ball_x
        reduction_factor= (bat.width / 2) / ball.MAX_VEL
        x_vel = difference_in_x / reduction_factor 
        ball.x_vel = -1 * x_vel
        HIT_SOUND.play()

    if bat.rect.collidepoint(left_ball_x, left_ball_y):
        ball.x_vel += ball.MAX_VEL
        HIT_SOUND.play()

    if bat.rect.collidepoint(right_ball_x, right_ball_y):
        ball.x_vel -= ball.MAX_VEL
        HIT_SOUND.play()

    for brick in bricks:

        if brick.rect.collidepoint(top_ball_x, top_ball_y) or brick.rect.collidepoint(bottom_ball_x, bottom_ball_y):
            ball.y_vel *= -1
            brick.health -= 1
            HIT_SOUND.play()
            
        if brick.rect.collidepoint(left_ball_x, left_ball_y) or brick.rect.collidepoint(right_ball_x, right_ball_y):
            ball.x_vel *= -1
            brick.health -= 1
            HIT_SOUND.play()

        if brick.health <= 0:
            bricks.remove(brick)

def menu(bat, ball):
    play_button = Button(WIDTH // 2 + BUTTON_WIDTH , HEIGHT // 2 , PLAY_BUTTON_IMAGE)
    setting_button = Button(WIDTH // 2 - BUTTON_WIDTH*2 , HEIGHT // 2 , SETTING_BUTTON_IMAGE)
    buy_bonus_button = Button(WIDTH // 2 - BUY_BONUS_WIDTH // 2, HEIGHT // 2 + BUY_BONUS_HEIGHT * 2, BUY_BONUS_IMAGE)
    buttons = [play_button, setting_button, buy_bonus_button]

    run = True

    while run == True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        draw_bg(WIN)
        WIN.blit(MENU, (WIDTH // 2 - MENU_WIDTH //2, MENU_HEIGHT * 2))

        for button in buttons:
            button.draw(WIN)

        if pygame.mouse.get_pressed()[0] == 1:
            mouse_pos = pygame.mouse.get_pos()

            if play_button.check_click(mouse_pos):
                run = False
                pygame.time.delay(500)
                main(bat, ball)
            
            if setting_button.check_click(mouse_pos):
                setting()

            if buy_bonus_button.check_click(mouse_pos):
                bonus(bat, ball)

        pygame.display.update()

def setting():
    ok_button = Button(WIDTH // 2 - OK_WIDTH // 2 , SETTING_BG_HEIGHT + 10 , OK_IMAGE)
    sound_button = Button(WIDTH // 2 - 130, HEIGHT //2 - 130, SOUND_IMAGE, 0.5)
    music_button = Button(WIDTH // 2 - 130, HEIGHT //2 - 30, MUSIC_IMAGE, 0.5)
    sound_bar = Button(WIDTH // 2 - 60, HEIGHT //2 - 115, PINK_BAR)
    music_bar = Button(WIDTH // 2 - 60, HEIGHT //2 - 15, PINK_BAR)

    buttons = [ok_button, sound_button, music_button, sound_bar, music_bar, sound_move_bar, music_move_bar]

    run = True
    while run == True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
    
        draw_bg(WIN)

        WIN.blit(MENU, (WIDTH // 2 - MENU_WIDTH //2, 0))
        WIN.blit(SETTING_BG, (WIDTH // 2 - SETTING_BG_WIDTH //2, MENU_HEIGHT ))
        
        for button in buttons:
            button.draw(WIN)

        if pygame.mouse.get_pressed()[0] == 1:
            mouse_pos = pygame.mouse.get_pos()
            if ok_button.check_click(mouse_pos):
                run = False

            sound_move_bar.scroll(mouse_pos, WIDTH // 2 -60, WIDTH//2 + 120, HIT_SOUND)
            sound_move_bar.scroll(mouse_pos, WIDTH // 2 -60, WIDTH//2 + 120, LOSE_SOUND)
            music_move_bar.scroll(mouse_pos, WIDTH // 2 -60, WIDTH//2 + 120, MUSIC)

        pygame.display.update()
        pygame.display.flip()

def bonus(bat, ball):

    bat_black_button = Bat(100, 150, BAT_IMAGE_WIDTH, BAT_HEIGHT, BAT_BLACK_IMAGE)
    bat_blue_button = Bat(100, 150 + BAT_HEIGHT + 50 , BAT_IMAGE_WIDTH, BAT_HEIGHT, BAT_BLUE_IMAGE)
    bat_orange_button = Bat(100, 150 + (BAT_HEIGHT  + 50) *2, BAT_IMAGE_WIDTH, BAT_HEIGHT , BAT_ORANGE_IMAGE)
    bat_pink_button = Bat(100, 150 + (BAT_HEIGHT + 50) *3, BAT_IMAGE_WIDTH, BAT_HEIGHT, BAT_PINK_IMAGE)
    bat_yellow_button = Bat(100, 150 + (BAT_HEIGHT + 50) *4, BAT_IMAGE_WIDTH, BAT_HEIGHT, BAT_YELLOW_IMAGE)

    ball_blue_button = Ball(300, 150, BALL_IMAGE_RADIUS, BALL_BLUE_IMAGE)
    ball_green_button = Ball(300, 150 + BALL_IMAGE_HEIGHT , BALL_IMAGE_RADIUS, BALL_GREEN_IMAGE)
    ball_orange_button = Ball(300, 150 + BALL_IMAGE_HEIGHT * 2, BALL_IMAGE_RADIUS, BALL_ORANGE_IMAGE)
    ball_red_button = Ball(300 + BALL_IMAGE_WIDTH * 2, 150, BALL_IMAGE_RADIUS, BALL_RED_IMAGE)
    ball_silver_button = Ball(300 + BALL_IMAGE_WIDTH * 2, 150 + BALL_IMAGE_HEIGHT , BALL_IMAGE_RADIUS, BALL_SILVER_IMAGE)
    ball_yellow_button = Ball(300 + BALL_IMAGE_WIDTH * 2, 150 + BALL_IMAGE_HEIGHT * 2, BALL_IMAGE_RADIUS, BALL_YELLOW_IMAGE)

    menu_button = Button(WIDTH //2 - MENU_WIDTH //2, HEIGHT - MENU_HEIGHT, MENU)
    play_button = Button(WIDTH //2 + MENU_WIDTH, HEIGHT - BUTTON_HEIGHT, PLAY_BUTTON_IMAGE)

    bat_buttons = [bat_black_button, bat_blue_button, bat_orange_button, bat_pink_button, bat_yellow_button]
    ball_buttons = [ball_blue_button, ball_green_button, ball_orange_button, ball_red_button, ball_silver_button, ball_yellow_button]
    buttons = [menu_button, play_button]

    run = True
    while run == True:

        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        draw_bg(WIN)
        WIN.blit(BUY_BONUS_BG, (0, 100))
        menu_button.draw(WIN)

        for button in buttons:
            button.draw(WIN)

        for bat_button in bat_buttons:
            bat_button.draw(WIN)

        for ball_button in ball_buttons:
            ball_button.draw(WIN)

        if pygame.mouse.get_pressed()[0] == 1:
            mouse_pos = pygame.mouse.get_pos()
            if menu_button.check_click(mouse_pos):
                run = False
                bat.reset()
                ball.reset()
                menu(bat, ball)

            if play_button.check_click(mouse_pos):
                run = False

            for i, bat_button in enumerate(bat_buttons):
                if bat_button.check_click(mouse_pos):
                    bat_image = BAT_IMAGES[i]
                    bat.image = bat_image

            for j, ball_button in enumerate(ball_buttons):
                if ball_button.check_click(mouse_pos):
                    ball_image = BALL_IMAGES[j]
                    ball_image = pygame.transform.scale(ball_image, (BALL_WIDTH, BALL_HEIGHT))
                    ball.image = ball_image

        pygame.display.update()

def main(bat, ball):
    level = [level1(), level2(), level3(), level4(), level5(), level6()]
    level_num = 1
    bricks = level[level_num - 1]

    # Button
    play_button = Button(BUTTON_WIDTH* 0.5, 0, PLAY_BUTTON_IMAGE, 0.5)
    setting_button = Button(0, 0, SETTING_BUTTON_IMAGE, 0.5)
    buy_bonus_button = Button(0, HEIGHT - BUY_BONUS_HEIGHT//2, BUY_BONUS_IMAGE, 0.5)
    buttons = [play_button, setting_button, buy_bonus_button]

    run = True
    
    while run == True:

        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()

        if pygame.mouse.get_pressed()[0] == 1:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.check_click(mouse_pos):
                main(bat, ball)
            if setting_button.check_click(mouse_pos):
                setting()
            if buy_bonus_button.check_click(mouse_pos):
                bonus(bat, ball)

        draw_bg(WIN)
        for brick in bricks:
            brick.draw(WIN)
            brick.update()
        bat.draw(WIN)
        ball.draw(WIN)
        ball.move()
        for button in buttons:
            button.draw(WIN)
        
        # Lose case
        lose = False
        if ball.y > HEIGHT:
            lose = True
            lose_text = "You lose!"
        if lose:
            text = LOSE_FONT.render(lose_text, 1 ,WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() //2))
            LOSE_SOUND.play()
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
            bat.reset()
            ball.reset()
            brick = level[level_num - 1]
            menu(bat, ball)

        # Passing level
        if bricks == []:
            bat.reset()
            ball.reset()
            WIN.blit(LEVEL_COMPLETE_IMAGE, (WIDTH//2 - LEVEL_WIDTH // 2, HEIGHT // 2 - LEVEL_HEIGHT //2))
            pygame.display.update()
            pygame.time.delay(3000)

            level_num += 1
            bricks = level[level_num - 1]
            
        handle_bat_movement(bat, keys)
        handle_collision(ball, bat, bricks)

        pygame.display.update()

if __name__ == "__main__":
    bat = Bat(WIDTH // 2 - BAT_IMAGE.get_width() / 2, HEIGHT - BAT_IMAGE_HEIGHT, BAT_IMAGE_WIDTH, BAT_HEIGHT, BAT_IMAGE)
    ball = Ball(WIDTH // 2 - BALL_IMAGE.get_width() / 2, HEIGHT - BAT_HEIGHT_BOTTOM_MARGIN - BAT_HEIGHT * 3 , BALL_RADIUS, BALL_IMAGE)
    menu(bat, ball)
