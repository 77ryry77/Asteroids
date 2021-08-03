from point import Point
from bullet import Bullet
from constants import HEIGHT, WIDTH
import pygame
import math

class Ship:
    def __init__(self, points, boosterCords):
        self.points = points
        self.x = 0
        self.xv = 0
        self.y = 0
        self.yv = 0
        self.angle = 0
        self.fireCoolDown = 0
        self.booster = boosterCords
        self.thrusting = False

    def rotate(self, angle):
        for point in self.points:
            point.rotate(angle)
        for point in self.booster:
            point.rotate(angle)
        self.angle += angle
    
    def scale(self, scaleFactor):
        for point in self.points:
            point.scale(scaleFactor)

    def getDrawCords(self, scale):
        shiftx = WIDTH/2
        shifty = HEIGHT/2
        result = []
        for p in self.points:
            result.append(((p.getX()) * scale + self.x + shiftx, (p.getY()) * scale + self.y + shifty))
        return result

    def getBoosterCords(self, scale):
        shiftx = WIDTH/2
        shifty = HEIGHT/2
        result = []
        for p in self.booster:
            result.append(((p.getX()) * scale + self.x + shiftx, (p.getY()) * scale + self.y + shifty))
        return result

    def disable(self):
        self.thrusting = False

    def move(self):
        self.thrusting = True
        self.xv += math.cos(self.angle)/35
        if self.xv > 2:
            self.xv = 2
        if self.xv < -2:
            self.xv = -2
        self.yv += math.sin(self.angle)/35
        if self.yv > 2:
            self.yv = 2
        if self.yv < -2:
            self.yv = -2
    
    def update(self):
        self.x += self.xv
        self.y += self.yv
        if self.fireCoolDown > 0:
            self.fireCoolDown -= 1

    def shoot(self, bullets):
        if self.fireCoolDown == 0:
            bullets.append(Bullet(self.angle, self.x, self.y))
            self.fireCoolDown = 10

            self.xv += -math.cos(self.angle)/10
            if self.xv > 2:
                self.xv = 2
            if self.xv < -2:
                self.xv = -2
            self.yv += -math.sin(self.angle)/10
            if self.yv > 2:
                self.yv = 2
            if self.yv < -2:
                self.yv = -2

    def stop(self):
        self.xv = 0
        self.yv = 0

    def reset(self):
        self.stop()
        self.x = 0
        self.y = 0

    def draw(self, window, color, scale):
        pygame.draw.lines(window, color, True, self.getDrawCords(scale), 3)
        if self.thrusting:
            pygame.draw.polygon(window, (255, 0, 0), self.getBoosterCords(scale))