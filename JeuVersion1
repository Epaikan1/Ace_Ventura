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

surf = pygame.Surface((50, 50))
jump_speed = -25
gravity = 1
velocity = 0
on_ground = True
crouch = False

background_image = pygame.image.load("C:\\Users\\larde\\Downloads\\fond.png")
player_image_g = pygame.image.load("C:\\Users\\larde\\Downloads\\persog.png")
player_image_d = pygame.image.load("C:\\Users\\larde\\Downloads\\persod.png")
player_image_sd = pygame.image.load("C:\\Users\\larde\\Downloads\\persosd1.png")
player_image_sg = pygame.image.load("C:\\Users\\larde\\Downloads\\persosg1.png")
player_image_c = pygame.image.load("C:\\Users\\larde\\Downloads\\persoc.png")
croco = pygame.image.load("C:\\Users\\larde\\Downloads\\croco.png")

directionPerso = 1


 
# Initialisation du sprite Player ______________________________________________________________________________________



class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_image_d, (100, 200))
        self.rect = self.image.get_rect()
        self.vitesse = 5
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.player_pos.x = 500
        self.player_pos.y = 200

    def update(self):
            
        self.image = image
        self.rect.topleft = self.player_pos

joueur = Joueur()



# Initialisation des sprites obstacles ______________________________________________________________________________________



class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        #self.image.fill((0, 0, 255)) Carrés bleus
        self.image = pygame.transform.scale(croco, (200, 150))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1700, 2100 - self.rect.width)
        self.rect.y = 740
        self.vitesse = random.randrange(1, 5)

    def update(self):
        self.rect.x -= self.vitesse
        if self.rect.x < 0:
            self.rect.y = 740
            self.rect.x = random.randrange(1800, 2100 - self.rect.width)

all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
all_sprites.add(joueur)

# Nombre de Sprites type obstacle
for _ in range(3):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)



# Lancement du jeu ______________________________________________________________________________________



while running:



# Initialisation ________________________________________________________________________________________



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



# Design et contrôle de la carte ________________________________________________________________________



    screen.blit(background_image, (0, - 100))



# Design et contrôle du personnage ______________________________________________________________________
    


    if on_ground == True and crouch == True :
        image = pygame.transform.scale(player_image_c, (150, 225))

    elif on_ground == True and crouch == False :
        image = pygame.transform.scale(player_image_g if directionPerso == 1 else player_image_d, (100, 250))

    elif on_ground == False and crouch == False :
        image = pygame.transform.scale(player_image_sg if directionPerso == 1 else player_image_sd, (175, 250))

    screen.blit(image, joueur.player_pos)



    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE] :
        running = False

    if joueur.player_pos.x <= -45 and (keys[pygame.K_q] or keys[pygame.K_LEFT]) :
        joueur.player_pos.x += 1 * dt
    elif joueur.player_pos.x >= 1435 and (keys[pygame.K_d] or keys[pygame.K_RIGHT]) :
        joueur.player_pos.x -= 1 * dt
    elif (keys[pygame.K_q] or keys[pygame.K_LEFT]) and crouch == False :
            directionPerso = 1
            joueur.player_pos.x -= 600 * dt
    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and crouch == False  :
            joueur.player_pos.x += 600 * dt
            directionPerso = 0

    if keys[pygame.K_s] or keys[pygame.K_DOWN] :
         crouch = True
    else :
         crouch = False
         

    if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and on_ground and crouch == False:
        velocity = jump_speed
        on_ground = False

    velocity += gravity
    joueur.player_pos.y += velocity

    if joueur.player_pos.y > 615:
        joueur.player_pos.y = 615
        on_ground = True



# Design et mouvement des obstacles ________________________________________________________________


    for obstacle in obstacles:
            obstacle.update()

    all_sprites.update()
    all_sprites.draw(screen)

    collisions = pygame.sprite.spritecollide(joueur, obstacles, False)
    if collisions:
        pygame.quit()
        sys.exit()





# Fin de programme et horloge ______________________________________________________________________


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()


# Old content _____________________________________________________________________________________

#pygame.draw.circle(screen, "red", player_pos, 40)    ddd
