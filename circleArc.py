#!/usr/bin/env python

from segment import Segment
import vector as vec
import config
from matplotlib.patches import Arc
from math import sin, cos, radians


def isPointInsideCircle(startAngle, endAngle, pointAngle):
    if startAngle <= endAngle:
        return pointAngle >= startAngle and pointAngle <= endAngle
    return pointAngle >= startAngle or pointAngle <= endAngle


class CircleArc(Segment):
    def __init__(self, data):
        self.center = vec.Point(data["center"][0], data["center"][1])
        self.radius = data["radius"]
        self.theta1 = data["theta1"]
        self.theta2 = data["theta2"]
        self.startsFromA = data["startsFromA"]

    def draw(self, ax):
        arc = Arc((self.center.x, self.center.y), self.radius, self.radius,
                  0, self.theta1, self.theta2, color=config.PATH_COLOR)
        ax.add_patch(arc)

    def getFrameRect(self):
        xCoords = [self.center[0] + self.radius *
                   cos(radians(self.theta1)), self.center[0] + self.radius * cos(radians(self.theta2))]
        yCoords = [self.center[1] + self.radius *
                   sin(radians(self.theta1)), self.center[1] + self.radius * sin(radians(self.theta2))]

        for angle in range(0, 360, 90):
            if isPointInsideCircle(self.theta1, self.theta2, angle):
                xCoords.append(
                    self.center[0] + self.radius * round(cos(radians(angle))))
                yCoords.append(
                    self.center[1] + self.radius * round(sin(radians(angle))))

        pMin = vec.Point(min(xCoords), min(yCoords))
        pMax = vec.Point(max(xCoords), max(yCoords))
        return (pMin, pMax)
