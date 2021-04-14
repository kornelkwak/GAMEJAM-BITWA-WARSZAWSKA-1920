import sys, cx_Freeze
from cx_Freeze import setup, Executable

executables = [cx_Freeze.Executable("menu.py", base = "Win32GUI", targetName="gra.exe", icon = "images/eagle.ico")]
cx_Freeze.setup( name="GRA",
    options = {"build exe": {"packages":["time", "menu","os", "pygame", "pygame_menu", "bitwa_warszawska", "bullets", "soldier", "enemy", "game", "settings", "intro", "stats", "score"],
    "included_files": ["images/okopy1.png","images/okopy2.png", "images/okopy3.png", "images/okopy4.png","images/okopy4.png","images/okopy5.png","images/okopy6.png",
    "images/okopy7.png","images/okopy8.png","images/okopy9.png","images/okopy10.png","images/p.png",
    "images/b1.png","images/b2.png","images/b3.png",
     "images/menu.png","images/menu2.png","images/menu3.png","images/plansza.png", "images]eagle.png", "sound/rifle1.wav", "sound/menu.mp3", "sound/game.mp3", "sound/reload.wav"], 'includes': ['_ssl'], 'bdist_msi': {
    'add_to_path': True,
    'environment_variables': [
        ("E_MYAPP_VAR", "=-*MYAPP_VAR", "1", "TARGETDIR")
    ]
}}},
    
    
    
    
    executables = executables
       
    
    
     )