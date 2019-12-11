import lineSegment
import vector as vec

def test_frame_rect():
    segment = lineSegment.LineSegment({
        "pA": [-5, -2],
        "pB": [-1, 4]
    })
    frameRect = segment.getFrameRect()
    assert frameRect[0] == vec.Point(-5, -2)
    assert frameRect[1] == vec.Point(-1, 4)