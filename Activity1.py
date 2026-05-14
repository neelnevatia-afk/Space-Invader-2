import random
import math
import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYERSTARTX = 370
PLAYERSTARTY = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED = 10
Collision_DISTANCE = 27
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
caption = pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
background = pygame.image.load("download.png")
playerImg = pygame.image.load("player.png")
playerx=PLAYERSTARTX
playery=PLAYERSTARTY
playerx_change = 0
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = PLAYERSTARTY
bulletX_change = 0
bulletY_change = BULLET_SPEED
bullet_state = "ready"
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
over_font = pygame.font.Font("freesansbold.ttf", 64)
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
     return distance > Collision_DISTANCE           

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

running = True
while running:
    screen.blit(background, (0, 0))
    player(playerx, playery)
   
        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerx
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    playerx += playerx_change
    playerx = max(0, min(playerx, SCREEN_WIDTH - 64))
    for i in range(num_of_enemies):
        
       if enemyY[i] > 340:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        game_over_text()
        break
       enemyX[i] += enemyX_change[i]
       if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]                                                   
       if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
             collision = True
             bullet_y = PLAYERSTARTY
             bullet_state = "ready"
             score_value += 1
             enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
             enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
       enemy(enemyX[i], enemyY[i], i)
       if enemyY[i] > playery - 64:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
    if bulletY <= 0:
        bulletY = PLAYERSTARTY
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    show_score(textX, textY)


            
pygame.quit()


