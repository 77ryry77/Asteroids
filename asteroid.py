from point import Point
import pygame
import math
import random
from constants import WIDTH, HEIGHT, ASPEED, STARTERS

asteroids = []

class Asteroid:
    def __init__(self):
        self.points = []
        for p in STARTERS:
            x = p[0] + random.random() * 2 - 1
            y = p[1] + random.random() * 2 - 1
            chance = random.randint(0, len(STARTERS))
            if chance != 0:
                self.points.append(Point(x, y))

        dir = random.random() * 2 * math.pi
        for point in self.points:
            point.rotate(dir)
        self.scale = random.randint(10, 25)

        side = random.randint(0, 3)
        if side == 0:
            self.x = random.randint(-WIDTH/2, WIDTH/2)
            self.y = -HEIGHT/2
            self.angle = random.random() * math.pi
        elif side == 1:
            self.y = random.randint(-HEIGHT/2, HEIGHT/2)
            self.x = WIDTH/2
            self.angle = random.random() * math.pi + math.pi / 2
        elif side == 2:
            self.x = random.randint(-WIDTH/2, WIDTH/2)
            self.y = HEIGHT/2
            self.angle = random.random() * math.pi + math.pi
        else:
            self.y = random.randint(-HEIGHT/2, HEIGHT/2)
            self.x = -WIDTH/2
            self.angle = random.random() * math.pi - math.pi / 2
        
        self.speed = random.randint(ASPEED - ASPEED / 2, ASPEED + ASPEED / 2)

    def scale(self, scaleFactor):
        for point in self.points:
            point.scale(scaleFactor)

    def getDrawCords(self):
        shiftx = WIDTH / 2
        shifty = HEIGHT / 2
        result = []
        for p in self.points:
            result.append(((p.getX()) * self.scale + self.x + shiftx, (p.getY()) * self.scale + self.y + shifty))
        return result

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        actualX = self.x + WIDTH / 2
        if actualX > WIDTH or actualX < 0:
            asteroids.remove(self)
        actualY = self.y + HEIGHT / 2
        if actualY > HEIGHT or actualY < 0:
            asteroids.remove(self)

    def draw(self, window, color):
        pygame.draw.polygon(window, color, self.getDrawCords())
        pygame.draw.lines(window, (255, 255, 255), True, self.getDrawCords(), 3)