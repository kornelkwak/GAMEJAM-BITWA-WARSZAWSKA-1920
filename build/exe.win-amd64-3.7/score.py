import pygame.font
import stats
from pygame.sprite import Group
from soldier import Eagle


class Scores():
    def __init__(self, ai_settings, screen, stats):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        self.text_color = (30, 30, 30) 
        self.font = pygame.font.SysFont(None, 48)

        self.prepare_score()
        self.prepare_high_score()
        self.prepare_level()
        self.prepare_eagles()

    def prepare_score(self):
        """Wyśiwetlenie punktacji w formie obrazu"""

        score_str = str(self.stats.score)
        self.score_image = self.font.render("Punkty: {}".format(score_str), True, 
        (255,255,255), self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.eagles.draw(self.screen)

    def prepare_high_score(self):
    
        high_score = int(round(self.stats.high_score, -1)) 
        high_score_str = "Rekord: {:,}".format(high_score) 
        self.high_score_image = self.font.render(high_score_str, True, 
            (255,255,255), self.ai_settings.bg_color)
    # Wyświetlenie najlepszego wyniku w grze na środku ekranu, przy górnej krawędzi.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx 
        self.high_score_rect.top = self.score_rect.top

    def prepare_level(self):
    
        self.level_image = self.font.render("Poziom: {}".format(str(self.ai_settings.level)), True, 
            (255,255,255), self.ai_settings.bg_color)
    # Numer poziomu jest wyświetlany pod aktualną punktacją.
        
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right 
        self.level_rect.top = self.score_rect.bottom + 10 

    
    def prepare_eagles(self):
        self.eagles = Group()
        for eagle_num in range(self.ai_settings.player_chance):
            eagle = Eagle(self.ai_settings, self.screen)
            eagle.rect.x = 10 + eagle_num * eagle.rect.width
            eagle.rect.y = 10
            self.eagles.add(eagle)




