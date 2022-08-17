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

facex = 50
facey = 50
facewidth = 150
faceheight = 150
facespeed = 5
xchange = facespeed
ychange = facespeed
sound = pygame.mixer.Sound("bounce.wav")

def move_face():
    global facex, facey, xchange, ychange

    if facex <= 0 or facex + 150 >= screenwidth: 
        xchange = xchange * -1
        sound.play()
    if facey <= 0 or facey + 150 >= screenheight: 
        ychange = ychange * -1
        sound.play()

    facex += xchange
    facey += ychange

done = False

while not done:
    # 1. Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 2. Program logic, change variables, etc.
    move_face()

    # 3. Draw stuff
    screen.fill(white)

    # Draw the head
    pygame.draw.ellipse(screen, yellow, [facex, facey, 150, 150], 0)
    pygame.draw.ellipse(screen, black, [facex, facey, 150, 150], 2)

    # Draw the eyes
    pygame.draw.ellipse(screen, black, [facex + 40, facey + 40, 10, 10], 0)
    pygame.draw.ellipse(screen, black, [facex + 100, facey + 40, 10, 10], 0)

    # Draw the mouth
    pygame.draw.line(screen, black, [facex + 45, facey + 100],
                                    [facex + 100, facey + 100], 3)

    # Flip the buffer and do short delay to maintain framerate
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
