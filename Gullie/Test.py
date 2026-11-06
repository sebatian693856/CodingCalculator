import pygame
pygame.display.set_caption("pong")
pygame.init()

WIDTH, HEIGHT = 1000, 600

ball_x, ball_y = 500, 300
balldirectx = "right"
balldirecty = "up"
playerscore = 0
opponentscore = 0
playerpaddle = 0
playerpaddletall = 100
opponentpaddle = 0
opponentpaddletall = 100

wn = pygame.display.set_mode((WIDTH, HEIGHT))
active = True
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    playerinput = pygame.key.get_pressed()
    if playerinput[pygame.K_UP] and playerpaddle >= 0:
        playerpaddle -= 0.5
    if playerinput[pygame.K_DOWN] and playerpaddle <= 500:
        playerpaddle += 0.5
    if playerinput[pygame.K_w] and opponentpaddle >= 0:
        opponentpaddle -= 0.2
    if playerinput[pygame.K_s] and opponentpaddle <= 500:
        opponentpaddle += 0.2
    pygame.draw.rect(wn, "red", (900, playerpaddle, 20, playerpaddletall))
    pygame.draw.rect(wn, "blue", (100, opponentpaddle, 20, opponentpaddletall))
    pygame.draw.circle(wn, "GREEN", (ball_x, ball_y), 10)
    pygame.display.update()

    pygame.draw.circle(wn, "GREEN", (ball_x, ball_y), 10)

    if ball_x >= 50 and ball_x <= 100 and ball_y >= opponentpaddle and ball_y <= opponentpaddle + 100:
        balldirectx = "right"
    if ball_x <= 1000 and ball_x >= 900 and ball_y >= playerpaddle and ball_y <= playerpaddle + 100:
        balldirectx = "left"
    if ball_y > 600:
        balldirecty = "down"
    if ball_y < 0:
        balldirecty = "up"
    if ball_x > 1000:
        opponentscore += 1
        ball_x = 500
        ball_y = 300
    if ball_x < 0:
        playerscore += 1
        ball_x = 500
        ball_y = 300
    if balldirectx == "right":
        ball_x += 0.1
    if balldirectx == "left":
        ball_x -= 0.1
    if balldirecty == "up":
        ball_y += 0.1
    if balldirecty == "down":
        ball_y -= 0.1
    wn.fill("black")