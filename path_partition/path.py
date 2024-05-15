#!/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
from path_partition.utils import tesselation_lines_between
from path_partition.vector import Point
from path_partition.segments.segment import Segment


def display_points(ax, points: list[Point]) -> None:
    x_axes = []
    y_axes = []
    for point in points:
        x_axes.append(point.x)
        y_axes.append(point.y)
    ax.plot(x_axes, y_axes, "ro")


def display_tesselation_lines(ax, plt, tesselation_parameter: float) -> None:
    x_lines = tesselation_lines_between(
        plt.xlim()[0], plt.xlim()[1], tesselation_parameter
    )
    for x in x_lines:
        line = Line2D(
            [x, x], [plt.ylim()[0], plt.ylim()[1]], color="grey", linestyle="--"
        )
        ax.add_line(line)

    y_lines = tesselation_lines_between(
        plt.ylim()[0], plt.ylim()[1], tesselation_parameter
    )
    for y in y_lines:
        line = Line2D(
            [plt.xlim()[0], plt.xlim()[1]], [y, y], color="grey", linestyle="--"
        )
        ax.add_line(line)


class Path:
    def __init__(self, path_id: str) -> None:
        self.path_id = path_id
        self.segments = []
        self.number_of_segments = 0
        self.stage_borders = []

    def append(self, segment: Segment) -> None:
        self.segments.append(segment)
        self.number_of_segments += 1

    def display(self, locator=1) -> None:
        fig, ax = plt.subplots()
        ax.set_aspect("equal", "box")
        ax.grid(True)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(locator))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(locator))

        for segment in self.segments:
            segment.draw(ax)
        display_points(ax, self.stage_borders)

        ax.autoscale_view()
        display_tesselation_lines(ax, plt, locator)
        plt.show()

    def calculate_stage_borders(self, tesselation_parameter: float) -> None:
        for segment in self.segments:
            self.stage_borders += segment.calculate_stage_borders(tesselation_parameter)
