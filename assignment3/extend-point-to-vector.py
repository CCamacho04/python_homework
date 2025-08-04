#Task 5
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
    
class Vector(Point):
    def __str__(self):
        return f'<{self.x}, {self.y}>'
    
    def  __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    v1 = Vector(1, 1)
    v2 = Vector(4, 6)
    v3 = v1 + v2

    print(p1, "==", p2, ":", p1 == p2)
    print(f'Distance between points: {p1.distance(p2)}')
    print(f'{v1} + {v2} = {v3}')