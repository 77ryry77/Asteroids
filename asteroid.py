from point import Point
import pygame
import math
import random
from constants import WIDTH, HEIGHT, SPEED

asteroids = []

starters = [
    [-1, 2],
    [1, 2],
    [2, 1],
    [2, -1],
    [1, -2],
    [-1, -2],
    [-2, -1],
    [-2, 1]
]

class Asteroid:
    def __init__(self):
        self.points = []
        for p in starters:
            x = p[0] + random.random() * 2 - 1
            y = p[1] + random.random() * 2 - 1
            chance = random.randint(0, len(starters))
            if chance != 0:
                self.points.append(Point(x, y))

        dir = random.random() * 2 * math.pi
        for point in self.points:
            point.rotate(dir)
        self.scale = random.randint(5, 25)
        
        self.x = 0
        self.y = 0
        self.angle = 0
    
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
        self.x += math.cos(self.angle) * SPEED
        self.y += math.sin(self.angle) * SPEED

        actualX = self.x + WIDTH / 2
        if actualX > WIDTH or actualX < 0:
            asteroids.remove(self)
        actualY = self.y + HEIGHT / 2
        if actualY > HEIGHT or actualY < 0:
            asteroids.remove(self)

    def draw(self, window, color):
        pygame.draw.polygon(window, color, self.getDrawCords())