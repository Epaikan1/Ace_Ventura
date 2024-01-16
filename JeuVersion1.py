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

background_image = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\fond.png")
background_image = pygame.transform.scale(background_image, (1550, 1000))
player_image_g = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\persog.png")
player_image_d = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\persod.png")
player_image_sd = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\persosd1.png")
player_image_sg = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\persosg1.png")
player_image_c = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\persoc.png")
croco = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\croco.png")
ele = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\ele.png")
palmier = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\palmier.png")
lion = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\lion.png")

directionPerso = 1


 
# Initialisation du sprite Player ______________________________________________________________________________________



class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_image_d, (100, 150))
        self.rect = self.image.get_rect()
        self.vitesse = 600
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.player_pos.x = 500
        self.player_pos.y = 200

    def update(self):
            
        self.image = image
        self.rect.topleft = self.player_pos

joueur = Joueur()



# Initialisation des sprites obstacles ______________________________________________________________________________________



class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        i = random.randrange(1, 3)
        if i == 1 :
            mob = croco
            a = 300
            b = 200
        elif i == 2 :
            mob = lion
            a = 250
            b = 200
        else :
            pass

        self.image = pygame.transform.scale(mob, (a, b))
        self.rect = self.image.get_rect()

        if i == 1 :
            self.rect.width = 250
            self.rect.x = random.randrange(1400, 2100 - self.rect.width)
            self.rect.y =690
        elif i == 2 :
            self.rect.x = random.randrange(1400, 2200 - self.rect.width)
            self.rect.y =720
        else :
            pass

        self.vitesse = random.randrange(1, 5)

    def update(self):
        self.rect.x -= self.vitesse
        if self.rect.x < -400:
            i = random.randrange(1, 3)
            if i == 1 :
                mob = croco
                a = 300
                b = 200
            elif i == 2 :
                mob = lion
                a = 250
                b = 200
            else :
                pass

            self.image = pygame.transform.scale(mob, (a, b))
            self.rect = self.image.get_rect()

            if i == 1 :
                self.rect.width = 250
                self.rect.x = random.randrange(1400, 2100 - self.rect.width)
                self.rect.y =690
            elif i == 2 :
                self.rect.x = random.randrange(1400, 2200 - self.rect.width)
                self.rect.y =720
            else :
                pass

class Deco(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image = pygame.transform.scale(palmier, (400, 300))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1400, 2200 - self.rect.width)
        self.rect.y =580
        self.vitesse = 10

    def update(self):
        if self.rect.x < -400:
            self.rect.x = 1500         
            self.rect.y =580
        if self.rect.x > 1600 :
            self.rect.x = -300
            self.rect.y = 580

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] :
            self.rect.x -= self.vitesse
        if keys[pygame.K_q] or keys[pygame.K_LEFT] :
            self.rect.x += self.vitesse



all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
decs = pygame.sprite.Group()
all_sprites.add(joueur)

# Nombre de Sprites type obstacle
for _ in range(2):
    obstacle = Mob()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

for z in range(1):
    dec = Deco()
    all_sprites.add(dec)
    decs.add(dec)



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
            joueur.player_pos.x -= joueur.vitesse * dt
    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and crouch == False  :
            joueur.player_pos.x += joueur.vitesse * dt
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

#pygame.draw.circle(screen, "red", player_pos, 40)
