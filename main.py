import pygame
from game import Game
pygame.init()


# Fenetre
pygame.display.set_caption("Shotter")
screen = pygame.display.set_mode((1080, 720))

# mettre le fond d'écran
background = pygame.image.load('assets/bg.jpg')

# charger notre jeu
game = Game()


running = True

# boucle tant que cette condition est vrait
while running:

    # appliquer l'arrier plan de notre joueur
    screen.blit(background, (0, -200))

    # appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # récuperer les projectile de mon joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # faire marcher les monstre
    for monster in game.all_monster:
        monster.forward()

    # appliquer l'ensemble de mon groupe de projectiles.
    game.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des image de mon groupe de monstres
    game.all_monster.draw(screen)

    # verifier si le joueur souhaite d'aller a droite ou a gauche
    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

    # mettre a jour l'écran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Fermeture du jeux')
             # detecter si le joueur a enclanchée une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # touche espace enchanchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
