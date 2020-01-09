#!/usr/bin/env python

from segment import Segment
import vector as vec
import config
from matplotlib.lines import Line2D


class LineSegment(Segment):
    def __init__(self, data):
        self.pA = vec.Point(data["pA"][0], data["pA"][1])
        self.pB = vec.Point(data["pB"][0], data["pB"][1])

    def draw(self, ax):
        line = Line2D([self.pA.x, self.pA.y], [self.pB.x,
                                               self.pB.y], color=config.PATH_COLOR)
        ax.add_line(line)

    def getFrameRect(self):
        pMin = vec.Point(min(self.pA.x, self.pB.x), min(self.pA.y, self.pB.y))
        pMax = vec.Point(max(self.pA.x, self.pB.x), max(self.pA.y, self.pB.y))
        return (pMin, pMax)

    def intersectionWithLine(self, line):
        if line[0] != 0:
            x = -line[2] / line[0]
            r = (x - self.pB.x) / (self.pA.x - self.pB.x)
            y = r * self.pA.y + (1 - r) * self.pB.y
            return [vec.Point(x, y)]
        elif line[1] != 0:
            y = -line[2] / line[1]
            r = (y - self.pB.y) / (self.pA.y - self.pB.y)
            x = r * self.pA.x + (1 - r) * self.pB.x
            return [vec.Point(x, y)]
        raise ValueError("Passed tuple doesn't represent a line!")
