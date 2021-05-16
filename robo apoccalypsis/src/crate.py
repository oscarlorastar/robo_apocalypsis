import pygame

class Crate(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("../assets/Crate.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        self.screen.blit(self.image, self.rect)