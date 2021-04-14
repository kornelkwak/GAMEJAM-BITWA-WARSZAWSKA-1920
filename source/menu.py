import os
import pygame
import pygame_menu
import bitwa_warszawska as b
from pygame import mixer
from score import Scores
import time


pygame.init()

surface = pygame.display.set_mode((1366,768), pygame.FULLSCREEN)


menu_image = pygame_menu.baseimage.BaseImage(
    image_path='images/menu.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
    
)

menu_image2 = pygame_menu.baseimage.BaseImage(
    image_path='images/menu2.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
    
)

menu_image3 = pygame_menu.baseimage.BaseImage(
    image_path='images/menu3.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
    
)

plansza = pygame_menu.baseimage.BaseImage(
    image_path='images/plansza.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
    
)

font = pygame_menu.font.FONT_PT_SERIF


menu_theme = pygame_menu.themes.Theme(widget_font = font, 
                background_color = menu_image, 
                title_shadow=True,
                title_background_color=(4, 47, 126),
                title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE,
                menubar_close_button = False,
                widget_alignment = pygame_menu.locals.ALIGN_LEFT, 
                                       
                )   

start_theme = pygame_menu.themes.Theme(widget_font = font, 
                background_color = plansza, 
                title_shadow=True,
                title_background_color=(4, 47, 126),
                title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE,
                menubar_close_button = False,
                widget_alignment = pygame_menu.locals.ALIGN_CENTER,

                             
                ) 
autor_theme = pygame_menu.themes.Theme(widget_font = font, 
                background_color = menu_image2, 
                title_shadow=True,
                title_background_color=(4, 47, 126),
                title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE,
                menubar_close_button = False,
                widget_alignment = pygame_menu.locals.ALIGN_LEFT,

                             
                ) 

zasady_theme = pygame_menu.themes.Theme(widget_font = font, 
                background_color = menu_image3, 
                title_shadow=True,
                title_background_color=(4, 47, 126),
                title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE,
                menubar_close_button = False,
                widget_alignment = pygame_menu.locals.ALIGN_LEFT,             
                ) 

menu_theme.widget_font_color = (0,0,0)

def start_the_game():
    
    b.main()


start = pygame_menu.Menu(height=767,
                        width=1365,
                        theme=start_theme,
                        title=''
                        )

autor = pygame_menu.Menu(height=767,
                        width=1365,
                        theme=autor_theme,
                        title=''
                        )
zasady = pygame_menu.Menu(height=767,
                        width=1365,
                        theme=zasady_theme,
                        title=''
                        )


menu = pygame_menu.Menu(height=767,
                        width=1365,
                        theme=menu_theme,
                        title='',
                        
                        )

start.add_vertical_margin(500)
start.add_button('KLIKNIJ ABY PRZEJŚĆ DALEJ', start_the_game, selection_color = (255,0,0), font_size = 40)

autor.add_button('WSTECZ', pygame_menu.events.BACK)
zasady.add_button('WSTECZ', pygame_menu.events.BACK)

menu.add_button('GRAJ', start)
menu.add_vertical_margin(5)
menu.add_button('ZASADY GRY', zasady)
menu.add_vertical_margin(5)
menu.add_button('AUTOR', autor)
menu.add_vertical_margin(5)
menu.add_button('WYJŚCIE', pygame_menu.events.EXIT)

mixer.music.load('sound/menu.mp3')
mixer.music.play(-1)


if __name__ == '__main__':
    menu.mainloop(surface)

