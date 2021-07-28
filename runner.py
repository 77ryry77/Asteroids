from pygame.constants import K_a, K_w
from shape import Shape
from point import Point
from shape import Shape
import math
import pygame


pygame.init()
window = pygame.display.set_mode((500, 500))



a = Shape([Point(1, 0), Point(-1, -1), Point(-1, 1)])

while True:
    pygame.event.get()
    pygame.time.delay(10)
    window.fill((10, 10, 10))
    a.draw(window, (255, 255, 255), 10, 250)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        a.move(1)
    elif keys[pygame.K_d]:
        a.rotate(math.pi/180)
    elif keys[pygame.K_a]:
        a.rotate(-math.pi/180)
    pygame.display.update()