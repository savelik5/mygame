import random
import time
import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

car_width = 80
car_height = 100

#car, background, lines_on_road, intro_background
car = pygame.image.load("Asphalt-027.jpg")

pygame.display.set_caption("going cars")

FPS = 120  

clock = pygame.time.Clock()
paused = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
        
    pygame.display.update()

    clock.tick(FPS)


pygame.quit() 