import pygame
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect=pygame.Rect(x, y, width, height) 
        self.text=text
        self.action=action
        self.font=pygame.font.Font(None) 

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)
        text_surface = self.font.render(self.text, True, GREEN)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)