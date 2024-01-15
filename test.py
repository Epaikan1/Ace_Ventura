import pygame
from pygame.sprite import *
import random
import time
import sys



# Pré-Initialisation, paramètre, etc ... __________________________________________________________________

# Definition of the Obstacle class
#largeur_fenetre = 800
#hauteur_fenetre = 600
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
clock = pygame.time.Clock()
running = True
dt = 0

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # You might need to adjust the size
        self.image.fill((255, 0, 0))  # Red color for simplicity
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1700 - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.vitesse = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.vitesse
        if self.rect.y > 820:
            self.rect.y = random.randrange(-100, -40)
            self.rect.x = random.randrange(0, 1700 - self.rect.width)

# Pré-Initialisation, paramètre, etc ...
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Create obstacles outside the main loop
for _ in range(8):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player_pos.x = 500
player_pos.y = 200

surf = pygame.Surface((50, 50))
jump_speed = -25
gravity = 1
velocity = 0
on_ground = True
crouch = False

background_image = pygame.image.load("C:\\Users\\larde\\Downloads\\plage.jpg")
player_image_g = pygame.image.load("C:\\Users\\larde\\Downloads\\persog.png")
player_image_d = pygame.image.load("C:\\Users\\larde\\Downloads\\persod.png")
player_image_sd = pygame.image.load("C:\\Users\\larde\\Downloads\\persosd1.png")
player_image_sg = pygame.image.load("C:\\Users\\larde\\Downloads\\persosg1.png")
player_image_c = pygame.image.load("C:\\Users\\larde\\Downloads\\persoc.png")
croco = pygame.image.load("C:\\Users\\larde\\Downloads\\croco.png")

directionPerso = 1



# Lancement du jeu ______________________________________________________________________________________



while running:



# Initialisation ________________________________________________________________________________________



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



# Design et contrôle de la carte ________________________________________________________________________



    screen.blit(background_image, (0, 0))



# Design et contrôle du personnage ______________________________________________________________________



    if on_ground == True and crouch == True :
        ajuste_taille = pygame.transform.scale(player_image_c, (175, 250))

    elif on_ground == True and crouch == False :
        ajuste_taille = pygame.transform.scale(player_image_g if directionPerso == 1 else player_image_d, (100, 250))

    elif on_ground == False and crouch == False :
         ajuste_taille = pygame.transform.scale(player_image_sg if directionPerso == 1 else player_image_sd, (175, 250))

    screen.blit(ajuste_taille, player_pos)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE] :
        running = False

    if player_pos.x <= -45 and keys[pygame.K_q] :
        player_pos.x += 1 * dt
    elif player_pos.x >= 1435 and keys[pygame.K_d] :
        player_pos.x -= 1 * dt
    elif keys[pygame.K_q] and crouch == False :
            directionPerso = 1
            player_pos.x -= 600 * dt
    elif keys[pygame.K_d] and crouch == False  :
            player_pos.x += 600 * dt
            directionPerso = 0

    if keys[pygame.K_s] :
         crouch = True
    else :
         crouch = False
         

    if keys[pygame.K_SPACE] and on_ground and crouch == False:
        velocity = jump_speed
        on_ground = False

    velocity += gravity
    player_pos.y += velocity

    if player_pos.y > 615:
        player_pos.y = 615
        on_ground = True



# Design et mouvement des obstacles ________________________________________________________________


    for obstacle in obstacles:
            obstacle.update()

    all_sprites.update()
    all_sprites.draw(screen)


# Fin de programme et horloge ______________________________________________________________________


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()


# Old content _____________________________________________________________________________________

#pygame.draw.circle(screen, "red", player_pos, 40)

    dt = clock.tick(60) / 1000

pygame.quit()
