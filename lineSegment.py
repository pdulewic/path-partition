#!/usr/bin/env python

from segment import Segment
import vector as vec
import config 
import utils 
from matplotlib.lines import Line2D


class LineSegment(Segment):
    def __init__(self, data):
        self.pA = vec.Point(data["pA"][0], data["pA"][1])
        self.pB = vec.Point(data["pB"][0], data["pB"][1])

    def draw(self, ax):
        line = Line2D([self.pA.x, self.pB.x], [self.pA.y,
                                               self.pB.y], color=config.PATH_COLOR)
        ax.add_line(line)

    def getFrameRect(self):
        pMin = vec.Point(min(self.pA.x, self.pB.x), min(self.pA.y, self.pB.y))
        pMax = vec.Point(max(self.pA.x, self.pB.x), max(self.pA.y, self.pB.y))
        return (pMin, pMax)

    def intersectionWithLine(self, line):
        known, unknown = utils.checkLineParallelism(line)

        knownValue = -line[2] / line[known]
        if 0 == (self.pA[known] - self.pB[known]):
            return []
        r = (knownValue - self.pB[known]) / (self.pA[known] - self.pB[known])
        if r < 0 or r > 1:
            return []
        unknownValue = r * self.pA[unknown] + (1 - r) * self.pB[unknown]
        if known:
            return [vec.Point(unknownValue, knownValue)]
        return [vec.Point(knownValue, unknownValue)]

    def orderPoints(self, points):
        i = 0  # assuming that segment is not vertical
        if self.pA.x == self.pB.x:
            i = 1   # however, if it is, then sort by y values
        points.sort(key=lambda p: p[i], reverse=(self.pB[i] < self.pA[i]))
        return points
