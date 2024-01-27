import pygame
import sys
pygame.init()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("Flowers.jpg")
background_rect = background.get_rect()

RED = pygame.Color(255, 25, 55)
GREEN = pygame.Color(25, 255, 55)

font = pygame.font.Font("./OpenSans_Condensed-ExtraBoldItalic.ttf", 70)
FPS = 120  

class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect=pygame.Rect(x, y, width, height) 
        self.text=text
        self.action=action
        self.font=pygame.font.Font("./OpenSans_Condensed-ExtraBoldItalic.ttf", 70)

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)
        text_surface = self.font.render(self.text, True, GREEN)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def click(self, pos):
        return self.rect.collidepoint(pos)


    
play_button = Button(500, 200, 200, 80, "play")
quit_button = Button(500, 300, 200, 80, "quit", action=sys.exit)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        # Кнопка выхода на comand_q
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
             
        # Кнопка выхода на встроенную кнопку
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.click(mouse_pos):
                print("auouo")
            elif quit_button.click(mouse_pos):
                print("Кнопка нажата!")
                quit_button.action()

    screen.blit(background, background_rect)
    
    play_button.draw()
    quit_button.draw()    
    pygame.display.update()

    clock.tick(FPS)


pygame.quit() 