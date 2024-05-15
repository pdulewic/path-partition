#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
from path_partition.utils import tesselation_lines_between

def display_points(ax, points):
    x_axes = []
    y_axes = []
    for point in points:
        x_axes.append(point.x)
        y_axes.append(point.y)
    ax.plot(x_axes, y_axes, 'ro')

def display_tesselation_lines(ax, plt, d):
    xLines = tesselation_lines_between(plt.xlim()[0], plt.xlim()[1], d)
    for x in xLines:
        line = Line2D([x, x], [plt.ylim()[0], plt.ylim()[1]], color="grey", linestyle="--")
        ax.add_line(line)

    yLines = tesselation_lines_between(plt.ylim()[0], plt.ylim()[1], d)
    for y in yLines:
        line = Line2D([plt.xlim()[0], plt.xlim()[1]], [y, y], color="grey", linestyle="--")
        ax.add_line(line)
    #print(plt.xlim())
    #print(plt.ylim())


class Path:
    def __init__(self, path_id: str) -> None:
        self.path_id = path_id
        self.segments = []
        self.number_of_segments = 0
        self.stage_borders = []

    def append(self, segment):
        self.segments.append(segment)
        self.number_of_segments += 1

    def display(self, locator = 1):
        fig, ax = plt.subplots()
        ax.set_aspect('equal', 'box') 
        ax.grid(True)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(locator))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(locator))

        for segment in self.segments:
            segment.draw(ax)
        display_points(ax, self.stage_borders)

        ax.autoscale_view()
        display_tesselation_lines(ax, plt, locator)
        plt.show()

    def calculate_stage_borders(self, d):
        for segment in self.segments:
            self.stage_borders += segment.calculate_stage_borders(d)

    
