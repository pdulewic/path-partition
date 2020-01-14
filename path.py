#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
import utils

def displayPoints(ax, points):
    x_axes = []
    y_axes = []
    for point in points:
        x_axes.append(point.x)
        y_axes.append(point.y)
    ax.plot(x_axes, y_axes, 'ro')

def displayTesselationLines(ax, plt, d):
    xLines = utils.tesselationLinesBetween(plt.xlim()[0], plt.xlim()[1], d)
    for x in xLines:
        line = Line2D([x, x], [plt.ylim()[0], plt.ylim()[1]], color="grey", linestyle="--")
        ax.add_line(line)

    yLines = utils.tesselationLinesBetween(plt.ylim()[0], plt.ylim()[1], d)
    for y in yLines:
        line = Line2D([plt.xlim()[0], plt.xlim()[1]], [y, y], color="grey", linestyle="--")
        ax.add_line(line)
    #print(plt.xlim())
    #print(plt.ylim())


class Path:
    def __init__(self, ID):
        self.pathID = ID
        self.segments = []
        self.numberOfSegments = 0
        self.stageBorders = []

    def append(self, segment):
        self.segments.append(segment)
        self.numberOfSegments += 1

    def display(self, locator = 1):
        fig, ax = plt.subplots()
        ax.set_aspect('equal', 'box') 
        ax.grid(True)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(locator))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(locator))

        for segment in self.segments:
            segment.draw(ax)
        displayPoints(ax, self.stageBorders)

        ax.autoscale_view()
        displayTesselationLines(ax, plt, locator)
        plt.show()

    def calculateStageBorders(self, d):
        for segment in self.segments:
            self.stageBorders += segment.calculateStageBorders(d)

    
