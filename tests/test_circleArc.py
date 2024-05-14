#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.abspath("../src"))

import segments.circle_arc as circleArc
import vector as vec
import config
import pytest
import math


# ---------- is_angle_within_range() ------------


def test_angle_within_range():
    assert True == circleArc.is_angle_within_range(57.6, 180.2, 170.3)
    assert True == circleArc.is_angle_within_range(253.1, 18.7, 2.6)
    assert True == circleArc.is_angle_within_range(19.5, 127.3, 127.3)
    assert False == circleArc.is_angle_within_range(18.7, 183.3, 227.9)
    assert False == circleArc.is_angle_within_range(194.2, 145.8, 184.6)
    assert False == circleArc.is_angle_within_range(164.8, 164.8, 12.5)


def test_angle_outside_range_0_360():
    with pytest.raises(ValueError):
        circleArc.is_angle_within_range(-3.5, 340.1, 8.8)
    with pytest.raises(ValueError):
        circleArc.is_angle_within_range(71.8, 721.8, 328.8)
    with pytest.raises(ValueError):
        circleArc.is_angle_within_range(71.8, 721.8, 328.8)


# ---------- is_point_inside_circle_arc() ------------


def test_point_inside_circle_arc():
    arc1 = circleArc.CircleArc(
        {
            "center": [-7.25, 2.99],
            "radius": 3.17,
            "theta1": 315.48,
            "theta2": 189.13,
            "starts_from_A": True,
        }
    )
    assert circleArc.is_point_inside_circle_arc(vec.Point(-10.39, 2.62), arc1)

    arc2 = circleArc.CircleArc(
        {
            "center": [3, -4],
            "radius": 1.5,
            "theta1": 52.22,
            "theta2": 308.53,
            "starts_from_A": True,
        }
    )
    assert circleArc.is_point_inside_circle_arc(vec.Point(-3.79, -2.73), arc2)

    arc3 = circleArc.CircleArc(
        {
            "center": [10, -4],
            "radius": 1,
            "theta1": 0,
            "theta2": 180,
            "starts_from_A": True,
        }
    )
    assert circleArc.is_point_inside_circle_arc(vec.Point(11, -4), arc3)


def test_point_outside_circle_arc():
    arc1 = circleArc.CircleArc(
        {
            "center": [-7.25, 2.99],
            "radius": 3.17,
            "theta1": 315.48,
            "theta2": 189.13,
            "starts_from_A": False,
        }
    )
    assert not circleArc.is_point_inside_circle_arc(vec.Point(-10.34, 2.31), arc1)

    arc2 = circleArc.CircleArc(
        {
            "center": [3, -4],
            "radius": 1.5,
            "theta1": 52.22,
            "theta2": 308.53,
            "starts_from_A": True,
        }
    )
    assert not circleArc.is_point_inside_circle_arc(vec.Point(4.06, -2.94), arc2)

    arc3 = circleArc.CircleArc(
        {
            "center": [10, -4],
            "radius": 1,
            "theta1": 0,
            "theta2": 180,
            "starts_from_A": False,
        }
    )
    assert not circleArc.is_point_inside_circle_arc(vec.Point(9.05, -4.31), arc3)


# ---------- get_frame_rect() -------------


def test_full_circle_rect():
    arc = circleArc.CircleArc(
        {
            "center": [-3, 7],
            "radius": 1.5,
            "theta1": 0,
            "theta2": 360,
            "starts_from_A": True,
        }
    )
    frameRect = arc.get_frame_rect()
    assert frameRect[0] == vec.Point(-4.5, 5.5)
    assert frameRect[1] == vec.Point(-1.5, 8.5)


def test_half_circle_rect():
    arc = circleArc.CircleArc(
        {
            "center": [-3, 7],
            "radius": 1.5,
            "theta1": 0,
            "theta2": 180,
            "starts_from_A": False,
        }
    )
    frameRect = arc.get_frame_rect()
    assert frameRect[0] == vec.Point(-4.5, 7)
    assert frameRect[1] == vec.Point(-1.5, 8.5)


def test_medium_arc_rect():
    arc = circleArc.CircleArc(
        {
            "center": [5, 2],
            "radius": 2.5,
            "theta1": 37.48,
            "theta2": 204.28,
            "starts_from_A": True,
        }
    )
    frameRect = arc.get_frame_rect()
    assert vec.length_squared(frameRect[0] - vec.Point(2.5, 0.97)) < config.NUM_ERR
    assert vec.length_squared(frameRect[1] - vec.Point(6.98, 4.5)) < config.NUM_ERR


def test_small_arc_crossing_zero_angle_rect():
    arc = circleArc.CircleArc(
        {
            "center": [5, 2],
            "radius": 2.5,
            "theta1": 334.62,
            "theta2": 24.23,
            "starts_from_A": True,
        }
    )
    frameRect = arc.get_frame_rect()
    assert vec.length_squared(frameRect[0] - vec.Point(7.26, 0.93)) < config.NUM_ERR
    assert vec.length_squared(frameRect[1] - vec.Point(7.5, 3.02)) < config.NUM_ERR


def test_tiny_arc_rect():
    arc = circleArc.CircleArc(
        {
            "center": [5, 2],
            "radius": 2.5,
            "theta1": 220.28,
            "theta2": 236.76,
            "starts_from_A": False,
        }
    )
    frameRect = arc.get_frame_rect()
    assert vec.length_squared(frameRect[0] - vec.Point(3.09, -0.09)) < config.NUM_ERR
    assert vec.length_squared(frameRect[1] - vec.Point(3.63, 0.39)) < config.NUM_ERR


def test_degenerated_arc_rect():
    arc = circleArc.CircleArc(
        {
            "center": [3, 4],
            "radius": 1.65,
            "theta1": 313.33,
            "theta2": 313.33,
            "starts_from_A": False,
        }
    )
    frameRect = arc.get_frame_rect()
    assert vec.length_squared(frameRect[0] - vec.Point(4.13, 2.8)) < config.NUM_ERR
    assert vec.length_squared(frameRect[1] - vec.Point(4.13, 2.8)) < config.NUM_ERR


# ------- intersection_with_line() ----------


def test_full_circle_intersection():
    arc = circleArc.CircleArc(
        {
            "center": [5, 2],
            "radius": 2.5,
            "theta1": 0,
            "theta2": 360,
            "starts_from_A": False,
        }
    )
    intersection = arc.intersection_with_line((1, 0, -3))
    assert 2 == len(intersection)
    assert intersection[0] == vec.Point(3, 3.5)
    assert intersection[1] == vec.Point(3, 0.5)


def test_arc_intersection_with_OY():
    arc = circleArc.CircleArc(
        {
            "center": [-5.5, 2.55],
            "radius": 6.12,
            "theta1": 241.58,
            "theta2": 63.72,
            "starts_from_A": False,
        }
    )
    intersection = arc.intersection_with_line((1, 0, 0))
    assert 2 == len(intersection)
    assert vec.length_squared(intersection[0] - vec.Point(0, 5.23)) < config.NUM_ERR
    assert vec.length_squared(intersection[1] - vec.Point(0, -0.13)) < config.NUM_ERR


def test_intersection_with_circle_but_not_with_arc():
    arc = circleArc.CircleArc(
        {
            "center": [3, -4],
            "radius": 1.5,
            "theta1": 52.22,
            "theta2": 308.53,
            "starts_from_A": True,
        }
    )
    assert not arc.intersection_with_line((1, 0, -4))


def test_only_one_intersection_point():
    arc = circleArc.CircleArc(
        {
            "center": [-7.25, 2.99],
            "radius": 3.17,
            "theta1": 315.48,
            "theta2": 189.13,
            "starts_from_A": False,
        }
    )
    intersection = arc.intersection_with_line((0, 1, -2))
    assert 1 == len(intersection)
    assert vec.length_squared(intersection[0] - vec.Point(-4.23, 2)) < config.NUM_ERR


def test_intersection_on_arc_edges():
    arc = circleArc.CircleArc(
        {
            "center": [10, -4],
            "radius": 1,
            "theta1": 0,
            "theta2": 180,
            "starts_from_A": True,
        }
    )
    intersection = arc.intersection_with_line((0, 1, 4))
    assert 2 == len(intersection)
    assert intersection[0] == vec.Point(11, -4)
    assert intersection[1] == vec.Point(9, -4)


def test_degenerated_arc_intersection():
    arc = circleArc.CircleArc(
        {
            "center": [5, 2],
            "radius": 2.5,
            "theta1": 31.67,
            "theta2": 31.67,
            "starts_from_A": True,
        }
    )
    assert not arc.intersection_with_line((1, 0, -3))


# ------------- order_points() ---------------


def test_order_points_already_ordered():
    arc = circleArc.CircleArc(
        {
            "center": [-3, 5],
            "radius": 2,
            "theta1": 346.75,
            "theta2": 327.1,
            "starts_from_A": True,
        }
    )
    points = [
        vec.Point(-1.01, 4.77),
        vec.Point(-1.58, 6.41),
        vec.Point(-4.22, 3.41),
        vec.Point(-1.46, 3.73),
    ]
    assert points == arc.order_points(points)


def test_order_not_ordered_points():
    arc = circleArc.CircleArc(
        {
            "center": [-3, 5],
            "radius": 2,
            "theta1": 346.75,
            "theta2": 327.1,
            "starts_from_A": True,
        }
    )
    points = [
        vec.Point(-1.58, 6.41),
        vec.Point(-1.01, 4.77),
        vec.Point(-1.46, 3.73),
        vec.Point(-4.22, 3.41),
    ]
    ordered = [
        vec.Point(-1.01, 4.77),
        vec.Point(-1.58, 6.41),
        vec.Point(-4.22, 3.41),
        vec.Point(-1.46, 3.73),
    ]
    assert ordered == arc.order_points(points)


def test_order_reversed_points():
    arc = circleArc.CircleArc(
        {
            "center": [-3, 5],
            "radius": 2,
            "theta1": 346.75,
            "theta2": 327.1,
            "starts_from_A": False,
        }
    )
    points = [
        vec.Point(-1.58, 6.41),
        vec.Point(-1.01, 4.77),
        vec.Point(-1.46, 3.73),
        vec.Point(-4.22, 3.41),
    ]
    ordered = [
        vec.Point(-1.46, 3.73),
        vec.Point(-4.22, 3.41),
        vec.Point(-1.58, 6.41),
        vec.Point(-1.01, 4.77),
    ]
    assert ordered == arc.order_points(points)


def test_order_empty_point_list():
    arc = circleArc.CircleArc(
        {
            "center": [-3, 5],
            "radius": 2,
            "theta1": 346.75,
            "theta2": 327.1,
            "starts_from_A": False,
        }
    )
    assert [] == arc.order_points([])


# ----------- calculate_stage_borders() ------------


def test_simple_arc_stage_borders():
    arc = circleArc.CircleArc(
        {
            "center": [3.71, -0.97],
            "radius": 3.1,
            "theta1": 341.41,
            "theta2": 19.67,
            "starts_from_A": False,
        }
    )
    points = [
        vec.Point(6.7, -0.16),
        vec.Point(6.8, -0.7),
        vec.Point(6.79, -1.3),
        vec.Point(6.7, -1.78),
    ]
    result = arc.calculate_stage_borders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert vec.length_squared(points[i] - result[i]) < config.NUM_ERR


def test_stage_borders_for_full_circle():
    arc = circleArc.CircleArc(
        {
            "center": [1.13, 2.01],
            "radius": 0.87,
            "theta1": 0,
            "theta2": 360,
            "starts_from_A": True,
        }
    )
    points = [
        vec.Point(1.66, 2.7),
        vec.Point(1.3, 2.86),
        vec.Point(0.7, 2.77),
        vec.Point(0.6, 2.7),
        vec.Point(0.63, 1.3),
        vec.Point(0.7, 1.26),
        vec.Point(1.3, 1.16),
        vec.Point(1.63, 1.3),
    ]
    result = arc.calculate_stage_borders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert vec.length_squared(points[i] - result[i]) < config.NUM_ERR


def test_arc_with_no_stage_borders():
    arc = circleArc.CircleArc(
        {
            "center": [3.71, -0.97],
            "radius": 3.1,
            "theta1": 72.44,
            "theta2": 96.47,
            "starts_from_A": False,
        }
    )
    assert not arc.calculate_stage_borders(2)


def test_stage_borders_on_arc_edges():
    arc = circleArc.CircleArc(
        {
            "center": [1.13, 2.01],
            "radius": 0.87,
            "theta1": 52.23,
            "theta2": 119.76,
            "starts_from_A": False,
        }
    )
    points = [vec.Point(0.7, 2.77), vec.Point(1.3, 2.86), vec.Point(1.66, 2.7)]
    result = arc.calculate_stage_borders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert vec.length_squared(points[i] - result[i]) < config.NUM_ERR


def test_duplicate_arc_stage_borders():
    arc = circleArc.CircleArc(
        {
            "center": [2, 0.7],
            "radius": 0.7,
            "theta1": 0,
            "theta2": 180,
            "starts_from_A": True,
        }
    )
    points = [
        vec.Point(2.7, 0.7),
        vec.Point(2.36, 1.3),
        vec.Point(1.63, 1.3),
        vec.Point(1.3, 0.7),
    ]
    result = arc.calculate_stage_borders(2)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert vec.length_squared(points[i] - result[i]) < config.NUM_ERR


def test_arc_stage_borders_with_different_tesselation():
    arc = circleArc.CircleArc(
        {
            "center": [3.24, 4.57],
            "radius": 1.55,
            "theta1": 0,
            "theta2": 180,
            "starts_from_A": True,
        }
    )
    points = [
        vec.Point(4.61, 5.3),
        vec.Point(3.7, 6.05),
        vec.Point(2.3, 5.8),
        vec.Point(1.88, 5.3),
    ]
    result = arc.calculate_stage_borders(3)
    assert len(points) == len(result)
    for i in range(len(result)):
        assert vec.length_squared(points[i] - result[i]) < config.NUM_ERR
