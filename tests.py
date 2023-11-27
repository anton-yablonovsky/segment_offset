import unittest
from classes.point import Point
from classes.polygon import Polygon


class TestStringMethods(unittest.TestCase):
    def test_case_1(self):
        segment_i = 2
        offset = -1.5

        polygon = Polygon(
            [Point(0, 0), Point(0, 500), Point(600, 500), Point(600, 0), Point(0, 0)],
            offset,
            segment_i,
        )

        our_result = polygon.segment_offset()
        correct_result = [(0, 0), (0, 500), (601.5, 500), (601.5, 0), (0, 0)]

        self.assertEqual(our_result, correct_result)

    def test_case_2(self):
        segment_i = 1
        offset = -1

        polygon = Polygon(
            [Point(3, 1), Point(1, 1), Point(1, 2), Point(3, 1)], offset, segment_i
        )

        our_result = polygon.segment_offset()
        correct_result = [(3, 1), (0, 1), (0, 2.5), (3, 1)]

        self.assertEqual(our_result, correct_result)

    def test_case_3(self):
        segment_i = 1
        offset = 1

        polygon = Polygon(
            [Point(3, 1), Point(1, 1), Point(1, 2), Point(3, 1)], offset, segment_i
        )

        our_result = polygon.segment_offset()
        correct_result = [(3, 1), (2, 1), (2, 1.5), (3, 1)]

        self.assertEqual(our_result, correct_result)

    def test_case_4(self):
        segment_i = 1
        offset = 1.5

        polygon = Polygon(
            [Point(3, 1), Point(1, 1), Point(1, 2), Point(3, 1)], offset, segment_i
        )

        our_result = polygon.segment_offset()
        correct_result = [(3, 1), (2.5, 1), (2.5, 1.25), (3, 1)]

        self.assertEqual(our_result, correct_result)


if __name__ == "__main__":
    unittest.main()
