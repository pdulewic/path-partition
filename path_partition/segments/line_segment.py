#!/usr/bin/env python

from segments.segment import Segment
import vector as vec
import config
import utils
from matplotlib.lines import Line2D


class LineSegment(Segment):
    def __init__(self, data):
        self.pA = vec.Point(data["pA"][0], data["pA"][1])
        self.pB = vec.Point(data["pB"][0], data["pB"][1])

    def draw(self, ax):
        line = Line2D(
            [self.pA.x, self.pB.x], [self.pA.y, self.pB.y], color=config.PATH_COLOR
        )
        ax.add_line(line)

    def get_frame_rect(self):
        bottom_left_point = vec.Point(min(self.pA.x, self.pB.x), min(self.pA.y, self.pB.y))
        top_right_point = vec.Point(max(self.pA.x, self.pB.x), max(self.pA.y, self.pB.y))
        return (bottom_left_point, top_right_point)

    def intersection_with_line(self, line):
        known, unknown = utils.check_line_parallelism(line)

        known_value = -line[2] / line[known]
        if 0 == (self.pA[known] - self.pB[known]):
            return []
        r = (known_value - self.pB[known]) / (self.pA[known] - self.pB[known])
        if r < 0 or r > 1:
            return []
        unknown_value = r * self.pA[unknown] + (1 - r) * self.pB[unknown]
        if known:
            return [vec.Point(unknown_value, known_value)]
        return [vec.Point(known_value, unknown_value)]

    def order_points(self, points):
        i = 0  # assuming that segment is not vertical
        if self.pA.x == self.pB.x:
            i = 1  # however, if it is, then sort by y values
        points.sort(key=lambda p: p[i], reverse=(self.pB[i] < self.pA[i]))
        return points
