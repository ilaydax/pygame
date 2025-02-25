from pygame import Rect  

class Platform:
    def __init__(self, x, y, width, height):
        self.rect = Rect(x, y, width, height)  # Rect sınıfını kullanarak platformun dikdörtgenini oluşturuyoruz
        self.color = (255, 182, 193)  # Platformun rengi (pembe)

    def draw(self):
        # Pygame Zero'da çizim işlemleri için `screen.draw.filled_rect` kullanılır
        screen.draw.filled_rect(self.rect, self.color)