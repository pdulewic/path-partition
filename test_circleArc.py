import circleArc
import vector as vec
import pytest
import config


# ---------- isAngleWithinRange() ------------

def test_angle_within_range():
    assert True == circleArc.isAngleWithinRange(57.6, 180.2, 170.3)
    assert True == circleArc.isAngleWithinRange(253.1, 18.7, 2.6)
    assert True == circleArc.isAngleWithinRange(19.5, 127.3, 127.3)
    assert False == circleArc.isAngleWithinRange(18.7, 183.3, 227.9)
    assert False == circleArc.isAngleWithinRange(194.2, 145.8, 184.6)
    assert False == circleArc.isAngleWithinRange(164.8, 164.8, 12.5)

def test_angle_outside_range_0_360():
    with pytest.raises(ValueError):
        circleArc.isAngleWithinRange(-3.5, 340.1, 8.8)
    with pytest.raises(ValueError):
        circleArc.isAngleWithinRange(71.8, 721.8, 328.8)
    with pytest.raises(ValueError):
        circleArc.isAngleWithinRange(71.8, 721.8, 328.8)

# ---------- isPointInsideCircleArc() ------------

def test_point_inside_circle_arc():
    arc1 = circleArc.CircleArc({
        "center": [-7.25, 2.99],
        "radius": 3.17,
        "theta1": 315.48,
        "theta2": 189.13,
        "startsFromA": True
    })
    assert circleArc.isPointInsideCircleArc(vec.Point(-10.39, 2.62), arc1)

    arc2 = circleArc.CircleArc({
        "center": [3, -4],
        "radius": 1.5,
        "theta1": 52.22,
        "theta2": 308.53,
        "startsFromA": True
    })
    assert circleArc.isPointInsideCircleArc(vec.Point(-3.79, -2.73), arc2)

    arc3 = circleArc.CircleArc({
        "center": [10, -4],
        "radius": 1,
        "theta1": 0,
        "theta2": 180,
        "startsFromA": True
    })
    assert circleArc.isPointInsideCircleArc(vec.Point(11, -4), arc3)

def test_point_outside_circle_arc():
    arc1 = circleArc.CircleArc({
        "center": [-7.25, 2.99],
        "radius": 3.17,
        "theta1": 315.48,
        "theta2": 189.13,
        "startsFromA": True
    })
    assert not circleArc.isPointInsideCircleArc(vec.Point(-10.34, 2.31), arc1)

    arc2 = circleArc.CircleArc({
        "center": [3, -4],
        "radius": 1.5,
        "theta1": 52.22,
        "theta2": 308.53,
        "startsFromA": True
    })
    assert not circleArc.isPointInsideCircleArc(vec.Point(4.06, -2.94), arc2)

    arc3 = circleArc.CircleArc({
        "center": [10, -4],
        "radius": 1,
        "theta1": 0,
        "theta2": 180,
        "startsFromA": True
    })
    assert not circleArc.isPointInsideCircleArc(vec.Point(9.05, -4.31), arc3)



# ---- removeDuplicatesPreservingOrder() -------

def test_remove_duplicates():
    assert [1, 2, 4, 5, 7] == circleArc.removeDuplicatesPreservingOrder([1, 2, 4, 5, 1, 2, 1, 1, 7])
    assert [91, 3, 7, 21] == circleArc.removeDuplicatesPreservingOrder([91, 3, 7, 3, 3, 21])
    assert [-33, 5] == circleArc.removeDuplicatesPreservingOrder([-33, -33, 5, -33])

# ---------- getFrameRect() -------------

def test_full_circle_rect():
    arc = circleArc.CircleArc({
        "center": [-3, 7],
        "radius": 1.5,
        "theta1": 0,
        "theta2": 360,
        "startsFromA": True
    })
    frameRect = arc.getFrameRect()
    assert frameRect[0] == vec.Point(-4.5, 5.5)
    assert frameRect[1] == vec.Point(-1.5, 8.5)


def test_half_circle_rect():
    arc = circleArc.CircleArc({
        "center": [-3, 7],
        "radius": 1.5,
        "theta1": 0,
        "theta2": 180,
        "startsFromA": True
    })
    frameRect = arc.getFrameRect()
    assert frameRect[0] == vec.Point(-4.5, 7)
    assert frameRect[1] == vec.Point(-1.5, 8.5)

def test_medium_arc_rect():
    arc = circleArc.CircleArc({
        "center": [5, 2],
        "radius": 2.5,
        "theta1": 37.48,
        "theta2": 204.28,
        "startsFromA": True
    })
    frameRect = arc.getFrameRect()
    assert vec.lengthSqrd(frameRect[0] - vec.Point(2.5, 0.97)) < config.NUM_ERR
    assert vec.lengthSqrd(frameRect[1] - vec.Point(6.98, 4.5)) < config.NUM_ERR

def test_small_arc_crossing_zero_angle_rect():
    arc = circleArc.CircleArc({
        "center": [5, 2],
        "radius": 2.5,
        "theta1": 334.62,
        "theta2": 24.23,
        "startsFromA": True
    })
    frameRect = arc.getFrameRect()
    assert vec.lengthSqrd(frameRect[0] - vec.Point(7.26, 0.93)) < config.NUM_ERR
    assert vec.lengthSqrd(frameRect[1] - vec.Point(7.5, 3.02)) < config.NUM_ERR

def test_tiny_arc_rect():
    arc = circleArc.CircleArc({
        "center": [5, 2],
        "radius": 2.5,
        "theta1": 220.28,
        "theta2": 236.76,
        "startsFromA": True
    })
    frameRect = arc.getFrameRect()
    assert vec.lengthSqrd(frameRect[0] - vec.Point(3.09, -0.09)) < config.NUM_ERR
    assert vec.lengthSqrd(frameRect[1] - vec.Point(3.63, 0.39)) < config.NUM_ERR

# ------- intersectionWithLine() ----------

def test_full_circle_intersection():
    arc = circleArc.CircleArc({
        "center": [5, 2],
        "radius": 2.5,
        "theta1": 0,
        "theta2": 360,
        "startsFromA": True
    })
    intersection = arc.intersectionWithLine((1,0,-3))
    assert 2 == len(intersection)
    assert intersection[0] == vec.Point(3, 3.5)
    assert intersection[1] == vec.Point(3, 0.5)

def test_arc_intersection_with_OY():
    arc = circleArc.CircleArc({
        "center": [-5.5, 2.55],
        "radius": 6.12,
        "theta1": 241.58,
        "theta2": 63.72,
        "startsFromA": True
    })
    intersection = arc.intersectionWithLine((1,0,0))
    assert 2 == len(intersection)
    assert vec.lengthSqrd(intersection[0] - vec.Point(0, 5.23)) < config.NUM_ERR
    assert vec.lengthSqrd(intersection[1] - vec.Point(0, -0.13)) < config.NUM_ERR

def test_intersection_with_circle_but_not_with_arc():
    arc = circleArc.CircleArc({
        "center": [3, -4],
        "radius": 1.5,
        "theta1": 52.22,
        "theta2": 308.53,
        "startsFromA": True
    })
    assert not arc.intersectionWithLine((1,0,-4))

def test_only_one_intersection_point():
    arc = circleArc.CircleArc({
        "center": [-7.25, 2.99],
        "radius": 3.17,
        "theta1": 315.48,
        "theta2": 189.13,
        "startsFromA": True
    })
    intersection = arc.intersectionWithLine((0,1,-2))
    assert 1 == len(intersection)
    assert vec.lengthSqrd(intersection[0] - vec.Point(-4.23, 2)) < config.NUM_ERR

def test_intersection_on_arc_edges():
    arc = circleArc.CircleArc({
        "center": [10, -4],
        "radius": 1,
        "theta1": 0,
        "theta2": 180,
        "startsFromA": True
    })
    intersection = arc.intersectionWithLine((0,1,4))
    assert 2 == len(intersection)
    assert intersection[0] == vec.Point(11, -4)
    assert intersection[1] == vec.Point(9, -4)


