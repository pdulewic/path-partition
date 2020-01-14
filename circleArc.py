#!/usr/bin/env python

from segment import Segment
import vector as vec
import config 
import utils 
from matplotlib.patches import Arc
from math import sin, cos, radians, degrees, sqrt


def isAngleWithinRange(startAngle, endAngle, pointAngle):
    if not (0 <= startAngle <= 360 and 0 <= endAngle <= 360 and 0 <= pointAngle <= 360):
        raise ValueError("Angle outside range (0,360)")
    if startAngle <= endAngle:
        return pointAngle >= startAngle and pointAngle <= endAngle
    return pointAngle >= startAngle or pointAngle <= endAngle


def isPointInsideCircleArc(point, circle):
    pAngle = degrees(vec.angle(point - circle.center))
    return isAngleWithinRange(circle.theta1, circle.theta2, pAngle)


class CircleArc(Segment):
    def __init__(self, data):
        self.center = vec.Point(data["center"][0], data["center"][1])
        self.radius = data["radius"]
        self.theta1 = data["theta1"]
        self.theta2 = data["theta2"]
        self.startsFromA = data["startsFromA"]

    def draw(self, ax):
        arc = Arc((self.center.x, self.center.y), self.radius * 2, self.radius * 2,
                  0, self.theta1, self.theta2, color=config.PATH_COLOR)
        ax.add_patch(arc)

    def getFrameRect(self):
        xCoords = [self.center[0] + self.radius *
                   cos(radians(self.theta1)), self.center[0] + self.radius * cos(radians(self.theta2))]
        yCoords = [self.center[1] + self.radius *
                   sin(radians(self.theta1)), self.center[1] + self.radius * sin(radians(self.theta2))]

        for angle in range(0, 360, 90):
            if isAngleWithinRange(self.theta1, self.theta2, angle):
                xCoords.append(
                    self.center[0] + self.radius * round(cos(radians(angle))))
                yCoords.append(
                    self.center[1] + self.radius * round(sin(radians(angle))))

        pMin = vec.Point(min(xCoords), min(yCoords))
        pMax = vec.Point(max(xCoords), max(yCoords))
        return (pMin, pMax)

    def intersectionWithLine(self, line):
        known, unknown = utils.checkLineParallelism(line)

        knownValue = -line[2] / line[known]
        if knownValue < self.center[known] - self.radius or knownValue > self.center[known] + self.radius:
            return []
        tmp = self.radius**2 - (knownValue - self.center[known])**2
        if tmp < 0:
            return []
        unknownValue1 = self.center[unknown] + sqrt(tmp)
        unknownValue2 = self.center[unknown] - sqrt(tmp)
        if known:
            result = [vec.Point(unknownValue1, knownValue),
                      vec.Point(unknownValue2, knownValue)]
        else:
            result = [vec.Point(knownValue, unknownValue1),
                      vec.Point(knownValue, unknownValue2)]
        result = utils.removeDuplicatesPreservingOrder(result)
        # remove points outside arc
        return [p for p in result if isPointInsideCircleArc(p, self)]

    def orderPoints(self, points):
        points.sort(key=lambda p: vec.angle(p - self.center), reverse=not self.startsFromA)
        if self.theta1 > self.theta2 and points:
            if self.startsFromA:
                if degrees(vec.angle(points[0] - self.center)) < self.theta1:
                    while degrees(vec.angle(points[-1] - self.center)) >= self.theta1:
                        points.insert(0, points.pop())
            else:
                if degrees(vec.angle(points[0] - self.center)) > self.theta2:
                    while degrees(vec.angle(points[-1] - self.center)) <= self.theta2:
                        points.insert(0, points.pop())  
        return points
