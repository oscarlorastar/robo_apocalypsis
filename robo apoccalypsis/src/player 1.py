import pygame
import toolbox
import projectile


class Player(pygame.sprite.Sprite):
    # Player constructor class
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen             
        self.x = x
        self.y = y
        self.image = pygame.image.load("../assets/Player_03.png")
        self.image_hurt = pygame.image.load("../assets/Player_03_hurt.png")
        self.enemy_image_defeated = pygame.image.load("../assets/Enemy_04.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 8
        self.angle = 0
        self.shoot_timer = 0
        self.shoot_timer_max = 10
        self.health = 30
        self.alive = True
        self.hurt_timer = 0
        
        
    # loop
    def update(self, enemies):
        self.rect.center = (self.x, self.y)

        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.get_hit(0)
                self.get_hit(enemy.damage)
                

        if self.shoot_timer > 0:
            self.shoot_timer -= 1
        
        # get the angle
        if self.alive:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.angle = toolbox.angle_between_points(self.x, self.y, mouse_x, mouse_y) 
        if self.alive:
            if self.hurt_timer > 0:
                image_to_rotate = self.image_hurt
                self.hurt_timer -= 1
            else:
                image_to_rotate = self.image
        else:
            image_to_rotate = self.enemy_image_defeated

        # get rotated
        image_to_draw, image_rect = toolbox.get_rotated_image(image_to_rotate, self.rect, self.angle)

        self.screen.blit(image_to_draw, image_rect)
        
    # move
    def move_down(self):
        if self.alive:
            self.y += self.speed
    def move_right(self):
        if self.alive:
            self.x += self.speed
    def move_up(self):
        if self.alive:        
            self.y -= self.speed
    def move_left(self):
        if self.alive:
            self.x -= self.speed
                
    def shoot(self):
        if self.shoot_timer <= 0 and self.alive:
            self.shoot_timer = self.shoot_timer_max
            projectile.waterballon(self.screen, self.x, self.y, self.angle)

    def get_hit(self, damage):
        if self.alive:
            self.hurt_timer = 5
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.alive = False
