#!/usr/bin/env python

import config 
import math


def tesselationLinesBetween(begin, end, d):
    if d < 2 * config.ROBOT_RADIUS:
        raise ValueError(
            "Given parameter d is smaller then double of robot radius!")

    dMin = math.floor(begin / d)
    dMax = math.ceil(end / d)
    result = []
    for i in range(dMin, dMax + 1):
        for sign in [-1, 1]:
            value = i * d + config.ROBOT_RADIUS * sign
            if begin <= value <= end:
                result.append(value)
    return result


def checkLineParallelism(line):
    if line[0] != 0:
        return 0, 1
    elif line[1] != 0:
        return 1, 0
    else:
        raise ValueError("Passed tuple doesn't represent a line!")

def removeDuplicatesPreservingOrder(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]