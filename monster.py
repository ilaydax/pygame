# monster.py (Yukarı doğru ateş etme)
import pygame
from bullet import Bullet

class Monster:
    def __init__(self, x, y):
        self.image = pygame.image.load('lkn_images/monster.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.shoot_timer = 0
        self.shoot_interval = 1000  # Ateş etme aralığı (ms)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self):
        """Canavar ateş ettiğinde mermi oluşturur."""
        bullet = Bullet(self.rect.centerx, self.rect.centery, direction="up")  # Yukarı doğru ateş et
        return bullet

    def update(self, current_time):
        """Canavarın ateş etme zamanlamasını kontrol eder."""
        if current_time - self.shoot_timer > self.shoot_interval:
            self.shoot_timer = current_time
            return self.shoot()  # Mermiyi döndürür
        return None