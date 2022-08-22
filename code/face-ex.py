import pygame
from pygame.locals import *

pygame.init()

white = (255, 255, 255)
black = (  0,   0,   0)
red = (255, 0, 0)
green = (0, 255, 0)
turquoise = (0, 255, 255)
yellow = (255, 255, 0)

class Circle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 100
        self.h = 100
        self.color = black
        
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color,
                            [self.x, self.y, self.w, self.h], 0)

class Face(Circle):
    def __init__(self):
        super().__init__()
        
    def draw(self, screen):
        super().draw(screen)
        
        x1 = self.x + (self.w / 3)
        x2 = x1 + (self.w / 3)
        y1 = self.y + (self.h / 3)
        y2 = y1 + (self.h / 3)
        
        pygame.draw.ellipse(screen, black, [x1, y1, 5, 5], 0)
        pygame.draw.ellipse(screen, black, [x2, y1, 5, 5], 0)
        pygame.draw.line(screen, black, [x1, y2], [x2, y2], 3)

        
screenwidth = 800
screenheight = 600
screensize = [screenwidth, screenheight]
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Drawing with Classes")

clock = pygame.time.Clock()


done = False

c1 = Circle()

c2 = Circle()
c2.x = 100
c2.y = 200
c2.w = 200
c2.h = 275
c2.color = turquoise

f1 = Face()
f1.x = 400
f1.y = 200
f1.w = 200
f1.h = 200
f1.color = yellow

f2 = Face()
f2.x = 450
f2.y = 450
f2.w = 75
f2.h = 75
f2.color = green

redface = Face()
redface.x = 300
redface.y = 50
redface.w = 200
redface.h = 100
redface.color = red

while not done:
    # 1. Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 2. Program logic, change variables, etc.

    # 3. Draw stuff
    screen.fill(white)
    c1.draw(screen)
    c2.draw(screen)
    f1.draw(screen)
    f2.draw(screen)
    redface.draw(screen)

    pygame.display.flip()
    clock.tick(20)


pygame.quit()
