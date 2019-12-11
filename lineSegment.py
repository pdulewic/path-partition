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
        line = Line2D([self.pA.x, self.pA.y], [self.pB.x, self.pB.y], color=config.PATH_COLOR)
        ax.add_line(line)

    def getFrameRect(self):
        return (vec.Point(-5,-2), vec.Point(-1,4))