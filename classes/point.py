from typing import Tuple

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def convert(self) -> Tuple:
        return self.x, self.y
