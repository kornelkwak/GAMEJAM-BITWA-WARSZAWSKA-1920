import pygame
from pygame.sprite import Sprite
from enemy import Enemy

class Bullet(Sprite):
    """Klasa zarządzająca kulami żołnierza"""

    def __init__(self, ai_settings, screen, soldier):
        """Utworzenie pocisku"""
        super(Bullet, self).__init__()
        self.screen = screen

        #Utworzenie pocisku o współrzędnych 0,0 i wymiarach z settings
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width,ai_settings.bullet_height)
        #Przeniesienie pocisku na inne miejsce (środek obiektu Soldier)
        self.rect.centerx = soldier.rect.centerx
        self.rect.top = soldier.rect.top

        # zamiana położenia współrzędnej y pocisku i zamiana na float (ze względu na zmienioną szybkość)
        self.y = float(self.rect.y)

        #pobranie parametrów pocisku - szybkość, kolor z klasy Settings
        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        """Poruszanie pocisku"""
        #zmiana współrzędnych pocisku
        self.y -= self.speed
        self.rect.y = self.y



    def draw_bullet(self):
        """Wyswietlenie pocisku na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    


