import pygame

pygame.init()

screen_width = 750
screen_height = 1000

FPS = 120  
GREEN = (0,255,0) 
clock = pygame.time.Clock()

background = pygame.image.load("2.jpg")
background_rect = background.get_rect()

bee = pygame.image.load("dance-2.png")
bee_rect = bee.get_rect()

screen = pygame.display.set_mode((screen_height, screen_width))
running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        bee_rect.y-=2
    if keys[pygame.K_s]:
        bee_rect.y+=2
    if keys[pygame.K_a]:
        bee_rect.x-=2
    if keys[pygame.K_d]:
        bee_rect.x+=2
    if keys[pygame.K_SPACE]:
        paused = not paused
        
    if paused:
        screen.fill(GREEN)
        bee_rect.x = 0
        bee_rect.y = 0
    else:


        screen.blit(background, background_rect)
        screen.blit(bee, bee_rect)
        
        pass
        
    pygame.display.update()

    clock.tick(FPS)


pygame.quit()

















