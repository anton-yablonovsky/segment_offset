from typing import List, Tuple
from .point import Point
from .segment import Segment
import math


class Polygon:
    def __init__(self, vertices: List[Point], offset: int, segment_i: int) -> None:
        self.segment_i = segment_i
        self.vertices = vertices
        self.offset = offset
        """self.offset_with_direction = (
            self.offset
            * Segment(
                self.vertices[segment_i], self.vertices[segment_i + 1]
            ).segment_direction()
        )
        self.vectors = [
            Segment(self.vertices[i], self.vertices[i + 1])
            for i in range(len(self.vertices))
            if i != len(self.vertices) - 1
        ]"""

    def line_intersection(self, line1: Segment, line2: Segment) -> Point:
        # https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
        x1, y1 = line1.start_point.x, line1.start_point.y
        x2, y2 = line1.end_point.x, line1.end_point.y
        x3, y3 = line2.start_point.x, line2.start_point.y
        x4, y4 = line2.end_point.x, line2.end_point.y
        try:
            px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            )
            py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            )
        except:
            return False
        return Point(px, py)

    def parallel_line_points(self, point1: Point, point2: Point) -> Tuple[Point]:
        # https://www.cuemath.com/geometry/slope/
        # m - slope, or tg of the angle between the line and ox
        # b - line`s y-intersept.
        # m_original == m_parallel
        # y_original = m_original * x_original + b_original
        # y_parallel = m_original * x_original + b_parallel
        # b_parallel = b_original + offset_with_direction

        m = Segment(point1, point2).get_slope()
        if m == None:
            return Point(point1.x + self.offset_with_direction, point1.y), Point(
                point2.x + self.offset_with_direction, point2.y
            )

        b_original = point1.y - m * point1.x
        b_parallel = b_original + self.offset_with_direction

        y1_parallel = -5
        y2_parallel = -10

        x1_parallel = (y1_parallel - b_parallel) / m
        x2_parallel = (y2_parallel - b_parallel) / m

        return Point(x1_parallel, y1_parallel), Point(x2_parallel, y2_parallel)

    def segment_offset(self) -> List[Tuple]:
        # I think issue with icorrect polygon is here.
        p1 = self.vertices[self.segment_i]
        p2 = self.vertices[self.segment_i + 1]
        v1 = Point(p2.x - p1.x, p2.y - p1.y)
        v2 = Point(p1.x - p2.x, p1.y - p2.y)
        d = ((p2.x - p1.x) ** 2 * (p2.y - p1.y) ** 2) ** 1/2

        unit_vector_1 = v1 / d
        unit_vector_2 = v2 / d

        x_unit_rotate_vector_1 = unit_vector_1.x * math.cos(math.pi / 2) - unit_vector_1.y * math.sin(math.pi / 2)
        y_unit_rotate_vector_1 = unit_vector_1.x * math.sin(math.pi / 2) + unit_vector_1.y * math.cos(math.pi / 2)

        unit_rotate_vector_1 = Point(x_unit_rotate_vector_1, y_unit_rotate_vector_1)

        x_unit_rotate_vector_2 = unit_vector_2.x * math.cos(-math.pi / 2) - unit_vector_2.y * math.sin(-math.pi / 2)
        y_unit_rotate_vector_2 = unit_vector_2.x * math.sin(-math.pi / 2) + unit_vector_2.y * math.cos(-math.pi / 2)

        unit_rotate_vector_2 = Point(x_unit_rotate_vector_2, y_unit_rotate_vector_2)

        rotate_vector_1 = unit_rotate_vector_1 * abs(self.offset)
        rotate_vector_2 = unit_rotate_vector_2 * abs(self.offset)

        return (rotate_vector_1 + p1).convert(), (rotate_vector_2 + p2).convert()
        
        """projection_point1, projection_point2 = self.parallel_line_points(
            self.vertices[self.segment_i],  # x1, y1 parallel
            self.vertices[self.segment_i + 1],  # x2, y2 parallel
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
        return [point.convert() for point in copy_vert]"""
