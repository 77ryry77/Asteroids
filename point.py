from matrix import Matrix
import math

class Point:

    def rotate(self, angle):
        rotator = Matrix(2, 2)
        rotator.m[0][0] = math.cos(angle)
        rotator.m[0][1] = -math.sin(angle)
        rotator.m[1][0] = math.sin(angle)
        rotator.m[1][1] = math.cos(angle)
        self.cords = self.cords.multiplyRight(rotator)
    
    def move(self, x, y):
        changes = Matrix(1, 2)
        changes.m[0][0] = x
        changes.m[1][0] = y
        self.cords = self.cords.add(changes)

    def scale(self, scaleFactor):
        self.cords = self.cords.multiplyNum(scaleFactor)

    def getX(self):
        return self.cords.m[0][0]
    def getY(self):
        return self.cords.m[1][0]

    def __str__(self):
        return self.cords.__str__()

    def __init__(self, x, y):
        self.cords = Matrix(1, 2)
        self.move(x, y)