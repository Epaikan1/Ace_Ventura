import pygame
import sys

pygame.init()

fps = 60
horloge = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Ace Ventura Course")

blanc = (255, 255, 255)
noir = (0, 0, 0)

fond1 = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\1.png").convert()
fond2 = pygame.image.load("C:\\Users\\larde\\OneDrive\\Bureau\\Informatique\\Python\\Piscine\\images\\2.png").convert()
fond1 = pygame.transform.scale(fond1, screen.get_size())
fond2 = pygame.transform.scale(fond2, screen.get_size())

class Personnage(pygame.sprite.Sprite):

    def __init__(self, image, x, y):

        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def afficher(self):

        screen.blit(self.image, self.rect)

class GameOver:

    def __init__(self):

        self.i = 1


    def afficher(self):

        screen.blit(fond1, (0, 0))

        pygame.display.flip()

    def update(self):

        self.i += 1

        if self.i <= 50:
            screen.blit(fond1, (0, 0))

        elif self.i > 50 and self.i < 100 :
            screen.blit(fond2, (0, 0))
        else :
            self.i = 1


go = GameOver()

game_over = True
running = True

i = 0

while running:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False

    if game_over:
        go.afficher()
        game_over = False

    go.update()

    pygame.display.flip()
    horloge.tick(fps)

