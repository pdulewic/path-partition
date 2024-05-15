#!/usr/bin/env python

from path_partition.segments.segment import Segment
from path_partition.vector import Point
from path_partition.config import PATH_COLOR
from path_partition.utils import check_line_parallelism
from matplotlib.lines import Line2D
from typing import Tuple


class LineSegment(Segment):
    def __init__(self, data: dict) -> None:
        self.pA = Point(data["pA"][0], data["pA"][1])
        self.pB = Point(data["pB"][0], data["pB"][1])

    def draw(self, ax) -> None:
        line = Line2D([self.pA.x, self.pB.x], [self.pA.y, self.pB.y], color=PATH_COLOR)
        ax.add_line(line)

    def get_frame_rect(self) -> Tuple[Point, Point]:
        bottom_left_point = Point(min(self.pA.x, self.pB.x), min(self.pA.y, self.pB.y))
        top_right_point = Point(max(self.pA.x, self.pB.x), max(self.pA.y, self.pB.y))
        return (bottom_left_point, top_right_point)

    def intersection_with_line(self, line) -> list[Point]:
        known, unknown = check_line_parallelism(line)

        known_value = -line[2] / line[known]
        if 0 == (self.pA[known] - self.pB[known]):
            return []
        r = (known_value - self.pB[known]) / (self.pA[known] - self.pB[known])
        if r < 0 or r > 1:
            return []
        unknown_value = r * self.pA[unknown] + (1 - r) * self.pB[unknown]
        if known:
            return [Point(unknown_value, known_value)]
        return [Point(known_value, unknown_value)]

    def order_points(self, points: list[Point]) -> list[Point]:
        i = 0  # assuming that segment is not vertical
        if self.pA.x == self.pB.x:
            i = 1  # however, if it is, then sort by y values
        points.sort(key=lambda p: p[i], reverse=(self.pB[i] < self.pA[i]))
        return points
