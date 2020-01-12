#!/usr/bin/env python

import lineSegment 
import vector as vec
import config 

# ---------- getFrameRect() -------------


def test_right_tilted_segment_rect():
    segment = lineSegment.LineSegment({
        "pA": [-5, -2],
        "pB": [-1, 4]
    })
    frameRect = segment.getFrameRect()
    assert frameRect[0] == vec.Point(-5, -2)
    assert frameRect[1] == vec.Point(-1, 4)


def test_left_tilted_segment_rect():
    segment = lineSegment.LineSegment({
        "pA": [-5, 4],
        "pB": [-1, -2]
    })
    frameRect = segment.getFrameRect()
    assert frameRect[0] == vec.Point(-5, -2)
    assert frameRect[1] == vec.Point(-1, 4)


def test_segment_parallel_to_OY_rect():
    segment = lineSegment.LineSegment({
        "pA": [12, -61],
        "pB": [12, -3]
    })
    frameRect = segment.getFrameRect()
    assert frameRect[0] == vec.Point(12, -61)
    assert frameRect[1] == vec.Point(12, -3)


def test_segment_parallel_to_OX_rect():
    segment = lineSegment.LineSegment({
        "pA": [14, -17],
        "pB": [92, -17]
    })
    frameRect = segment.getFrameRect()
    assert frameRect[0] == vec.Point(14, -17)
    assert frameRect[1] == vec.Point(92, -17)


# ------- intersectionWithLine() ----------

def test_intersection_with_parallel_to_OY():
    segment = lineSegment.LineSegment({
        "pA": [0, 1],
        "pB": [2, 3]
    })
    intersection = segment.intersectionWithLine((1, 0, -1))
    assert 1 == len(intersection)
    assert intersection[0] == vec.Point(1, 2)


def test_intersection_with_parallel_to_OX():
    segment = lineSegment.LineSegment({
        "pA": [3, -7],
        "pB": [5, -4]
    })
    intersection = segment.intersectionWithLine((0, 1, 5))
    assert 1 == len(intersection)
    assert vec.lengthSqrd(
        intersection[0] - vec.Point(4.33, -5)) < config.NUM_ERR


def test_intersection_with_OY():
    segment = lineSegment.LineSegment({
        "pA": [6.64, 2.3],
        "pB": [-5.86, -3.6]
    })
    intersection = segment.intersectionWithLine((1, 0, 0))
    assert 1 == len(intersection)
    assert vec.lengthSqrd(
        intersection[0] - vec.Point(0, -0.83)) < config.NUM_ERR


def test_intersection_on_segment_edge():
    segment = lineSegment.LineSegment({
        "pA": [0.5, 1],
        "pB": [1.9, 1.78]
    })
    intersection = segment.intersectionWithLine((1, 0, -0.5))
    assert 1 == len(intersection)
    assert intersection[0] == vec.Point(0.5, 1)


def test_no_intersection():
    segment = lineSegment.LineSegment({
        "pA": [1.73, 5.3],
        "pB": [1.98, 4.77]
    })
    assert not segment.intersectionWithLine((0, 1, -4.5))


def test_X_line_overlaping_segment():
    segment = lineSegment.LineSegment({
        "pA": [0.5, 1],
        "pB": [0.5, 2]
    })
    assert not segment.intersectionWithLine((1, 0, -0.5))


def test_Y_line_overlaping_segment():
    segment = lineSegment.LineSegment({
        "pA": [-13.72, 3.76],
        "pB": [26.09, 3.76]
    })
    assert not segment.intersectionWithLine((0, 1, -3.76))


# -------------- orderPoints() ---------------

def test_order_points_already_ordered():
    segment = lineSegment.LineSegment({
        "pA": [0.5, 1],
        "pB": [1.9, 1.78]
    })
    points = [vec.Point(0.77, 1.15), vec.Point(0.88, 1.21), vec.Point(1.7, 1.67)]
    assert points == segment.orderPoints(points)


def test_order_unordered_points():
    segment = lineSegment.LineSegment({
        "pA": [0.5, 1],
        "pB": [1.9, 1.78]
    })
    points = [vec.Point(0.88, 1.21), vec.Point(0.77, 1.15), vec.Point(1.7, 1.67)]
    ordered = [vec.Point(0.77, 1.15), vec.Point(0.88, 1.21), vec.Point(1.7, 1.67)]
    assert ordered == segment.orderPoints(points)


def test_order_points_in_reverse_order():
    segment = lineSegment.LineSegment({
        "pA": [1.9, 1.78],
        "pB": [0.5, 1]
    })
    points = [vec.Point(0.88, 1.21), vec.Point(
        0.77, 1.15), vec.Point(1.7, 1.67)]
    ordered = [vec.Point(1.7, 1.67), vec.Point(
        0.88, 1.21), vec.Point(0.77, 1.15)]
    assert ordered == segment.orderPoints(points)


def test_order_points_on_vertical_segment():
    segment = lineSegment.LineSegment({
        "pA": [-0.77, 3.89],
        "pB": [-0.77, 1.6]
    })
    points = [vec.Point(-0.77, 2.93), vec.Point(-0.77, 1.82), vec.Point(-0.77, 3.7)]
    ordered = [vec.Point(-0.77, 3.7), vec.Point(-0.77, 2.93), vec.Point(-0.77, 1.82)]
    assert ordered == segment.orderPoints(points)


def test_order_empty_point_list():
    segment = lineSegment.LineSegment({
        "pA": [-0.77, 3.89],
        "pB": [-0.77, 1.6]
    })
    assert [] == segment.orderPoints([])

# ----------- calculateStageBorders() ------------


def test_simple_line_stage_borders():
    segment = lineSegment.LineSegment({
        "pA": [1.09, 0.92],
        "pB": [3.64, 1.13]
    })
    points = [vec.Point(1.3, 0.93), vec.Point(2.7, 1.05), vec.Point(3.3, 1.1)]
    result = segment.calculateStageBorders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert vec.lengthSqrd(points[i] - result[i]) < config.NUM_ERR


def test_simple_line_stage_borders2():
    segment = lineSegment.LineSegment({
        "pA": [5.62, 3.37],
        "pB": [4.48, 0.37]
    })
    points = [vec.Point(5.59, 3.3), vec.Point(5.37, 2.7), vec.Point(5.3, 2.52),
              vec.Point(4.84, 1.3), vec.Point(4.7, 0.94), vec.Point(4.61, 0.7)]
    result = segment.calculateStageBorders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert vec.lengthSqrd(points[i] - result[i]) < config.NUM_ERR


def test_negative_line_stage_borders():
    segment = lineSegment.LineSegment({
        "pA": [1, -2],
        "pB": [2.98, 0.61]
    })
    points = [vec.Point(1.3, -1.61), vec.Point(1.53, -1.3),
              vec.Point(1.99, -0.7), vec.Point(2.7, 0.24)]
    result = segment.calculateStageBorders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert vec.lengthSqrd(points[i] - result[i]) < config.NUM_ERR


def test_duplicate_line_stage_borders():
    segment = lineSegment.LineSegment({
        "pA": [3.4, 3.4],
        "pB": [2.6, 2.6]
    })
    points = [vec.Point(3.3, 3.3), vec.Point(2.7, 2.7)]
    assert points == segment.calculateStageBorders(2)


def test_advanced_line_stage_borders():
    segment = lineSegment.LineSegment({
        "pA": [4.3, -1.08],
        "pB": [-0.82, 1.89]
    })
    points = [vec.Point(3.65, -0.7), vec.Point(3.3, -0.5), vec.Point(2.7, -0.15), vec.Point(1.3, 0.67),
              vec.Point(1.24, 0.7), vec.Point(0.7, 1.01), vec.Point(0.21, 1.3), vec.Point(-0.7, 1.83)]
    result = segment.calculateStageBorders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert vec.lengthSqrd(points[i] - result[i]) < config.NUM_ERR


def test_line_with_no_stage_borders():
    segment = lineSegment.LineSegment({
        "pA": [1.35, -0.64],
        "pB": [2.65, 0.45]
    })
    assert not segment.calculateStageBorders(2)


def test_line_stage_borders_with_different_tesselation():
    segment = lineSegment.LineSegment({
        "pA": [9, 4],
        "pB": [4.63, 6.84]
    })
    points = [vec.Point(8.3, 4.46), vec.Point(7, 5.3), vec.Point(6.7, 5.5),
              vec.Point(5.3, 6.41), vec.Point(4.85, 6.7)]
    result = segment.calculateStageBorders(3)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert vec.lengthSqrd(points[i] - result[i]) < config.NUM_ERR
