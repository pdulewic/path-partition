#!/usr/bin/env python

class Path:
    def __init__(self, ID):
        self.pathID = ID
        self.segments = []
        self.numberOfSegments = 0

    def append(self, segment):
        self.segments.append(segment)
        self.numberOfSegments += 1
