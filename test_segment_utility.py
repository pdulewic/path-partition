import segment
import pytest
import config

if config.ROBOT_RADIUS != 0.7:
    pytest.skip("Tests for tesselationLinesBetween() are only valid for robot radius equal to 0.7",
                allow_module_level=True)


def test_tesselation_lines_between():
    assert [4.7, 7.3] == segment.tesselationLinesBetween(4.2, 7.6, 4)
    assert [-12.7, -11.3, -9.7, -8.3, -6.7, -5.3, -3.7, -2.3, -0.7, 0.7,
            2.3, 3.7, 5.3, 6.7] == segment.tesselationLinesBetween(-13.1, 8.2, 3)
    assert [4.7] == segment.tesselationLinesBetween(3.34, 5.27, 2)
    assert [2.7, 3.3, 4.7] == segment.tesselationLinesBetween(2.7, 4.7, 2)
    assert [-0.7, 0.7] == segment.tesselationLinesBetween(-6.2, 6.29, 7)
    assert [] == segment.tesselationLinesBetween(0.71, 8.29, 9)


def test_tesselation_lines_between_outside_range():
    with pytest.raises(ValueError):
        segment.tesselationLinesBetween(4.2, 7.6, 1.3)
