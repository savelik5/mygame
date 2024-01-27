import pygame

pygame.init()

screen_width = 500
screen_height = 500
colors_list = [pygame.Color(18, 192, 233), pygame.Color(196, 113, 237), pygame.Color(246, 79, 89)]
FPS = 120  
GREEN = (0,255,0) 
clock = pygame.time.Clock()

background = pygame.image.load("Flowers.jpg")
background_rect = background.get_rect()

bee = pygame.image.load("bee-2.png")
bee_rect = bee.get_rect()
screen = pygame.display.set_mode((screen_height, screen_width))
for y in range(700):
    for x in range(screen_width):          
        index = int(x / screen_width * (len(colors_list) - 1)) 
        color1 = colors_list[index] 
        color2 = colors_list[index + 1]
        r = int((x % (screen_width // (len(colors_list) - 1))) / (screen_width // (len(colors_list) - 1)) * (color2.r - color1.r) + color1.r) 
        g = int((x % (screen_width // (len(colors_list) - 1))) / (screen_width // (len(colors_list) - 1)) * (color2.g - color1.g) + color1.g) 
        b = int((x % (screen_width // (len(colors_list) - 1))) / (screen_width // (len(colors_list) - 1)) * (color2.b - color1.b) + color1.b)
        screen.set_at((x, y), pygame.Color(r,g,b))

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
        
    
    
    
        
    screen.blit(bee, bee_rect)
        
        
        
    pygame.display.update()

    clock.tick(FPS)


pygame.quit()

















