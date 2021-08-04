import pygame.constants
from point import Point
from ship import Ship
from constants import WIDTH, HEIGHT
from bullet import bullets
from ship import player
import math
import pygame


pygame.init()



window = pygame.display.set_mode((WIDTH, HEIGHT))


while True:
    pygame.event.get()
    pygame.time.delay(10)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.move()
    else:
        player.disable()
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
    
    window.fill((10, 10, 10))
    player.draw(window, (255, 255, 255), 10)
    for b in bullets:
        b.draw(window, (255, 0, 0), 5)


    pygame.display.update()