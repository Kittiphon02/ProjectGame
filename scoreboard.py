# scoreboard.py
import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.highest_score = 0
        self.highest_level = 1

    def increase_level(self):
        self.level += 1
        # Update highest level if the current level is greater
        if self.level > self.highest_level:
            self.highest_level = self.level

    def increase_score(self, amount):
        """Increase score by the specified amount."""
        self.score += amount
        # Update highest score if the current score is greater
        if self.score > self.highest_score:
            self.highest_score = self.score

    def display_score(self, screen):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        level_text = font.render(f"Level: {self.level}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))

    def game_over(self, screen):
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        score_text = font.render(f"Your Score: {self.score}", True, (255, 255, 255))
        high_score_text = font.render(f"Highest Score: {self.highest_score}", True, (255, 255, 0))
        level_text = font.render(f"Level Reached: {self.level}", True, (255, 255, 255))
        high_level_text = font.render(f"Highest Level: {self.highest_level}", True, (255, 255, 0))
        go_text = font.render("Press 'G' to Go Again", True, (255, 0, 0))

        screen.blit(game_over_text, (200, 150))
        screen.blit(score_text, (200, 200))
        screen.blit(high_score_text, (200, 250))
        screen.blit(level_text, (200, 300))
        screen.blit(high_level_text, (200, 350))
        screen.blit(go_text, (200, 400))

    def reset_score(self):
        """Reset the score and level for a new game."""
        self.score = 0
        self.level = 1
