import pygame
pygame.display.set_caption("pong")
pygame.init()

WIDTH, HEIGHT = 1000, 600

ball_x, ball_y = 500, 100

wn = pygame.display.set_mode((WIDTH, HEIGHT))
active = True
while active:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            active = False
    pygame.draw.circle(wn, (255, 225, 255), (ball_x, ball_y), 30)
    pygame.display.update()