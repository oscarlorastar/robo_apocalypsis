import pygame
import random
from player import Player
from projectile import waterballon
from enemy import Enemy

# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True


background_image = pygame.image.load("../assets/BG_Sand.png")

playerGroup = pygame.sprite.Group()
projectilesGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()


Player.containers = playerGroup
waterballon.containers = projectilesGroup
Enemy.containers = enemiesGroup

enemy_spawn_timer_max = 80
enemy_spawn_timer = 0

mr_player = Player(screen, game_width/2, game_height/2)


# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        mr_player.move_down()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        mr_player.move_right()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        mr_player.move_up()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        mr_player.move_left()
    if pygame.mouse.get_pressed()[0]:
        mr_player.shoot()

    enemy_spawn_timer -= 1
    if enemy_spawn_timer <= 0:
        new_enemy = Enemy(screen, 0, 0, mr_player)
        side_to_spawn = random.randint(0, 3)
        if side_to_spawn == 0:
            new_enemy.x = random.randint(0, game_width)
            new_enemy.y = -new_enemy.image.get_height()
        elif side_to_spawn == 1:
            new_enemy.x = -new_enemy.image.get_width()
            new_enemy.y = game_height + new_enemy.image.get_height()
        elif side_to_spawn == 2:
            new_enemy.x = -new_enemy.image.get_width()
            new_enemy.y = random.randint(0, game_height)
        elif side_to_spawn == 3:
            new_enemy.x = game_width + new_enemy.image.get_width()
            new_enemy.y = random.randint(0, game_height)
        enemy_spawn_timer = enemy_spawn_timer_max
        
    screen.blit(background_image, (0, 0))

    for projectile in projectilesGroup:
        projectile.update()

    for enemy in enemiesGroup:
        enemy.update(projectilesGroup)

    mr_player.update(enemiesGroup)
    

    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(40)
    pygame.display.set_caption("ATTACK OF THE ROBOTS fps: " + str(clock.get_fps()))
