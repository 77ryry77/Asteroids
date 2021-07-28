from point import Point
import pygame
import math

SPEED = 4
class Bullet:
    def __init__(self, angle, x, y):
        self.points = [Point(.5, .5), Point(.5, -.5), Point(-.5, -.5), Point(-.5, .5)]
        self.x = x
        self.y = y
        self.angle = angle
    
    def scale(self, scaleFactor):
        for point in self.points:
            point.scale(scaleFactor)

    def getDrawCords(self, shiftx, shifty, scale):
        result = []
        for p in self.points:
            result.append(((p.getX()) * scale + self.x + shiftx, (p.getY()) * scale + self.y + shifty))
        return result

    def move(self):
        self.x += math.cos(self.angle) * SPEED
        self.y += math.sin(self.angle) * SPEED

    def draw(self, window, color, scale, shiftx, shifty):
        pygame.draw.lines(window, color, True, self.getDrawCords(shiftx, shifty, scale), 3)