import circleArc
import vector as vec
import pytest


# ------- isPointInsideCircle() ----------

def test_point_inside_angle():
    assert True == circleArc.isPointInsideCircle(57.6, 180.2, 170.3)
    assert True == circleArc.isPointInsideCircle(253.1, 18.7, 2.6)
    assert True == circleArc.isPointInsideCircle(19.5, 127.3, 127.3)
    assert False == circleArc.isPointInsideCircle(18.7, 183.3, 227.9)
    assert False == circleArc.isPointInsideCircle(194.2, 145.8, 184.6)
    assert False == circleArc.isPointInsideCircle(164.8, 164.8, 12.5)

def test_point_inside_angle_outside_range():
    with pytest.raises(ValueError):
        circleArc.isPointInsideCircle(-3.5, 340.1, 8.8)
    with pytest.raises(ValueError):
        circleArc.isPointInsideCircle(71.8, 721.8, 328.8)
    with pytest.raises(ValueError):
        circleArc.isPointInsideCircle(71.8, 721.8, 328.8)

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
    assert vec.lengthSqrd(frameRect[0] - vec.Point(2.5, 0.97)) < 0.001
    assert vec.lengthSqrd(frameRect[1] - vec.Point(6.98, 4.5)) < 0.001

def test_small_arc_crossing_zero_angle_rect():
    arc = circleArc.CircleArc({
        "center": [5, 2],
        "radius": 2.5,
        "theta1": 334.62,
        "theta2": 24.23,
        "startsFromA": True
    })
    frameRect = arc.getFrameRect()
    assert vec.lengthSqrd(frameRect[0] - vec.Point(7.26, 0.93)) < 0.001
    assert vec.lengthSqrd(frameRect[1] - vec.Point(7.5, 3.02)) < 0.001

def test_tiny_arc__rect():
    arc = circleArc.CircleArc({
        "center": [5, 2],
        "radius": 2.5,
        "theta1": 220.28,
        "theta2": 236.76,
        "startsFromA": True
    })
    frameRect = arc.getFrameRect()
    assert vec.lengthSqrd(frameRect[0] - vec.Point(3.09, -0.09)) < 0.001
    assert vec.lengthSqrd(frameRect[1] - vec.Point(3.63, 0.39)) < 0.001
