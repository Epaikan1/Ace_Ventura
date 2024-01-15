import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()

    if player_pos.x >= 0 and player_pos.y >= 0 and player_pos.x <= 1280 and player_pos.y <= 720 :
        if keys[pygame.K_w]:
            player_pos.y -= 500 * dt
        if keys[pygame.K_s]:
            player_pos.y += 500 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 500 * dt
        if keys[pygame.K_d]:
            player_pos.x += 500 * dt
    elif player_pos.x <= 0 :
        player_pos.x = 1
    elif player_pos.y <= 0 :
        player_pos.y = 1
    elif player_pos.x >= 1280 :
        player_pos.x = 1279
    elif player_pos.y >= 720 :
        player_pos.y = 719

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
