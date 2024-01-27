# screen.set_at((x, y), pygame.Color(0,int(x/screen_width*255),int(x/screen_width*255)))
import pygame

pygame.init()
colors_list = [pygame.Color(18, 192, 233), pygame.Color(196, 113, 237), pygame.Color(246, 79, 89)]

screen_width =700
screen_height = 700
screen = pygame.display.set_mode((screen_height, screen_width))

FPS = 120  

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for y in range(700):
        for x in range(screen_width):          
            index = int(x / screen_width * (len(colors_list) - 1)) 
            color1 = colors_list[index] 
            color2 = colors_list[index + 1]
            r = int((x % (screen_width // (len(colors_list) - 1))) / (screen_width // (len(colors_list) - 1)) * (color2.r - color1.r) + color1.r) 
            g = int((x % (screen_width // (len(colors_list) - 1))) / (screen_width // (len(colors_list) - 1)) * (color2.g - color1.g) + color1.g) 
            b = int((x % (screen_width // (len(colors_list) - 1))) / (screen_width // (len(colors_list) - 1)) * (color2.b - color1.b) + color1.b)
            screen.set_at((x, y), pygame.Color(r,g,b))
            
        
    pygame.display.update()

    clock.tick(FPS)


pygame.quit() 