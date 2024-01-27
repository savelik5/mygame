import pygame

pygame.init()

screen_width = 700
screen_height = 900
screen = pygame.display.set_mode((screen_height, screen_width))
GREEN = pygame.Color(45, 215, 0)
RED = pygame.Color(255, 0, 0)
font = pygame.font.Font("./OpenSans_Condensed-ExtraBoldItalic.ttf", 50)
text = font.render("Super Mario Odyssey",True, RED)

ORANGE = pygame.Color(255, 110, 40)
font2 = pygame.font.Font("./OpenSans_Condensed-MediumItalic.ttf", 50)
text2 = font2.render("Super Mario Odyssey 2",True, ORANGE)

FPS = 120  

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(GREEN)        
    screen.blit(text, (100, 100))
    screen.blit(text2, (300, 300))
        
    pygame.display.update()

    clock.tick(FPS)


pygame.quit() 