import random
import time
import pygame

pygame.init()

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
FPS = 120

screen_width = 1100
screen_height = 618.75
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("going cars")

car_width = 80
car_height = 100

#car, background, lines_on_road, intro_background
# car = pygame.image.load("")
intro_background_img = pygame.image.load("intro_background.jpg")
intro_background = pygame.transform.scale(intro_background_img, (1100, 618.75))




clock = pygame.time.Clock()
paused = False

# создание Объекта Текст
def text_object(text, font):
    text_render = font.render(text, True, WHITE)
    return text_render, text_render.get_rect()




# интро
def intro():
    print("Это меню игры")
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        screen.blit(intro_background,(0,0))
        font = pygame.font.Font("./OpenSans_Condensed-ExtraBoldItalic.ttf", 50)
        start_text, start_text_rect = text_object("GOING CARS", font)
        screen.blit(start_text, start_text_rect)
        
        

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

