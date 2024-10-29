# scoreboard.py
import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.level = 1

    def increase_level(self):
        self.score += 1

    def display_score(self, screen):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def game_over(self):
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        screen = pygame.display.get_surface()  # Get the main display screen
        screen.blit(game_over_text, (200, 250))

    def reset_score(self):
        """Reset the score to 0 for a new game."""
        self.score = 0
        self.level = 1
