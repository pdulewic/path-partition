#!/usr/bin/env python

from path_partition.config import ROBOT_RADIUS
import math
from typing import Tuple, Iterable


def tesselation_lines_between(
    begin: float, end: float, tesselation_parameter: float
) -> list[float]:
    if tesselation_parameter < 2 * ROBOT_RADIUS:
        raise ValueError(
            "Given tesselation_parameter is smaller then double of robot radius!"
        )

    d_min = math.floor(begin / tesselation_parameter)
    d_max = math.ceil(end / tesselation_parameter)
    result = []
    for i in range(d_min, d_max + 1):
        for sign in [-1, 1]:
            value = i * tesselation_parameter + ROBOT_RADIUS * sign
            if begin <= value <= end:
                result.append(value)
    return result


def check_line_parallelism(line) -> Tuple[int, int]:
    if line[0] != 0:
        return 0, 1
    elif line[1] != 0:
        return 1, 0
    else:
        raise ValueError("Passed tuple doesn't represent a line!")


def remove_duplicates_preserving_order(seq: Iterable) -> list:
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]
