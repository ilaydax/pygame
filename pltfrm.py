import pygame

class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height) 
        self.color = (255, 182, 193)  

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect) 