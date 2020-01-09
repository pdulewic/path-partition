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
    intersection = segment.intersectionWithLine((1,0,-1))
    assert 1 == len(intersection)
    assert intersection[0] == vec.Point(1, 2)

def test_intersection_with_parallel_to_OX():
    segment = lineSegment.LineSegment({
        "pA": [3, -7],
        "pB": [5, -4]
    })
    intersection = segment.intersectionWithLine((0,1,5))
    assert 1 == len(intersection)
    assert vec.lengthSqrd(intersection[0] - vec.Point(4.33, -5)) < config.NUM_ERR

def test_intersection_with_OY():
    segment = lineSegment.LineSegment({
        "pA": [6.64, 2.3],
        "pB": [-5.86, -3.6]
    })
    intersection = segment.intersectionWithLine((1,0,0))
    assert 1 == len(intersection)
    assert vec.lengthSqrd(intersection[0] - vec.Point(0, -0.83)) < config.NUM_ERR