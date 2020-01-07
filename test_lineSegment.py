import lineSegment
import vector as vec

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
