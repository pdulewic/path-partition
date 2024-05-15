#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
from path_partition.utils import (
    tesselation_lines_between,
    remove_duplicates_preserving_order,
)
from typing import Tuple
from path_partition.vector import Point


class Segment:
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self, ax) -> None:
        """draw segment on 'ax' using matplotlib functions"""
        raise NotImplementedError

    @abstractmethod
    def get_frame_rect(self) -> Tuple[Point, Point]:
        """returns bottom left and top right points defining a rectangle that fully
        covers the segment"""
        raise NotImplementedError

    @abstractmethod
    def intersection_with_line(self, line) -> list[Point]:
        """returns points of intersection of segment and line Ax + By + C = 0
        represented as list line == [A, B, C]. Works only for lines parallel to
        OX or OY!"""
        raise NotImplementedError

    @abstractmethod
    def order_points(self, points: list[Point]) -> list[Point]:
        """sorts points according to their distance from the beginning of the sector"""
        raise NotImplementedError

    def calculate_stage_borders(self, tesselation_parameter: float) -> list[Point]:
        points = []
        frame_rect = self.get_frame_rect()
        for i in [0, 1]:
            tesselation_lines = tesselation_lines_between(
                frame_rect[0][i], frame_rect[1][i], tesselation_parameter
            )
            for line_coordinate in tesselation_lines:
                # list [A, B, C] representing line Ax + By + C = 0
                line = [0, 0, -line_coordinate]
                line[i] = 1
                points += self.intersection_with_line(line)
        points = remove_duplicates_preserving_order(points)
        return self.order_points(points)
