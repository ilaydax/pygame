import pygame

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 50)
    menu_running = True
    music_on = True
    
    # Arka plan resmi yükleme
    background = pygame.image.load("lkn_images/main_background.png")
    background = pygame.transform.scale(background, (800, 600))
    
    # Müzik başlatma
    pygame.mixer.init()
    pygame.mixer.music.load("lkn_music/background_music.mp3")
    pygame.mixer.music.play(-1)

    while menu_running:
        screen.blit(background, (0, 0))
        
        # Butonlar
        play_button = pygame.Rect(300, 200, 200, 50)
        music_button = pygame.Rect(300, 300, 200, 50)
        exit_button = pygame.Rect(300, 400, 200, 50)
        
        pygame.draw.rect(screen, (100, 50, 150), play_button, border_radius=15)
        pygame.draw.rect(screen, (80, 40, 120), music_button, border_radius=15)
        pygame.draw.rect(screen, (150, 50, 100), exit_button, border_radius=15)
        
        screen.blit(font.render("Play", True, (255, 255, 255)), (360, 210))
        screen.blit(font.render("Music: " + ("On" if music_on else "Off"), True, (255, 255, 255)), (310, 310))
        screen.blit(font.render("Exit", True, (255, 255, 255)), (360, 410))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return  # Oyuna başla
                if music_button.collidepoint(event.pos):
                    music_on = not music_on
                    if music_on:
                        pygame.mixer.music.play(-1)
                    else:
                        pygame.mixer.music.stop()
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()

if __name__ == "__main__":
    main_menu()
