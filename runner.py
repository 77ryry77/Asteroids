from pygame.constants import K_a, K_w
from shape import Shape
from point import Point
from shape import Shape
import math
import pygame


pygame.init()
window = pygame.display.set_mode((1500, 1000))



a = Shape([Point(1.5, 0), Point(-1.5, -1), Point(-.5, 0), Point(-1.5, 1)])

while True:
    pygame.event.get()
    pygame.time.delay(10)
    window.fill((10, 10, 10))
    a.draw(window, (255, 255, 255), 10, 750, 500)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        a.move()
    elif keys[pygame.K_d]:
        a.rotate(math.pi/90)
    elif keys[pygame.K_a]:
        a.rotate(-math.pi/90)
    a.update()
    pygame.display.update()