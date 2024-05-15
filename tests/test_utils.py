#!/usr/bin/env python

import sys
import os

import pytest
from path_partition.config import ROBOT_RADIUS
from path_partition.utils import tesselation_lines_between, remove_duplicates_preserving_order
from path_partition.vector import Point

if ROBOT_RADIUS != 0.7:
    pytest.skip(
        "Tests for tesselation_lines_between() are only valid for robot radius equal to 0.7",
        allow_module_level=True,
    )


def test_tesselation_lines_between():
    assert [4.7, 7.3] == tesselation_lines_between(4.2, 7.6, 4)
    assert [
        -12.7,
        -11.3,
        -9.7,
        -8.3,
        -6.7,
        -5.3,
        -3.7,
        -2.3,
        -0.7,
        0.7,
        2.3,
        3.7,
        5.3,
        6.7,
    ] == tesselation_lines_between(-13.1, 8.2, 3)
    assert [4.7] == tesselation_lines_between(3.34, 5.27, 2)
    assert [2.7, 3.3, 4.7] == tesselation_lines_between(2.7, 4.7, 2)
    assert [-0.7, 0.7] == tesselation_lines_between(-6.2, 6.29, 7)
    assert [] == tesselation_lines_between(0.71, 8.29, 9)


def test_tesselation_lines_between_outside_range():
    with pytest.raises(ValueError):
        tesselation_lines_between(4.2, 7.6, 1.3)


def test_remove_duplicates_int():
    assert [1, 2, 4, 5, 7] == remove_duplicates_preserving_order(
        [1, 2, 4, 5, 1, 2, 1, 1, 7]
    )
    assert [91, 3, 7, 21] == remove_duplicates_preserving_order([91, 3, 7, 3, 3, 21])
    assert [-33, 5] == remove_duplicates_preserving_order([-33, -33, 5, -33])


def test_remove_duplicates_point():
    points = [Point(4, 9), Point(-9, 3), Point(4, 9)]
    expected = [Point(4, 9), Point(-9, 3)]
    assert expected == remove_duplicates_preserving_order(points)
