import pygame
from pygame.locals import *

pygame.init()

white = (255, 255, 255)
black = (  0,   0,   0)
green = (  0, 255,   0)

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
    pygame.draw.line(screen, green, [100, 200], [150, 300], 3)
    pygame.draw.line(screen, green, [150, 300], [200, 200], 3)

    # Flip the buffer and do short delay to maintain framerate
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
