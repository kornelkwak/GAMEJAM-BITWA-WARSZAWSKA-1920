import pygame
from pygame.sprite import Sprite
from random import randint

class Enemy(Sprite):
    """Klasa pojedynczego Bolszewika"""
    def __init__(self, ai_settings, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        images_list=  ['images/b1.png','images/b2.png','images/b3.png']
        random_image = images_list[randint(0,2)]
        self.image = pygame.image.load(random_image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.speed = ai_settings.enemy_speed

    def blitme(self):
        """Wyświetlenie bolszewika w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)

    def update(self, ai_settings):
        """Poruszanie wroga"""
        #zmiana współrzędnych wrogów
        self.x += (self.ai_settings.enemy_speed * self.ai_settings.enemy_direction)
        self.rect.x = self.x
        
    def screen_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    