from point import Point
import pygame
import math

class Shape:
    def __init__(self, points):
        self.points = points
        self.x = 0
        self.y = 0
        self.angle = 0

    def rotate(self, angle):
        for point in self.points:
            point.rotate(angle)
        self.angle += angle
    
    def scale(self, scaleFactor):
        for point in self.points:
            point.scale(scaleFactor)

    def getDrawCords(self, shift, scale):
        result = []
        for p in self.points:
            result.append(((p.getX()) * scale + self.x + shift, (p.getY()) * scale + self.y + shift))
        return result

    def move(self, distance):
        self.x += math.cos(self.angle) * distance
        self.y += math.sin(self.angle) * distance

    def draw(self, window, color, scale, shift):
        pygame.draw.lines(window, color, True, self.getDrawCords(shift, scale), 3)