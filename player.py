import pygame
from projectile import Projectile

# créer une première classe qui vas représenter notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    def launch_projectile(self):
        # instace ptn j'ai la flemme d'écrire
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec le monstre

            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
