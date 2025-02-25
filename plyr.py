from pygame import Rect

class Player:
    def __init__(self):
        # Pygame Zero'da görüntü yükleme
        self.idle_image = 'player_idle'  # 'player_idle.png' dosyası images klasöründe olmalı
        self.original_image = self.idle_image
        self.rect = Rect(100, 300, 40, 70)  # Karakterin boyutları (40x70)
        self.velocity_y = 0  # Düşüş hızı
        self.gravity = 0.8  # Yerçekimi
        self.jump_power = -15  # Zıplama gücü
        self.speed = 5  # Hız
        self.facing_left = False
        self.on_ground = False  # Yerde mi kontrolü
        self.game_over = False  # Oyun bitme durumu

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
        if keys["left"] or keys["a"]:  # Sol hareket
            self.rect.x -= self.speed
            if not self.facing_left:
                self.idle_image = self.original_image + '_flipped'  # Görüntüyü ters çevir
                self.facing_left = True
        if keys["right"] or keys["d"]:  # Sağ hareket
            self.rect.x += self.speed
            if self.facing_left:
                self.idle_image = self.original_image  # Görüntüyü düz hale getir
                self.facing_left = False

    def draw(self):
        """Ekrana karakteri çizer."""
        screen.blit(self.idle_image, self.rect.topleft)  # Pygame Zero'da blit işlemi

    def update(self, keys, platforms):
        """Karakterin her karede güncellenmesini sağlar."""
        if not self.game_over:  # Eğer oyun bitmediyse güncelleme devam eder
            if keys["space"]:  # Zıplama
                self.jump()

            self.apply_gravity(platforms)  # Yerçekimini uygula
            self.move(keys)  # Hareket et
            self.draw()  # Karakteri çiz