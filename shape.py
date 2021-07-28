from point import Point
import pygame
import math

class Shape:
    def __init__(self, points):
        self.points = points
        self.x = 0
        self.xv = 0
        self.y = 0
        self.yv = 0
        self.angle = 0

    def rotate(self, angle):
        for point in self.points:
            point.rotate(angle)
        self.angle += angle
    
    def scale(self, scaleFactor):
        for point in self.points:
            point.scale(scaleFactor)

    def getDrawCords(self, shiftx, shifty, scale):
        result = []
        for p in self.points:
            result.append(((p.getX()) * scale + self.x + shiftx, (p.getY()) * scale + self.y + shifty))
        return result

    def move(self):
        self.xv += math.cos(self.angle)/50
        if self.xv > 2:
            self.xv = 2
        if self.xv < -2:
            self.xv = -2
        self.yv += math.sin(self.angle)/50
        if self.yv > 2:
            self.yv = 2
        if self.yv < -2:
            self.yv = -2
    
    def update(self):
        self.x += self.xv
        self.y += self.yv

    def draw(self, window, color, scale, shiftx, shifty):
        pygame.draw.lines(window, color, True, self.getDrawCords(shiftx, shifty, scale), 3)