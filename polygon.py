import pygame

pygame.init()

screen_width = 1100
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

GREEN = pygame.Color(45, 215, 0)
FPS = 120  

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.polygon(screen, GREEN, ((100,400),(104, 170),(140,101)))
    pygame.draw.polygon(screen, GREEN, ((100,400),(104, 170),(140,101)))
    pygame.draw.polygon(screen, GREEN, ((109,480),(174, 890),(190,191)))
    pygame.display.update()

    clock.tick(FPS)


pygame.quit() 