#!/usr/bin/env python

#import vector as vec
from abc import ABCMeta, abstractmethod
import pathpartition.utils as utils


class Segment:
    __metaclass__ = ABCMeta

    # draw segment on 'ax' using matplotlib functions   
    @abstractmethod
    def draw(self, ax): raise NotImplementedError
    # returns bottom left and top right points defining a rectangle that fully
    # covers the segment
    @abstractmethod
    def getFrameRect(self): raise NotImplementedError
    # returns points of intersection of segment and line Ax + By + C = 0
    # represented as list line == [A, B, C]. Works only for lines parallel to
    # OX or OY!
    @abstractmethod
    def intersectionWithLine(self, line): raise NotImplementedError
    # sorts points according to their distance from the beginning of the sector
    @abstractmethod
    def orderPoints(self, points): raise NotImplementedError


    # TBD
    def calculateStageBorders(self, d):
        points = []
        frameRect = self.getFrameRect()
        for i in [0, 1]:
            tesselationLines = utils.tesselationLinesBetween(frameRect[0][i], frameRect[1][i], d)
            for lineCoordinate in tesselationLines:
                # list [A, B, C] representing line Ax + By + C = 0
                line = [0, 0, -lineCoordinate]
                line[i] = 1 
                points += self.intersectionWithLine(line)
        points = utils.removeDuplicatesPreservingOrder(points)
        return self.orderPoints(points)

