import pygame

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_height, screen_width))

FPS = 120  
WHITE = pygame.Color(0,245,255)

clock = pygame.time.Clock()
running = True

def DrawStar(x, y, size):
    pygame.draw.rect(screen, WHITE, (x, y, size, size))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    DrawStar(20, 30, 40)
    
        
    pygame.display.update()

    clock.tick(FPS)


pygame.quit()