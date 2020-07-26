import sys, pygame, stats
import settings, soldier
from enemy import Enemy
from bullets import Bullet
from random import randint
from soldier import Soldier, Eagle
from time import sleep
from pygame import mixer
from settings import loadify
from score import Scores
from menu import menu, surface


def event_control(ai_settings, screen, soldier, bullets):
    #Oczekiwanie na naciśnięcie klawisza lub przycisku myszy
    for event in pygame.event.get(): #pętla zdarzeń
        
        #Jeżeli został wciśnięty jakiś klawisz
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_control(event, ai_settings, screen, soldier, bullets)
        elif event.type == pygame.KEYUP:
            keyup_control(event, soldier)
           
        #Jeżeli wciśnięty klawisz był jednym z klawiszy RIGHT lub LEFT            
def keydown_control(event, ai_settings, screen, soldier, bullets):
    
    if event.key == pygame.K_RIGHT:
        soldier.move_right = True
    elif event.key == pygame.K_LEFT:
        soldier.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, soldier, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def keyup_control(event, soldier):
    if event.key == pygame.K_RIGHT:
        soldier.move_right = False
    elif event.key == pygame.K_LEFT:
        soldier.move_left = False

def fire_bullet(ai_settings, screen, soldier, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, soldier)
            bullets.add(new_bullet)
            shot = pygame.mixer.Sound('sound/rifle1.wav')
            #puszczenie dźwięku jednokrotnie (-1 wielokrotnie)
            shot.play()
    else: 
        rel = pygame.mixer.Sound('sound/reload.wav')
        #puszczenie dźwięku jednokrotnie (-1 wielokrotnie)
        rel.play()

def screen_update(ai_settings, screen, stats, scoreboard, soldier, enemies, bullets):
    
    
    #Wyświetlenie ostatnio zmodyfikowanego ekranu, uaktualnia ekran gry
    screen.blit(ai_settings.bg_color, (0, 0))
    scoreboard.show_score()
    #Wyświetlenie pocisków 
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    soldier.blitme() #odświerzenie położenia żołnierza
    enemies.draw(screen)
    #Odświerzenie ekranu gry
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, scoreboard, soldier, enemies,bullets):
    """Uaktualnienie położenia pocisków"""

    #Uaktualnienie położenia pocisków
    bullets.update()
    #Usunięcie pocisków z poza ekranu
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
    if len(enemies) == 0:
            
            ai_settings.level += 1
            scoreboard.prepare_level()
            next_level(ai_settings)
          
            
            #zwiększenie prędkości wraz z postepem levela
            ai_settings.soldier_speed *= ai_settings.speedup_scale
            ai_settings.enemy_speed *= ai_settings.speedup_scale
            ai_settings.group_speed *= ai_settings.speedup_scale
            bullets.empty()
            back_to_center(soldier)

            create_group(ai_settings, screen, soldier, enemies)
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        stats.score += 10 * ai_settings.level
        scoreboard.prepare_score()
        check_high_score(stats, scoreboard)
def update_enemies(ai_settings,stats, screen, enemies,  bullets):
    
    group_edges(ai_settings, enemies)
    enemies.update(ai_settings)      
        
        


def get_number_enemies_x(ai_settings, enemy_width):

    #Obliczenie szerokości miejsca na przeciwników i obliczenie ilości w rzędzie
    available_space_x = ai_settings.screen_width - 2 * enemy_width #Obliczenie ilości miejsca na enemy
    number_enemy_x = 13
    return number_enemy_x


def get_number_rows(ai_settings, solider_height, enemy_height):
    available_space_y = (ai_settings.screen_height - 2 * enemy_height)
    number_rows = 2
    return number_rows

def create_enemy(ai_settings, screen, enemies, enemy_number, row_number):

    random_x = randint(-10, 10)
    random_y = randint(-10, 10)
    enemy = Enemy(ai_settings, screen) #tworzy enemy
    enemy_width = enemy.rect.width #określa szerokość pojedynczego enemy
    enemy_height = enemy.rect.height
    enemy.x = enemy_width + 1.2 * enemy_width * enemy_number + random_x #oblicza x enemy w rzędzie
    enemy.rect.x = enemy.x #przypisanie x enemy do atrybutu rect.x
    enemy.rect.y = enemy_height + 1.3 * enemy_height * row_number + random_y
     
    
    enemies.add(enemy) #dodanie obiektu enemy do grupy enemies


def create_group(ai_settings, screen, soldier, enemies):
    """Utworzenie grupy przeciwników"""
    enemy = Enemy(ai_settings, screen)
    number_enemies_x = get_number_enemies_x(ai_settings, enemy.rect.width)
    number_rows = get_number_rows(ai_settings, soldier.rect.height, enemy.rect.height)
    
    for row_number in range(number_rows):
        for enemy_number in range(number_enemies_x):
            create_enemy(ai_settings, screen, enemies, enemy_number, row_number)

def group_edges(ai_settings, enemies):
    for enemy in enemies.sprites():
        if enemy.screen_edges():
            change_enemies_direction(ai_settings, enemies)
            break

def change_enemies_direction(ai_settings, enemies):  
    for enemy in enemies.sprites():
        enemy.rect.y += ai_settings.group_speed
    ai_settings.enemy_direction *= -1


def ememies_wins(ai_settings, screen, stats, scoreboard, soldier, enemies):
    if pygame.sprite.spritecollideany(soldier, enemies):
        player_hit(ai_settings, screen,stats, scoreboard, soldier, enemies)
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            ai_settings.player_chance -= 1       
            enemies.empty()
            back_to_center(soldier)
            create_group(ai_settings, screen, soldier, enemies)
    check_player_chance(ai_settings, soldier)
    ai_settings.win = False

def player_hit(ai_settings, screen,stats, scoreboard, soldier, enemies):
        ai_settings.player_chance -= 1
        scoreboard.prepare_eagles()
        enemies.empty()
        back_to_center(soldier)
        create_group(ai_settings, screen, soldier, enemies)
        sleep(0.75)

def back_to_center(soldier):
        soldier.center = soldier.screen_rect.centerx
        
def check_player_chance(ai_settings, soldier):
    if ai_settings.player_chance <= 0:
        menu.mainloop(surface)
        ai_settings.soldier_speed = 2
        ai_settings.enemy_speed = 2
        ai_settings.group_speed = randint(5,10)
          
        

def next_level(ai_settings):
    if ai_settings.level > 10:
        menu.mainloop(surface)
    else:
        ai_settings.bg_color = loadify(ai_settings.bg_list[ai_settings.level - 1])
        ai_settings.bg_color = pygame.transform.scale(ai_settings.bg_color, (1366, 768))



def check_high_score(stats, scoreboard):
    
    if stats.score > stats.high_score: 
        stats.high_score = stats.score
        scoreboard.prepare_high_score()
        






        

    



    


 


    
