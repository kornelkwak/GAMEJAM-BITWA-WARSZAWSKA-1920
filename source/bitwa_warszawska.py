import pygame

from pygame.sprite import Group
from settings import Settings
from soldier import Soldier, Eagle
import game as g
from score import Scores
from stats import GameStats
from pygame import mixer


FPS = 60 
fpsClock = pygame.time.Clock()


def main():
    mixer.music.load('sound/game.mp3')
    mixer.music.play(-1)
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    #Utworzenie ekranu rozgrywki
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN)  
    
    pygame.display.set_caption("GRA")
    

    eagle = Eagle(ai_settings, screen)
    #Utworzenie obiektu żołnierz
    soldier = Soldier(ai_settings, screen)
    #obiekt Group w której bedzie przechowywana grupa pocisków
    bullets = Group()
    enemies = Group()

    scoreboard = Scores(ai_settings, screen, stats)

    

    #wywołanie funkcji tworzącej całą grupę przeciwników
    g.create_group(ai_settings, screen, soldier, enemies)
    
    #Rozpoczecie pętli głównej gry:
    while True:

        
        
        g.event_control(ai_settings, screen, soldier, bullets) #wywołuje kontrolę zdarzeń
        soldier.update() #aktualizacja pozycji żołnierza
        bullets.update() #aktualizacja położenia pocisków z grupy bullets
        g.update_bullets(ai_settings, screen, stats, scoreboard, soldier, enemies,bullets)
        g.update_enemies(ai_settings, stats, screen, enemies,  bullets)
        g.ememies_wins(ai_settings, screen,stats, scoreboard, soldier, enemies)
        g.screen_update(ai_settings, screen, stats, scoreboard, soldier, enemies, bullets) #aktualizacja ekranu gry
        




