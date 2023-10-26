import pygame
import random
import time
from math import floor,ceil
pygame.init()
WIDTH, HEIGHT = 500, 750
PLAYER_SIZE = 100
PLAYER_SPEED = 10
OBJECT_SIZE = 30
OBJECT_COLOR = (255, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Captain Toad Catches!")
pygame.display.set_icon(pygame.image.load("assets/icon.png"))
player_image = pygame.image.load("assets/toad.png")
player_image = pygame.transform.scale(player_image, (100, 110))
player_x = (WIDTH - PLAYER_SIZE) // 2
player_y = HEIGHT - PLAYER_SIZE
score = 0
life = 1000
clock = pygame.time.Clock()
objects = []
font = pygame.font.Font(None, 36)
running = True
frame_count = 0
object_frequency = 60
flip=False
def num(n):return int(n) if str(n).endswith(".0") else float(n)
while running:
    screen.blit(pygame.image.load("assets/background.png"),(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
        pass
    elif keys[pygame.K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
        flip=True
    elif keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += PLAYER_SPEED
        flip=False
    frame_count += 1
    if frame_count % object_frequency == 0:
        object_x = random.randint(0, WIDTH - (OBJECT_SIZE*1.5))
        object_y = 0
        objects.append([object_x, object_y,random.randint(0,4)])
    for obj in objects:
        obj[1] += 5 + (floor(pygame.time.get_ticks() / 5000) / 3)
        screen.blit(pygame.transform.scale(pygame.image.load("assets/diamond.png" if obj[2] else "assets/bomb.png"),(OBJECT_SIZE*1.5,OBJECT_SIZE*1.5)),(obj[0],obj[1]))
    for obj in objects:
        if player_x < obj[0] + OBJECT_SIZE and player_x + PLAYER_SIZE > obj[0] and player_y < obj[1] + OBJECT_SIZE and player_y + PLAYER_SIZE > obj[1]:
            objects.remove(obj)
            if obj[2]:score += 1
            else: life-=200
        elif not obj[1]<HEIGHT-OBJECT_SIZE:
            running=not life<=10
            if running:life-=100 if obj[2] else 0
    objects = [obj for obj in objects if obj[1] < HEIGHT-OBJECT_SIZE]
    player_image_flipped=pygame.transform.flip(player_image,flip, False)
    screen.blit(player_image_flipped, (player_x, player_y))
    score_display = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_display, (10, 35))
    if not frame_count%5:life+=1 if life<1000 else 0
    life_display = font.render(f"Health: {num(life/10)}", True, (255,255,255))
    screen.blit(life_display,(10,10))
    pygame.display.update()
    clock.tick(60)
    object_frequency = max(60-((floor(pygame.time.get_ticks()/2000))),20)
game_over_text = font.render(f"You're a failure! Your Score: {str(score)}", True, (255, 255, 255))
screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 18))
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()