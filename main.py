import pygame
import random
import time
from math import floor

pygame.init()
WIDTH, HEIGHT = 500, 750
PLAYER_SIZE = 100
PLAYER_SPEED = 10
OBJECT_SIZE = 30
OBJECT_SPEED = 2
BACKGROUND_COLOR = (0, 0, 0)
OBJECT_COLOR = (255, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catching Game")

# Load the player image
player_image = pygame.image.load("toad.png")
player_image = pygame.transform.scale(player_image, (100, 110))

# Initialize player position
player_x = (WIDTH - PLAYER_SIZE) // 2
player_y = HEIGHT - PLAYER_SIZE

# Initialize score
score = 0

# Create clock object to control the frame rate
clock = pygame.time.Clock()
objects = []
font = pygame.font.Font(None, 36)

running = True
frame_count = 0
object_frequency = 60
flip=False

screen.blit(pygame.image.load("background.png"),(0,0))
while running:
    screen.fill(BACKGROUND_COLOR)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        pass
    elif keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
        flip=True
    elif keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += PLAYER_SPEED
        flip=False


    # Generate new falling objects at random intervals
    frame_count += 1
    if frame_count % object_frequency == 0:
        object_x = random.randint(0, WIDTH - OBJECT_SIZE)
        object_y = 0
        objects.append([object_x, object_y])

    # Move and draw the falling objects
    for obj in objects:
        obj[1] += OBJECT_SPEED
        pygame.draw.rect(screen, OBJECT_COLOR, (obj[0], obj[1], OBJECT_SIZE, OBJECT_SIZE))

    # Check for collisions with the player
    for obj in objects:
        if player_x < obj[0] + OBJECT_SIZE and player_x + PLAYER_SIZE > obj[0] and player_y < obj[1] + OBJECT_SIZE and player_y + PLAYER_SIZE > obj[1]:
            objects.remove(obj)
            score += 1

    # Remove objects that are out of the screen
    objects = [obj for obj in objects if obj[1] < HEIGHT]

    # Display the player
    player_image_flipped=pygame.transform.flip(player_image,flip, False)
    screen.blit(player_image_flipped, (player_x, player_y))

    # Display the score
    score_display = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_display, (10, 10))

    #life_display = font_render(f"Life: {}")

    pygame.display.update()
    clock.tick(60)
    OBJECT_SPEED = 2 + (floor(pygame.time.get_ticks() / 5000) / 3)
    object_frequency = 60 + (floor(pygame.time.get_ticks() / 1000))

# Game over screen
game_over_text = font.render("Game Over! Your Score: " + str(score), True, (255, 255, 255))
screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 18))
pygame.display.update()

# Wait for a few seconds before quitting
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()
