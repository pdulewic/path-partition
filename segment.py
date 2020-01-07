#!/usr/bin/env python

import vector as vec
from abc import ABCMeta, abstractmethod
import config
import math


def tesselationLinesBetween(begin, end, d):
    if d < 2 * config.ROBOT_RADIUS:
        raise ValueError("Given parameter d is smaller then double of robot radius!")

    dMin = math.floor(begin / d)
    dMax = math.ceil(end / d)
    result = []
    for i in range(dMin, dMax + 1):
        for sign in [-1,1]:
            value = i * d + config.ROBOT_RADIUS * sign
            if begin <= value <= end:
                result.append(value)
    return result

class Segment:
    __metaclass__ = ABCMeta

    @abstractmethod
    # draw segment on 'ax' using matplotlib functions
    def draw(self, ax): raise NotImplementedError
    # returns bottom left and top right points defining a rectangle that fully
    # covers the segment
    def getFrameRect(self): raise NotImplementedError
