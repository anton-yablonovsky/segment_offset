from typing import Tuple


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def convert(self) -> Tuple:
        return self.x, self.y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __truediv__(self, scalar):
        try:
            x = self.x / scalar
            y = self.y / scalar
        except:
            return False

        return Point(x, y)
    
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

