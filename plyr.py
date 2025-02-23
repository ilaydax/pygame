import pygame

class Player:
    def __init__(self):
        self.idle_image = pygame.image.load('lkn_images/player_idle.png').convert_alpha()
        self.idle_image = pygame.transform.scale(self.idle_image, (40, 70))
        self.original_image = self.idle_image
        self.rect = self.idle_image.get_rect(midbottom=(100, 300))
        self.velocity_y = 0  # Düşüş hızı
        self.gravity = 0.8  # Yerçekimi
        self.jump_power = -15  # Zıplama gücü
        self.speed = 5  # Hız
        self.facing_left = False
        self.on_ground = False  # Yerde mi kontrolü
        self.game_over = False  # Oyun bitme durumu

        self.color = (255, 0, 0)  # Burada renk tanımlaması ekledim (kırmızı)

    def jump(self):
        """Karakter zıplamak için çağrılır."""
        if self.on_ground:  # Yerdeyse zıplar
            self.velocity_y = self.jump_power  # Zıplama hızı
            self.on_ground = False  # Zıpladı, artık yerde değil

    def apply_gravity(self, platforms):
        """Yer çekimi uygular ve platformlara çarpışmayı kontrol eder."""
        if not self.on_ground:  # Yerde değilse yerçekimi etkili olmalı
            self.velocity_y += self.gravity  # Yerçekimini uygula
        self.rect.y += self.velocity_y  # Yüksekliği güncelle

        self.on_ground = False  # Başlangıçta yerle temasta değil

        for platform in platforms:
            if self.rect.colliderect(platform.rect):  # Platforma çarpma kontrolü
                if self.velocity_y > 0:  # Aşağıya düşüyorsa
                    self.rect.bottom = platform.rect.top  # Platforma oturur
                    self.velocity_y = 0  # Düşüş hızı sıfırlanır
                    self.on_ground = True  # Yerde olduğunu işaretle

                    # Eğer en alt platforma inerse, oyun biter
                    if platform.rect.top == 550:  # En alttaki platformun yüksekliği
                        self.game_over = True
                        return  # Artık daha fazla işlem yapmasına gerek yok

                elif self.velocity_y < 0:  # Eğer yukarı doğru hareket ediyorsa (başını çarptıysa)
                    self.rect.top = platform.rect.bottom  # Başını platforma çarptıysa
                    self.velocity_y = 0  # Hız sıfırlanır

        # Eğer karakter tamamen düşerse GAME OVER
        if self.rect.top > 600:
            self.game_over = True

    def move(self, keys):
        """Sağa ve sola hareketi işler."""
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed  # Sol hareket
            if not self.facing_left:
                self.idle_image = pygame.transform.flip(self.original_image, True, False)
                self.facing_left = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed  # Sağ hareket
            if self.facing_left:
                self.idle_image = self.original_image
                self.facing_left = False

    def draw(self, screen):
        """Ekrana karakteri çizer."""
        screen.blit(self.idle_image, self.rect)

    def update(self, keys, screen, platforms):
        """Karakterin her karede güncellenmesini sağlar."""
        if not self.game_over:  # Eğer oyun bitmediyse güncelleme devam eder
            if keys[pygame.K_SPACE]:  # Zıplama
                self.jump()

            self.apply_gravity(platforms)  # Yerçekimini uygula
            self.move(keys)  # Hareket et
            self.draw(screen)  # Karakteri çiz

        # Eğer renkli kutu çizmeyi istiyorsan aşağıdaki satırı ekleyebilirsin
        # pygame.draw.rect(screen, self.color, self.rect)  # Renkli kutu (isteğe bağlı) 