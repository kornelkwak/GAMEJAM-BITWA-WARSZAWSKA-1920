import pygame, sys, os
from random import randint
class Settings():
    """Klasa z całymi ustawieniami gry"""


    #Inicjacja ustawień gry
    def __init__(self):

        #Gra
        self.level = 1
        self.win = False

        #Okno
        self.screen_width = 1366
        self.screen_height = 768

        self.bg_list = ['images/okopy1.png','images/okopy2.png','images/okopy3.png','images/okopy4.png','images/okopy5.png','images/okopy6.png','images/okopy7.png','images/okopy8.png',
        'images/okopy9.png','images/okopy10.png', 'images/okopy10.png']
        
        self.bg_color = loadify(self.bg_list[self.level - 1])
        
        self.bg_color = pygame.transform.scale(self.bg_color, (1366, 768))
        
        
        #Pocisk
        
        self.bullet_width = 3
        self.bullet_height = 9
        self.bullet_color = 255, 232, 0
        self.bullet_allowed = 3 #ograniczenie ilości pocisków na ekranie

    

        #kierunek -> 1 prawo, -1 w lewo
        self.enemy_direction = 1
        self.group_speed = randint(6, 10)

        #Player
        self.player_chance = 3
        self.points = 0
        self.speedup_scale = 1.1
        

        self.soldier_speed = 2
        self.enemy_speed = 2
        self.bullet_speed = 3
        

def loadify(img):
    return pygame.image.load(img).convert_alpha()

    



