from pygame import Rect  

class Bullet:
    def __init__(self, x, y, direction="up"):
        # Pygame Zero'da görüntü yükleme
        self.image = 'bullet'  # 'bullet.png' dosyası images klasöründe olmalı
        self.rect = Rect(x, y, 10, 20)  # Merminin boyutları (10x20)
        self.speed = 5  # Mermi hızını ayarlıyoruz
        self.direction = direction  # Merminin yönü

    def move(self):
        """Merminin hareket etmesini sağlar."""
        if self.direction == "up":
            self.rect.y -= self.speed  # Yukarı doğru hareket
        else:
            self.rect.x += self.speed  # Sağa doğru hareket (varsayılan)

    def draw(self):
        """Mermiyi ekrana çizer."""
        screen.blit(self.image, self.rect.topleft)  # Pygame Zero'da blit işlemi

    def off_screen(self):
        """Mermi ekrandan çıktığında True döner."""
        if self.direction == "up":
            return self.rect.y < 0  # Yukarı doğru çıkarsa
        else:
            return self.rect.x > screen.width  # Sağa doğru çıkarsa