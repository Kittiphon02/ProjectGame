# item.py

import pygame
import random

class Item:
    def __init__(self):
        # Create a Pygame Surface for the item (e.g., a 20x20 square)
        self.image = pygame.Surface((20, 20))  # You can also load an image file here
        self.image.fill((255, 0, 0))  # Red color for visibility

        # Set the initial position randomly
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(600, 800)  # Start off-screen on the right
        self.rect.y = random.randint(0, 580)

    def move_item(self):
        # Move the item leftward across the screen
        self.rect.x -= 5  # Adjust speed as needed

    def refresh(self):
        # Reset the item’s position off-screen to the right
        self.rect.x = random.randint(600, 800)
        self.rect.y = random.randint(0, 580)
