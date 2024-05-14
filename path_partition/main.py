#!/usr/bin/env python

import json
import sys
import logging
import argparse
import config
from path import Path
from segments.circleArc import CircleArc
from segments.lineSegment import LineSegment


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(module)s: %(message)s"
)


def load(filename):
    data = json.load(open(filename))
    path = Path(data["pathID"])
    for segment in data["segments"]:
        # in case of adding new types of segments, this statements should
        # be replaced by some switch/case instructions
        if segment["isLineSegment"]:
            path.append(LineSegment(segment))
        else:
            path.append(CircleArc(segment))
    return path


if __name__ == "__main__":
    logging.info("Starting PathPartition")

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="name of the .json file with path to divide",
    )
    parser.add_argument(
        "-t",
        "--tesselation",
        default=config.DEFAULT_TESSELATION,
        help="tesselation square size",
    )
    args = parser.parse_args()
    filename = args.file

    if not filename.endswith(".json"):
        logging.error("Specified file is not a .json file, exiting...")
        exit()

    try:
        logging.info("Loading %s...", filename)
        path = load(filename)
        logging.info("Path loaded with %d segments", path.numberOfSegments)

        tesselationParameter = float(args.tesselation)
        if tesselationParameter < 2 * config.ROBOT_RADIUS:
            logging.warning(
                "Tesselation value is smaller then 2 * robot radius (%f). Setting default value %f",
                config.ROBOT_RADIUS * 2,
                config.DEFAULT_TESSELATION,
            )
            tesselationParameter = config.DEFAULT_TESSELATION
        path.calculateStageBorders(tesselationParameter)
        path.display(tesselationParameter)
    except IOError:
        logging.error("File %s not accessible", filename)
