#!/usr/bin/env python

from path_partition.segments.segment import Segment
from path_partition.vector import Point, angle
from path_partition.config import PATH_COLOR
from path_partition.utils import check_line_parallelism, remove_duplicates_preserving_order
from matplotlib.patches import Arc
from math import sin, cos, radians, degrees, sqrt


def is_angle_within_range(start_angle, end_angle, point_angle):
    if not (0 <= start_angle <= 360 and 0 <= end_angle <= 360 and 0 <= point_angle <= 360):
        raise ValueError("Angle outside range (0,360)")
    if start_angle <= end_angle:
        return point_angle >= start_angle and point_angle <= end_angle
    return point_angle >= start_angle or point_angle <= end_angle


def is_point_inside_circle_arc(point, circle):
    point_angle = degrees(angle(point - circle.center))
    return is_angle_within_range(circle.theta1, circle.theta2, point_angle)


class CircleArc(Segment):
    def __init__(self, data):
        self.center = Point(data["center"][0], data["center"][1])
        self.radius = data["radius"]
        self.theta1 = data["theta1"]
        self.theta2 = data["theta2"]
        self.starts_from_A = data["starts_from_A"]

    def draw(self, ax):
        arc = Arc(
            (self.center.x, self.center.y),
            self.radius * 2,
            self.radius * 2,
            angle=0,
            theta1=self.theta1,
            theta2=self.theta2,
            color=PATH_COLOR,
        )
        ax.add_patch(arc)

    def get_frame_rect(self):
        x_coordinates = [
            self.center[0] + self.radius * cos(radians(self.theta1)),
            self.center[0] + self.radius * cos(radians(self.theta2)),
        ]
        y_coordinates = [
            self.center[1] + self.radius * sin(radians(self.theta1)),
            self.center[1] + self.radius * sin(radians(self.theta2)),
        ]

        for angle in range(0, 360, 90):
            if is_angle_within_range(self.theta1, self.theta2, angle):
                x_coordinates.append(
                    self.center[0] + self.radius * round(cos(radians(angle)))
                )
                y_coordinates.append(
                    self.center[1] + self.radius * round(sin(radians(angle)))
                )

        bottom_left_point = Point(min(x_coordinates), min(y_coordinates))
        top_right_point = Point(max(x_coordinates), max(y_coordinates))
        return (bottom_left_point, top_right_point)

    def intersection_with_line(self, line):
        known, unknown = check_line_parallelism(line)

        known_value = -line[2] / line[known]
        if (
            known_value < self.center[known] - self.radius
            or known_value > self.center[known] + self.radius
        ):
            return []
        tmp = self.radius**2 - (known_value - self.center[known]) ** 2
        if tmp < 0:
            return []
        unknown_value1 = self.center[unknown] + sqrt(tmp)
        unknown_value2 = self.center[unknown] - sqrt(tmp)
        if known:
            result = [
                Point(unknown_value1, known_value),
                Point(unknown_value2, known_value),
            ]
        else:
            result = [
                Point(known_value, unknown_value1),
                Point(known_value, unknown_value2),
            ]
        result = remove_duplicates_preserving_order(result)
        # remove points outside arc
        return [p for p in result if is_point_inside_circle_arc(p, self)]

    def order_points(self, points):
        points.sort(
            key=lambda p: angle(p - self.center), reverse=not self.starts_from_A
        )
        if self.theta1 > self.theta2 and points:
            if self.starts_from_A:
                if degrees(angle(points[0] - self.center)) < self.theta1:
                    while degrees(angle(points[-1] - self.center)) >= self.theta1:
                        points.insert(0, points.pop())
            else:
                if degrees(angle(points[0] - self.center)) > self.theta2:
                    while degrees(angle(points[-1] - self.center)) <= self.theta2:
                        points.insert(0, points.pop())
        return points
