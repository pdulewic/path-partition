#!/usr/bin/env python

from segment import Segment
import vector as vec
import config
from matplotlib.patches import Arc

class CircleArc(Segment):
    def __init__(self, data):
        self.center = vec.Point(data["center"][0], data["center"][1])
        self.radius = data["radius"]
        self.theta1 = data["theta1"]
        self.theta2 = data["theta2"]
        self.startsFromA = data["startsFromA"]

    def draw(self, ax):
        arc = Arc((self.center.x, self.center.y), self.radius, self.radius, 0, self.theta1, self.theta2, color=config.PATH_COLOR)
        ax.add_patch(arc)

    def getFrameRect():
        return 0

