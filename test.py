import pygame
import time
import sys



# Pré-Initialisation, paramètre, etc ... __________________________________________________________________



pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player_pos.x = 500
player_pos.y = 200

surf = pygame.Surface((50, 50))
jump_speed = -20
gravity = 0.8
velocity = 0
on_ground = True

background_image = pygame.image.load("C:\\Users\\larde\\Downloads\\plage.jpg")
player_image = pygame.image.load("C:\\Users\\larde\\Downloads\\test.jpg")



# Lancement du jeu ______________________________________________________________________________________



while running:



# Initialisation ________________________________________________________________________________________



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



# Design et contrôle de la carte ________________________________________________________________________



    screen.blit(background_image, (0, 0))



# Design et contrôle du personnage ______________________________________________________________________



    #pygame.draw.circle(screen, "red", player_pos, 40)
    ajuste_taille = pygame.transform.scale(player_image, (50, 50))  # Adjust the size as needed
    screen.blit(ajuste_taille, player_pos)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE] :
        break

    if player_pos.x <= 0 and keys[pygame.K_q] :
        player_pos.x += 1 * dt
    elif player_pos.x >= 1485 and keys[pygame.K_d] :
        player_pos.x -= 1 * dt
    elif keys[pygame.K_q]:
        player_pos.x -= 500 * dt
    elif keys[pygame.K_d]:
        player_pos.x += 500 * dt

    if keys[pygame.K_SPACE] and on_ground:
        velocity = jump_speed
        on_ground = False

    velocity += gravity
    player_pos.y += velocity

    if player_pos.y > 815:
        player_pos.y = 815
        on_ground = True



# Design et mouvement des obstacles ________________________________________________________________







# Fin de programme et horloge ______________________________________________________________________


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
