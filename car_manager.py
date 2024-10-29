import pygame
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_image = pygame.image.load("Logi.png")  # Load the car image
        self.car_image = pygame.transform.scale(self.car_image, (20, 30))  # Resize as needed
        self.speed = 5  # Initial speed

    def create_car(self):
        if random.randint(1, 20) == 1:  # Randomly create a car
            new_car = self.car_image.get_rect()
            new_car.x = 600  # Start from the right side of the screen
            new_car.y = random.randint(100, 500)  # Random y position
            self.all_cars.append((self.car_image, new_car))

    def move_cars(self, slowed=False):
        """Move all cars left, with optional slowing effect."""
        current_speed = self.speed * 0.5 if slowed else self.speed  # Half speed if slowed

        for car_surface, car_rect in self.all_cars:
            car_rect.x -= current_speed  # Move car to the left

        # Remove cars that have gone off the screen
        self.all_cars = [car for car in self.all_cars if car[1].x > -50]  # Keep cars that are still on screen

    def level_up(self):
        """Increase car speed with each level up."""
        self.speed += 1  # Increase speed for the next level

    def reset(self):
        """Clear all cars and reset speed for a new game."""
        self.all_cars.clear()  # Clear all cars for reset
        self.speed = 5  # Reset speed to initial value
