# aparat: www.aparat.com/arta_code.com

# 1- imports
import pygame
from time import sleep

# 2- start_pygame
pygame.init()

# 3- settings_for_game_screen
display_width = 800
display_hight = 600
gameDisplay = pygame.display.set_mode((display_width, display_hight))

# name_game
pygame.display.set_caption("ColorKey")

# color
color = (0, 0, 0)

#clock
clock = pygame.time.Clock()

# Exit
Exit = False

# 4- game_loop
while not Exit:
    # 5- quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True

        # 7- Key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            if event.key == pygame.K_g:
                color = (0, 255, 0)
            if event.key == pygame.K_b:
                color = (0, 0, 255)
            if event.key == pygame.K_w:
                color = (255, 255, 255)
            if event.key == pygame.K_y:
                color = (255, 255, 0)
            if event.key == pygame.K_SPACE:
                color = (0, 0, 0)
                sleep(1)
                Exit = True
        
    # 6- update
    # color_screen
    gameDisplay.fill(color)
    # update_screen
    clock.tick(60)
    pygame.display.update()


# quit
pygame.quit()
quit()