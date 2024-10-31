import pygame
import time
from moviepy.editor import VideoFileClip
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from item import Item
from food import Food  # เพิ่มการ import คลาส Food

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Car Game")

# Load sounds
jump_sound = pygame.mixer.Sound("woosh-230554.mp3")
crash_sound = pygame.mixer.Sound("sword-hit-7160.mp3")

# Load video as background using MoviePy
video = VideoFileClip("wy.mp4").resize((600, 600))

# Load death effect image
death_effect_img = pygame.image.load("Boom.png")  # Replace with your effect image file
death_effect_img = pygame.transform.scale(death_effect_img, (60, 60))  # Adjust size if needed

# Create game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
items = [Item() for _ in range(5)]  # สร้างไอเท็มหลายชิ้น
foods = [Food() for _ in range(3)]  # สร้างอาหาร 3 ชิ้น

# Game state variables
game_is_on = True
slow_duration = 5
slow_effect_end_time = 0
highest_score = 0
death_effect_active = False
death_effect_start_time = 0
effect_duration = 1.0  # Duration of death effect (in seconds)

# Main game loop
clock = pygame.time.Clock()
video_start_time = time.time()

def reset_game():
    """Reset game state for a new start."""
    global game_is_on, video_start_time, highest_score, death_effect_active, slow_effect_end_time
    player.go_to_start()
    car_manager.reset()  # Reset car speed and clear cars
    scoreboard.reset_score()  # Reset score
    game_is_on = True
    death_effect_active = False
    slow_effect_end_time = 0  # Reset slow effect
    video_start_time = time.time()

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_is_on:
                jump_sound.play()
                player.go_up()
            elif event.key == pygame.K_DOWN and game_is_on:
                player.go_down()
            elif event.key == pygame.K_LEFT and game_is_on:
                player.go_left()
            elif event.key == pygame.K_RIGHT and game_is_on:
                player.go_right()
            elif event.key == pygame.K_g and not game_is_on:  # 'G' to restart
                reset_game()

    # Update video frame based on elapsed time
    elapsed_time = time.time() - video_start_time
    video_frame = video.get_frame(elapsed_time)
    video_surface = pygame.surfarray.make_surface(video_frame.swapaxes(0, 1))
    screen.blit(video_surface, (0, 0))  # Draw video as background

    if game_is_on:
        # Update game elements
        car_manager.create_car()
        
        # Apply slowing effect if active
        if time.time() < slow_effect_end_time:
            car_manager.move_cars(slowed=True)  # Move cars slower
        else:
            car_manager.move_cars(slowed=False)  # Move cars normally
        
        # Handle items
        for item in items:
            item.move_item()  # Move each item leftward
            screen.blit(item.image, item.rect)  # Draw the item on the screen

            # Check for item collection
            if player.rect.colliderect(item.rect):
                item.refresh()
                slow_effect_end_time = time.time() + slow_duration  # Activate slow effect
            
            # If item goes off-screen, reset its position
            if item.rect.left < 0:
                item.refresh()
        
        # Handle food items
        for food in foods:
            food.move_food()  # Move each food item leftward
            screen.blit(food.image, food.rect)  # Draw the food on the screen

            # Check for food collection
            if player.rect.colliderect(food.rect):
                food.refresh()  # Reset food position
                scoreboard.increase_score(10)  # เพิ่มคะแนนให้ผู้เล่นเมื่อเก็บอาหารได้
            
            # If food goes off-screen, reset its position
            if food.rect.left < 0:
                food.refresh()
        
        # Collision detection for cars
        for car_surface, car_rect in car_manager.all_cars:
            if car_rect.colliderect(player.rect):
                game_is_on = False
                crash_sound.play()
                death_effect_active = True
                death_effect_start_time = time.time()
                if scoreboard.score > highest_score:
                    highest_score = scoreboard.score  # Update highest score

        # Check if player reached finish line
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()  # Increase car speed with each level
            scoreboard.increase_level()  # Increase score by 1

    # Draw player or death effect
    if not death_effect_active:
        screen.blit(player.image, player.rect)
    else:
        # Display death effect for a short duration
        if time.time() - death_effect_start_time < effect_duration:
            # Draw death effect at player's last position
            screen.blit(death_effect_img, player.rect)
        else:
            # After effect ends, display game over screen
          
            # After effect ends, display game over screen
            game_is_on = False
            font = pygame.font.Font(None, 36)

            # Display current score and highest score
            score_text = font.render(f"Your Score: {scoreboard.score}", True, (255, 255, 255))
            high_score_text = font.render(f"Highest Score: {scoreboard.highest_score}", True, (255, 255, 0))

            # Display current level and highest level
            level_text = font.render(f"Level Reached: {scoreboard.level}", True, (255, 255, 255))
            high_level_text = font.render(f"Highest Level: {scoreboard.highest_level}", True, (255, 255, 0))

            # Display restart instruction
            go_text = font.render("Press 'G' to Go Again", True, (255, 0, 0))

            # Blit texts to the screen
            screen.blit(score_text, (200, 150))
            screen.blit(high_score_text, (200, 200))
            screen.blit(level_text, (200, 250))
            screen.blit(high_level_text, (200, 300))
            screen.blit(go_text, (200, 350))

            # Update display
            pygame.display.flip()


            # Wait for 'G' key to restart
            waiting_for_restart = True
            while waiting_for_restart:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                        waiting_for_restart = False
                        reset_game()
                        # Main game loop changes

    if not game_is_on and death_effect_active:
        # Display death effect and show game over screen after effect duration
        if time.time() - death_effect_start_time < effect_duration:
            screen.blit(death_effect_img, player.rect)
        else:
            # Display game over and score
            scoreboard.game_over(screen)
            pygame.display.flip()


    # Draw cars on the screen
    for car_surface, car_rect in car_manager.all_cars:
        screen.blit(car_surface, car_rect)

    # Display the score
    scoreboard.display_score(screen)

    # Update display and set frame rate
    pygame.display.flip()
    clock.tick(30)  # Run the game at 30 frames per second
