import math

class Matrix:
    def __init__(self, width, height):
        self.m = [[0 for w in range(width)] for h in range(height)]
        self.width = width
        self.height = height

    def multiplyRight(self, l):#self is on the right
        result = Matrix(self.width, l.height)
        for i in range(result.height):
            for j in range(result.width):
                num = 0
                for a in range(l.width):
                    num += l.m[i][a] * self.m[a][j]
                result.m[i][j] = num
        return result
    
    def multiplyNum(self, n):
        result = Matrix(self.width, self.height)
        for i in range(self.height):
            for j in range(self.width):
                result.m[i][j] = self.m[i][j] * n
        return result


    def add(self, r):
        result = Matrix(self.width, self.height)
        for i in range(self.height):
            for j in range(self.width):
                result.m[i][j] = self.m[i][j] + r.m[i][j]
        return result

    def subtract(self, r):
        result = Matrix(self.width, self.height)
        for i in range(self.height):
            for j in range(self.width):
                result.m[i][j] = self.m[i][j] - r.m[i][j]
        return result


    def __str__(self):
        output = ""
        for i in range(self.height):
            for j in range(self.width):
                output += str(self.m[i][j]) + " "
            output += "\n"
        return output