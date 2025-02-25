from plyr import Player
from pltfrm import Platform
from monster import Monster
from bullet import Bullet
import random
from menu import main_menu  # Menü ekranını içe aktarıyoruz

# Pygame Zero ayarları
WIDTH = 800  # Ekran genişliği
HEIGHT = 600  # Ekran yüksekliği
TITLE = "Platformer Game"  # Oyun başlığı

# Önce menü ekranını aç
main_menu()  # Kullanıcı "Play" tuşuna basana kadar burada kalır

# Arka plan resmi
background = "background"  # 'background.png' dosyası images klasöründe olmalı

# Oyuncu nesnesi
player = Player()

# Başlangıç platformları
platforms = [
    Platform(0, 550, 800, 20),  # En alt platform (zemin)
    Platform(100, 450, 100, 20),
    Platform(300, 350, 100, 20),
    Platform(500, 250, 100, 20),
    Platform(700, 150, 100, 20)
]

# Canavarların yerleşimi
monsters = [
    Monster(random.randint(platforms[1].rect.right, platforms[2].rect.left), platforms[0].rect.top - 10),
    Monster(random.randint(platforms[2].rect.right, platforms[3].rect.left), platforms[0].rect.top - 10),
    Monster(random.randint(platforms[3].rect.right, platforms[4].rect.left), platforms[0].rect.top - 10)
]

# Yeni platform oluşturma fonksiyonu
def generate_new_platform():
    last_platform = platforms[-1]
    min_gap, max_gap = 150, 300
    new_x = random.randint(last_platform.rect.x + min_gap, last_platform.rect.x + max_gap)
    new_y = random.randint(100, 400)
    new_platform = Platform(new_x, new_y, 100, 20)
    
    for platform in platforms:
        if new_platform.rect.colliderect(platform.rect):
            return generate_new_platform()
    
    # Yeni platform üzerine canavar ekleyelim
    monsters.append(Monster(random.randint(new_platform.rect.right, new_platform.rect.right + 200), platforms[0].rect.top - 40))
    
    return new_platform

# Bullet ve Monster listeleri
bullets = []
platforms_passed = 0
current_time = 0  # Zamanlama için sayaç

def draw():
    """Ekrana her şeyi çizer."""
    screen.blit(background, (0, 0))  # Arka planı çiz

    # Canavarlar ve mermiler
    for monster in monsters:
        monster.draw()
    for bullet in bullets:
        bullet.draw()

    # Platformlar ve oyuncu
    for platform in platforms:
        platform.draw()
    player.draw()

    # Game over durumu
    if player.game_over:
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2), color=(255, 0, 0), fontsize=74)

def update():
    """Oyunun her karede güncellenmesini sağlar."""
    global platforms_passed, current_time

    if not player.game_over:
        keys = keyboard  # Klavye girişlerini al

        # Zamanlayıcıyı güncelle
        current_time += 1

        # Canavarlar ve ateş etme
        for monster in monsters:
            if current_time % 60 == 0:  # Her 60 karede bir ateş et
                bullet = monster.shoot()
                if bullet:
                    bullets.append(bullet)

        # Mermileri hareket ettirme
        for bullet in bullets[:]:
            bullet.move()
            if bullet.off_screen():
                bullets.remove(bullet)

        # Oyuncuyu güncelle
        player.update(keys, platforms)

        # Yeni platform oluşturma
        if player.rect.bottom <= platforms[-1].rect.top:
            platforms_passed += 1
            if platforms_passed >= 2:
                new_platform = generate_new_platform()
                platforms.append(new_platform)
                platforms_passed = 0

        # Game over kontrolü
        for bullet in bullets:
            if player.rect.colliderect(bullet.rect):
                player.game_over = True
                break

def on_mouse_down(pos):
    """Fare tıklamasını işler."""
    pass  # Fare tıklamaları için gerekirse buraya kod ekleyebilirsiniz