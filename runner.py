import pygame.constants
import pygame
import math
from constants import WIDTH, HEIGHT
from bullet import bullets
from asteroid import Asteroid, asteroids
import asteroid
from ship import player

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

count = 0
while True:
    pygame.event.get()
    pygame.time.delay(10)

    if count == 100:
        asteroids.append(Asteroid())
        count = 0
    else:
        count += 1
        
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

    for a in asteroids:
        a.move()

    if keys[pygame.K_s]:
        player.stop()
    if keys[pygame.K_r]:
        player.reset()
    player.update()
    
    window.fill((10, 10, 10))
    for b in bullets:
        b.draw(window, (255, 0, 0), .5)
    for a in asteroids:
        a.draw(window, (0, 40, 60))
    player.draw(window, (255, 255, 255), 1)

    pygame.display.update()