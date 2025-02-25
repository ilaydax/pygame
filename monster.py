from pygame import Rect  
from bullet import Bullet  

class Monster:
    def __init__(self, x, y):
        # Pygame Zero'da görüntü yükleme
        self.image = 'monster'  # 'monster.png' dosyası images klasöründe olmalı
        self.rect = Rect(x, y, 40, 40)  # Canavarın boyutları (40x40)
        self.shoot_timer = 0
        self.shoot_interval = 1000  # Ateş etme aralığı (ms)

    def draw(self):
        """Canavarın ekrana çizilmesini sağlar."""
        screen.blit(self.image, self.rect.topleft)  # Pygame Zero'da blit işlemi

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