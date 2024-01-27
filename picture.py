import pygame
from pygame.locals import *
pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_height, screen_width))
RED = pygame.Color(255, 255,0)
FPS = 120  
click_time_click = 0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if click_time_click == 0:
                point1 = pygame.mouse.get_pos()
            else: 
                point2 = pygame.mouse.get_pos()
            click_time_click += 1
            if click_time_click > 1:
                pygame.draw.line(screen, RED,point1, point2, 55)
                click_time_click = 0


    
        
    pygame.display.update()

    clock.tick(FPS)


pygame.quit()