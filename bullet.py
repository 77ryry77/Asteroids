from point import Point
import pygame
import math
from constants import WIDTH, HEIGHT, BSPEED

bullets = []


class Bullet:
    def __init__(self, angle, x, y):
        self.points = [Point(5, 5), Point(5, -5), Point(-5, -5), Point(-5, 5)]
        self.x = x
        self.y = y
        self.angle = angle
    
    def scale(self, scaleFactor):
        for point in self.points:
            point.scale(scaleFactor)

    def getDrawCords(self, scale):
        shiftx = WIDTH / 2
        shifty = HEIGHT / 2
        result = []
        for p in self.points:
            result.append(((p.getX()) * scale + self.x + shiftx, (p.getY()) * scale + self.y + shifty))
        return result

    def move(self):
        self.x += math.cos(self.angle) * BSPEED
        self.y += math.sin(self.angle) * BSPEED

        actualX = self.x + WIDTH / 2
        if actualX > WIDTH or actualX < 0:
            bullets.remove(self)
        actualY = self.y + HEIGHT / 2
        if actualY > HEIGHT or actualY < 0:
            bullets.remove(self)

    def draw(self, window, color, scale):
        pygame.draw.lines(window, color, True, self.getDrawCords(scale), 3)