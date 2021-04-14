class GameStats():
    
    def __init__(self, ai_settings):
        """Inicjalizacja danych statystycznych."""
        self.ai_settings = ai_settings
        self.reset_stats() 
    def reset_stats(self):
        
        self.soldier_left = self.ai_settings.player_chance
        self.score = 0
        self.high_score = 0
        self.level = 1

        