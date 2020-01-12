#!/usr/bin/env python

import pytest
import config 
import utils 
import vector as vec

if config.ROBOT_RADIUS != 0.7:
    pytest.skip("Tests for tesselationLinesBetween() are only valid for robot radius equal to 0.7",
                allow_module_level=True)


# -------- tesselationLinesBetween() -----------

def test_tesselation_lines_between():
    assert [4.7, 7.3] == utils.tesselationLinesBetween(4.2, 7.6, 4)
    assert [-12.7, -11.3, -9.7, -8.3, -6.7, -5.3, -3.7, -2.3, -0.7, 0.7,
            2.3, 3.7, 5.3, 6.7] == utils.tesselationLinesBetween(-13.1, 8.2, 3)
    assert [4.7] == utils.tesselationLinesBetween(3.34, 5.27, 2)
    assert [2.7, 3.3, 4.7] == utils.tesselationLinesBetween(2.7, 4.7, 2)
    assert [-0.7, 0.7] == utils.tesselationLinesBetween(-6.2, 6.29, 7)
    assert [] == utils.tesselationLinesBetween(0.71, 8.29, 9)


def test_tesselation_lines_between_outside_range():
    with pytest.raises(ValueError):
        utils.tesselationLinesBetween(4.2, 7.6, 1.3)


# ---- removeDuplicatesPreservingOrder() -------

def test_remove_duplicates_int():
    assert [1, 2, 4, 5, 7] == utils.removeDuplicatesPreservingOrder([1, 2, 4, 5, 1, 2, 1, 1, 7])
    assert [91, 3, 7, 21] == utils.removeDuplicatesPreservingOrder([91, 3, 7, 3, 3, 21])
    assert [-33, 5] == utils.removeDuplicatesPreservingOrder([-33, -33, 5, -33])

def test_remove_duplicates_point():
    points = [vec.Point(4,9), vec.Point(-9, 3), vec.Point(4,9)]
    expected = [vec.Point(4,9), vec.Point(-9, 3)]
    assert expected == utils.removeDuplicatesPreservingOrder(points)
