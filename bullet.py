# bullet.py (Yukarı doğru hareket eden mermi)
import pygame

class Bullet:
    def __init__(self, x, y, direction="up"):
        self.image = pygame.image.load('lkn_images/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5  # Mermi hızını ayarlıyoruz
        self.direction = direction  # Merminin yönü

    def move(self):
        """Merminin hareket etmesini sağlar."""
        if self.direction == "up":
            self.rect.y -= self.speed  # Yukarı doğru hareket
        else:
            self.rect.x += self.speed  # Sağa doğru hareket (varsayılan)

    def draw(self, screen):
        """Mermiyi ekrana çizer."""
        screen.blit(self.image, self.rect)

    def off_screen(self):
        """Mermi ekrandan çıktığında True döner."""
        if self.direction == "up":
            return self.rect.y < 0  # Yukarı doğru çıkarsa
        else:
            return self.rect.x > pygame.display.get_surface().get_width()  # Sağa doğru çıkarsa