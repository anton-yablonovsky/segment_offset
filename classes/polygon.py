from typing import List, Tuple
from .point import Point
from .segment import Segment
import math


class Polygon:
    def __init__(self, vertices: List[Point], offset: int, segment_i: int) -> None:
        self.segment_i = segment_i
        self.offset = offset
        self.vertices = vertices
        self.vectors = [
            Segment(self.vertices[i], self.vertices[i + 1])
            for i in range(len(self.vertices))
            if i != len(self.vertices) - 1
        ]
        self.segment_direction = [
            Segment(self.vertices[i], self.vertices[i + 1]).segment_direction()
            for i in range(len(self.vertices))
            if i != len(self.vertices) - 1
        ]

    def line_intersection(self, line1: Segment, line2: Segment) -> Point:
        x1, y1 = line1.start_point.x, line1.start_point.y
        x2, y2 = line1.end_point.x, line1.end_point.y
        x3, y3 = line2.start_point.x, line2.start_point.y
        x4, y4 = line2.end_point.x, line2.end_point.y

        xdiff, ydiff = (x1 - x2, x3 - x4), (y1 - y2, y3 - y4)

        def det(a, b):
            try:
                return a.x * b.y - a.y * b.x
            except:
                return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)

        if div == 0:
            return False

        d = (
            det(line1.start_point, line1.end_point),
            det(line2.start_point, line2.end_point),
        )

        return Point(det(d, xdiff) / div, det(d, ydiff) / div)  # x, y

    def parallel_line_points(self, point1: Point, point2: Point) -> Tuple[Point]:
        # Check if the line is vertical
        # Calculate the slope of the initial line
        modify_offset = (
            self.offset * self.segment_direction[self.segment_i]
        )  # depends on direction
        m = Segment(point1, point2).get_slope()
        if m == None:
            return Point(point1.x + modify_offset, point1.y), Point(
                point2.x + modify_offset, point2.y
            )

        # Calculate the perpendicular slope
        m_perpendicular = -1 / m

        # Calculate the offset
        dx = modify_offset / math.sqrt(1 + m_perpendicular ** 2)
        dy = m_perpendicular * dx

        # Calculate the coordinates of the new points for the parallel line
        return Point(point1.x + dx, point1.y + dy), Point(point2.x + dx, point2.y + dy)

    def segment_offset(self) -> List[Tuple]:
        projection_point1, projection_point2 = self.parallel_line_points(
            self.vertices[self.segment_i],  # x1, y1
            self.vertices[self.segment_i + 1],  # x2, y2
        )

        parallel_line = Segment(projection_point1, projection_point2)
        intersection_lst = [
            intersection
            for vector in self.vectors
            if (intersection := self.line_intersection(parallel_line, vector))
        ]
        copy_vert = self.vertices.copy()
        copy_vert[self.segment_i] = intersection_lst[0]
        copy_vert[self.segment_i + 1] = intersection_lst[1]
        return [point.convert() for point in copy_vert]
