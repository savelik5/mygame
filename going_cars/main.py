import random
import time
import pygame

pygame.init()

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
FPS = 120

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("going cars")

car_width = 80
car_height = 100

#car, background, lines_on_road, intro_background
# car = pygame.image.load("asphalt-027.jpg")



clock = pygame.time.Clock()
paused = False


def intro():
    print("Это меню игры")


def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        

        pygame.display.update()

        clock.tick(FPS)

intro()
game_loop()
pygame.quit() 

