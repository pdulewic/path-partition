#!/usr/bin/env python

import vector as vec
from abc import ABCMeta, abstractmethod

class Segment:
    __metaclass__ = ABCMeta

    @abstractmethod
    # draw segment on 'ax' using matplotlib functions
    def draw(self, ax): raise NotImplementedError
    # returns bottom left and top right points defining a rectangle that fully 
    # covers the segment
    def getFrameRect(self): raise NotImplementedError
