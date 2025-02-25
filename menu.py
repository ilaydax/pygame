from pygame import Rect 
from pgzero.builtins import music

def main_menu():
    # Pygame Zero'da ekran boyutu ve başlık ayarlama
    WIDTH = 800
    HEIGHT = 600
    TITLE = "Main Menu"

    # Arka plan resmi yükleme
    background = "main_background"  # 'main_background.png' dosyası images klasöründe olmalı

    # Müzik ayarları
    music_on = True
    music.play("background_music")  # 'background_music.mp3' dosyası music klasöründe olmalı

    def draw():
        """Ekrana menüyü çizer."""
        screen.blit(background, (0, 0))  # Arka planı çiz

        # Butonlar
        play_button = Rect(300, 200, 200, 50)
        music_button = Rect(300, 300, 200, 50)
        exit_button = Rect(300, 400, 200, 50)

        screen.draw.filled_rect(play_button, (100, 50, 150))  # Play butonu
        screen.draw.filled_rect(music_button, (80, 40, 120))  # Music butonu
        screen.draw.filled_rect(exit_button, (150, 50, 100))  # Exit butonu

        screen.draw.text("Play", center=play_button.center, color=(255, 255, 255), fontsize=30)
        screen.draw.text("Music: " + ("On" if music_on else "Off"), center=music_button.center, color=(255, 255, 255), fontsize=30)
        screen.draw.text("Exit", center=exit_button.center, color=(255, 255, 255), fontsize=30)

    def on_mouse_down(pos):
        """Fare tıklamasını işler."""
        nonlocal music_on

        play_button = Rect(300, 200, 200, 50)
        music_button = Rect(300, 300, 200, 50)
        exit_button = Rect(300, 400, 200, 50)

        if play_button.collidepoint(pos):
            return  # Oyuna başla
        if music_button.collidepoint(pos):
            music_on = not music_on
            if music_on:
                music.play("background_music")
            else:
                music.stop()
        if exit_button.collidepoint(pos):
            exit()  # Oyundan çık

    # Pygame Zero'da ana döngü otomatik olarak çalışır