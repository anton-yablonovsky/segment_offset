from .point import Point


class Segment:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        self.start_point = start_point
        self.end_point = end_point

    def segment_direction(self) -> int:
        if (
            self.start_point.x < self.end_point.x
            and self.start_point.y < self.end_point.y
        ):
            return -1

        elif (
            self.start_point.x > self.end_point.x
            and self.start_point.y > self.end_point.y
        ):
            return 1

        elif (
            self.start_point.x < self.end_point.x
            and self.start_point.y > self.end_point.y
        ):
            return -1

        elif (
            self.start_point.x > self.end_point.x
            and self.start_point.y < self.end_point.y
        ):
            return 1

        elif (
            self.start_point.x == self.end_point.x
            and self.start_point.y < self.end_point.y
        ):
            return 1

        elif (
            self.start_point.x == self.end_point.x
            and self.start_point.y > self.end_point.y
        ):
            return -1

    def get_slope(self) -> float:

        if self.start_point.x == self.end_point.x:
            # If the line is vertical, set slope to None (undefined)
            return None

        else:
            return (self.end_point.y - self.start_point.y) / (
                self.end_point.x - self.start_point.x
            )
