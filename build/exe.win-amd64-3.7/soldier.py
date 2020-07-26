import pygame
from pygame.sprite import Sprite


class Soldier(Sprite):

    def __init__(self, ai_settings, screen):
        """Inicjalizacja żołnierza i jego położenie początkowe."""
        super(Soldier, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        

        # Wczytanie obrazu żołnierza i pobranie jego prostokąta.
        self.image = pygame.image.load('images/p.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Każdy nowy żołnierz pojawia się na dole ekranu.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


        self.center = float(self.rect.centerx)      

        self.move_right = False  
        self.move_left = False

    def blitme(self):
        """Wyświetlenie żołnierza w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Aktualizacja położenia żołnierza"""

        #pierwszy warunek: jeśli parametr ruchu w lewo/prawo jest True
        #drugi warunek: jeśli obiekt znajduje się w ramce projektu
        if self.move_right and self.rect.right < self.screen_rect.right: 
            self.center += self.ai_settings.soldier_speed

        if self.move_left and self.rect.left > 0:
            self.center -= self.ai_settings.soldier_speed

        self.rect.centerx = self.center

    
        
class Eagle(Sprite):

    def __init__(self, ai_settings, screen):
        
        super(Eagle, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        

        # Wczytanie obrazu żołnierza i pobranie jego prostokąta.
        self.image = pygame.image.load('images/eagle.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


