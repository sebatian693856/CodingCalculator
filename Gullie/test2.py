import pygame
pygame.display.set_caption("pong")
pygame.init()

WIDTH, HEIGHT = 1000, 600

ball_x, ball_y = 500, 300
balldirectx = "right"
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerpaddle -= 5
            if event.key == pygame.K_DOWN:
                playerpaddle += 5
            if event.key == pygame.K_w:
                opponentpaddle -= 5
            if event.key == pygame.K_s:
                opponentpaddle += 5

    

    pygame.draw.rect(wn, "red", (900, playerpaddle, 20, playerpaddletall))
    pygame.draw.rect(wn, "blue", (100, opponentpaddle, 20, opponentpaddletall))
    pygame.display.update()
    wn.fill("black")




#    pygame.draw.circle(wn, "BLUE", (ball_x, ball_y), 10)
#    if ball_x >= 1000:
#        playerscore =+ 1
#    if ball_x <= 0:
#        opponentscore =+ 1 
#    if balldirectx == "right":
#        ball_x =+ 0.1
#    if balldirectx == "left":
#        ball_x =- 0.1
    