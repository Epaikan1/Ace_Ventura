import pygame
import sys

pygame.init()

# Variables
largeur_fenetre = 800
hauteur_fenetre = 600
fps = 60
horloge = pygame.time.Clock()
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Ace Ventura Course")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Charger l'image de fond
fond1 = pygame.image.load("/Users/maro wague/Desktop/projet_python/fond1.png")
fond1 = pygame.transform.scale(fond1, (largeur_fenetre, hauteur_fenetre))

class Personnage(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def afficher(self):
        fenetre.blit(self.image, self.rect)

# Charger l'image du personnage et ajuster sa taille
image_personnage = pygame.image.load("/Users/marowague/Desktop/projet_python/personnage.png")
image_personnage = pygame.transform.scale(image_personnage, (500, 500))

# Créer une instance du personnage en bas de l'écran
personnage = Personnage(image_personnage, largeur_fenetre // 2, hauteur_fenetre + 240)

def afficher_game_over():
    # Afficher l'image de fond
    fenetre.blit(fond1, (0, 0))

    # Créer une police pour le texte
    police = pygame.font.Font(None, 74)
    
    # Créer un texte "Game Over"
    #texte_game_over = police.render("Game Over", True, blanc)
    #rect_game_over = texte_game_over.get_rect()
    #rect_game_over.center = (largeur_fenetre // 2, hauteur_fenetre // 2 - 50)
    
    # Afficher le texte "Game Over"
    #fenetre.blit(texte_game_over, rect_game_over)

    # Afficher le personnage en bas de l'écran
    personnage.afficher()

    pygame.display.flip()

# Boucle principale
game_over = True  # Mettez cette variable à True pour afficher la page Game Over

while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_over:
        afficher_game_over()

    pygame.display.flip()
    horloge.tick(fps)
