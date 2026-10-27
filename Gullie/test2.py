import pygame
pygame.display.set_caption("pong")
pygame.init()

WIDTH, HEIGHT = 1000, 600

ball_x, ball_y = 500, 100
circles = [
    (ball_x, ball_y),
    (150, 120),
    (850, 120),
    (500, 500),
    (200, 450),
    (800, 450),
]

wn = pygame.display.set_mode((WIDTH, HEIGHT))
active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

    wn.fill((0, 0, 0))

    for x, y in circles:
        pygame.draw.circle(wn, (255, 225, 255), (x, y), 30)

    pygame.display.update()
