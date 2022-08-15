import pygame
from pygame.locals import *

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

screenwidth = 800
screenheight = 600
screensize = [screenwidth, screenheight]
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("WINDOW TITLE HERE")

clock = pygame.time.Clock()

done = False

while not done:
    # 1. Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 2. Program logic, change variables, etc.

    # 3. Draw stuff
    screen.fill(white)
    pygame.draw.ellipse(screen, yellow, [50, 50, 400, 400], 0)
    pygame.draw.ellipse(screen, black, [50, 50, 400, 400], 2)

    pygame.draw.ellipse(screen, black, [145, 145, 50, 50], 0)
    pygame.draw.ellipse(screen, black, [300, 145, 50, 50], 0)
    pygame.draw.line(screen, black, [175, 340], [325, 340], 6)

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
