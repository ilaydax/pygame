import pygame
from plyr import Player
from pltfrm import Platform
from monster import Monster
from bullet import Bullet
import cnfg
import random
from menu import main_menu  # Menü ekranını içe aktarıyoruz

# Önce menü ekranını aç
main_menu()  # Kullanıcı "Play" tuşuna basana kadar burada kalır

pygame.init()
screen = pygame.display.set_mode((cnfg.SCREEN_WIDTH, cnfg.SCREEN_HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load(cnfg.BACKGROUND_IMAGE)
background_width, background_height = background.get_size()

scroll_x = 0

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
running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    scroll_x -= cnfg.BACKGROUND_SCROLL_SPEED
    if scroll_x <= -background_width:
        scroll_x = 0

    # Arka plan kaydırma
    screen.blit(background, (scroll_x, 0))
    screen.blit(background, (scroll_x + background_width, 0))

    # Canavarlar ve ateş etme
    current_time = pygame.time.get_ticks()
    for monster in monsters:
        bullet = monster.update(current_time)
        if bullet:
            bullets.append(bullet)
        monster.draw(screen)

    # Mermileri hareket ettirme
    for bullet in bullets[:]:
        bullet.move()
        bullet.draw(screen)
        if bullet.off_screen():
            bullets.remove(bullet)

    # Karakter ve platformları çizme
    player.update(keys, screen, platforms)
    for platform in platforms:
        platform.draw(screen)

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

    if player.game_over:
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (cnfg.SCREEN_WIDTH // 2 - 150, cnfg.SCREEN_HEIGHT // 2 - 50))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
