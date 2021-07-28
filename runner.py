import pygame.constants
from point import Point
from ship import Ship
import math
import pygame


pygame.init()
window = pygame.display.set_mode((1500, 1000))



player = Ship([Point(1.5, 0), Point(-1.5, -1), Point(-.5, 0), Point(-1.5, 1)])
bullets = []

while True:
    pygame.event.get()
    pygame.time.delay(10)
    window.fill((10, 10, 10))
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_w]:
        player.move()
    if keys[pygame.K_d]:
        player.rotate(math.pi/90)
    elif keys[pygame.K_a]:
        player.rotate(-math.pi/90)
    if keys[pygame.K_SPACE]:
        player.shoot(bullets)

    for b in bullets:
        b.move()

    if keys[pygame.K_s]:
        player.stop()
    if keys[pygame.K_r]:
        player.reset()
    player.update()
    
    
    player.draw(window, (255, 255, 255), 10, 750, 500)
    for b in bullets:
        b.draw(window, (255, 0, 0), 5, 750, 500)


    pygame.display.update()