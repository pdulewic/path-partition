#!/usr/bin/env python

import sys
import os

from path_partition.segments.line_segment import LineSegment
from path_partition.vector import Point, length_squared
from path_partition.config import NUM_ERR 


def test_right_tilted_segment_rect():
    segment = LineSegment({"pA": [-5, -2], "pB": [-1, 4]})
    frameRect = segment.get_frame_rect()
    assert frameRect[0] == Point(-5, -2)
    assert frameRect[1] == Point(-1, 4)


def test_left_tilted_segment_rect():
    segment = LineSegment({"pA": [-5, 4], "pB": [-1, -2]})
    frameRect = segment.get_frame_rect()
    assert frameRect[0] == Point(-5, -2)
    assert frameRect[1] == Point(-1, 4)


def test_segment_parallel_to_OY_rect():
    segment = LineSegment({"pA": [12, -61], "pB": [12, -3]})
    frameRect = segment.get_frame_rect()
    assert frameRect[0] == Point(12, -61)
    assert frameRect[1] == Point(12, -3)


def test_segment_parallel_to_OX_rect():
    segment = LineSegment({"pA": [14, -17], "pB": [92, -17]})
    frameRect = segment.get_frame_rect()
    assert frameRect[0] == Point(14, -17)
    assert frameRect[1] == Point(92, -17)


def test_intersection_with_parallel_to_OY():
    segment = LineSegment({"pA": [0, 1], "pB": [2, 3]})
    intersection = segment.intersection_with_line((1, 0, -1))
    assert 1 == len(intersection)
    assert intersection[0] == Point(1, 2)


def test_intersection_with_parallel_to_OX():
    segment = LineSegment({"pA": [3, -7], "pB": [5, -4]})
    intersection = segment.intersection_with_line((0, 1, 5))
    assert 1 == len(intersection)
    assert length_squared(intersection[0] - Point(4.33, -5)) < NUM_ERR


def test_intersection_with_OY():
    segment = LineSegment({"pA": [6.64, 2.3], "pB": [-5.86, -3.6]})
    intersection = segment.intersection_with_line((1, 0, 0))
    assert 1 == len(intersection)
    assert length_squared(intersection[0] - Point(0, -0.83)) < NUM_ERR


def test_intersection_on_segment_edge():
    segment = LineSegment({"pA": [0.5, 1], "pB": [1.9, 1.78]})
    intersection = segment.intersection_with_line((1, 0, -0.5))
    assert 1 == len(intersection)
    assert intersection[0] == Point(0.5, 1)


def test_no_intersection():
    segment = LineSegment({"pA": [1.73, 5.3], "pB": [1.98, 4.77]})
    assert not segment.intersection_with_line((0, 1, -4.5))


def test_X_line_overlaping_segment():
    segment = LineSegment({"pA": [0.5, 1], "pB": [0.5, 2]})
    assert not segment.intersection_with_line((1, 0, -0.5))


def test_Y_line_overlaping_segment():
    segment = LineSegment({"pA": [-13.72, 3.76], "pB": [26.09, 3.76]})
    assert not segment.intersection_with_line((0, 1, -3.76))


def test_order_points_already_ordered():
    segment = LineSegment({"pA": [0.5, 1], "pB": [1.9, 1.78]})
    points = [Point(0.77, 1.15), Point(0.88, 1.21), Point(1.7, 1.67)]
    assert points == segment.order_points(points)


def test_order_unordered_points():
    segment = LineSegment({"pA": [0.5, 1], "pB": [1.9, 1.78]})
    points = [Point(0.88, 1.21), Point(0.77, 1.15), Point(1.7, 1.67)]
    ordered = [Point(0.77, 1.15), Point(0.88, 1.21), Point(1.7, 1.67)]
    assert ordered == segment.order_points(points)


def test_order_points_in_reverse_order():
    segment = LineSegment({"pA": [1.9, 1.78], "pB": [0.5, 1]})
    points = [Point(0.88, 1.21), Point(0.77, 1.15), Point(1.7, 1.67)]
    ordered = [Point(1.7, 1.67), Point(0.88, 1.21), Point(0.77, 1.15)]
    assert ordered == segment.order_points(points)


def test_order_points_on_vertical_segment():
    segment = LineSegment({"pA": [-0.77, 3.89], "pB": [-0.77, 1.6]})
    points = [Point(-0.77, 2.93), Point(-0.77, 1.82), Point(-0.77, 3.7)]
    ordered = [Point(-0.77, 3.7), Point(-0.77, 2.93), Point(-0.77, 1.82)]
    assert ordered == segment.order_points(points)


def test_order_empty_point_list():
    segment = LineSegment({"pA": [-0.77, 3.89], "pB": [-0.77, 1.6]})
    assert [] == segment.order_points([])


def test_simple_line_stage_borders():
    segment = LineSegment({"pA": [1.09, 0.92], "pB": [3.64, 1.13]})
    points = [Point(1.3, 0.93), Point(2.7, 1.05), Point(3.3, 1.1)]
    result = segment.calculate_stage_borders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert length_squared(points[i] - result[i]) < NUM_ERR


def test_simple_line_stage_borders2():
    segment = LineSegment({"pA": [5.62, 3.37], "pB": [4.48, 0.37]})
    points = [
        Point(5.59, 3.3),
        Point(5.37, 2.7),
        Point(5.3, 2.52),
        Point(4.84, 1.3),
        Point(4.7, 0.94),
        Point(4.61, 0.7),
    ]
    result = segment.calculate_stage_borders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert length_squared(points[i] - result[i]) < NUM_ERR


def test_negative_line_stage_borders():
    segment = LineSegment({"pA": [1, -2], "pB": [2.98, 0.61]})
    points = [
        Point(1.3, -1.61),
        Point(1.53, -1.3),
        Point(1.99, -0.7),
        Point(2.7, 0.24),
    ]
    result = segment.calculate_stage_borders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert length_squared(points[i] - result[i]) < NUM_ERR


def test_duplicate_line_stage_borders():
    segment = LineSegment({"pA": [3.4, 3.4], "pB": [2.6, 2.6]})
    points = [Point(3.3, 3.3), Point(2.7, 2.7)]
    assert points == segment.calculate_stage_borders(2)


def test_advanced_line_stage_borders():
    segment = LineSegment({"pA": [4.3, -1.08], "pB": [-0.82, 1.89]})
    points = [
        Point(3.65, -0.7),
        Point(3.3, -0.5),
        Point(2.7, -0.15),
        Point(1.3, 0.67),
        Point(1.24, 0.7),
        Point(0.7, 1.01),
        Point(0.21, 1.3),
        Point(-0.7, 1.83),
    ]
    result = segment.calculate_stage_borders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert length_squared(points[i] - result[i]) < NUM_ERR


def test_line_with_no_stage_borders():
    segment = LineSegment({"pA": [1.35, -0.64], "pB": [2.65, 0.45]})
    assert not segment.calculate_stage_borders(2)


def test_line_stage_borders_with_different_tesselation():
    segment = LineSegment({"pA": [9, 4], "pB": [4.63, 6.84]})
    points = [
        Point(8.3, 4.46),
        Point(7, 5.3),
        Point(6.7, 5.5),
        Point(5.3, 6.41),
        Point(4.85, 6.7),
    ]
    result = segment.calculate_stage_borders(3)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert length_squared(points[i] - result[i]) < NUM_ERR
