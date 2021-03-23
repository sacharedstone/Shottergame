import pygame
from player import Player
from monster import Monster

# créer une second classe qui vas représenter notre jeu
class Game(pygame.sprite.Sprite):

    def __init__(self):
        # generer notre joueur
        self.player = Player(self)
        # groupe ed monstre
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster()
        self.all_monster.add(monster)