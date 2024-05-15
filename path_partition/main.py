#!/usr/bin/env python

import json
import logging
import argparse
from path_partition.config import DEFAULT_TESSELATION, ROBOT_RADIUS
from path_partition.path import Path
from path_partition.segments.circle_arc import CircleArc
from path_partition.segments.line_segment import LineSegment


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(module)s: %(message)s"
)

logger = logging.getLogger(__name__)


def load(filename):
    data = json.load(open(filename))
    path = Path(data["path_id"])
    for segment in data["segments"]:
        # in case of adding new types of segments, this statements should
        # be replaced by some switch/case instructions
        if segment["is_line_segment"]:
            path.append(LineSegment(segment))
        else:
            path.append(CircleArc(segment))
    return path


if __name__ == "__main__":
    logger.info("Starting PathPartition")

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
        default=DEFAULT_TESSELATION,
        help="tesselation square size",
    )
    args = parser.parse_args()
    filename = args.file

    if not filename.endswith(".json"):
        logger.error("Specified file is not a .json file, exiting...")
        exit()

    try:
        logger.info("Loading %s...", filename)
        path = load(filename)
        logger.info(f"Path loaded with {path.number_of_segments} segments")

        tesselation_parameter = float(args.tesselation)
        if tesselation_parameter < 2 * ROBOT_RADIUS:
            logger.warning(
                f"Tesselation value is smaller then 2 * robot radius ({ROBOT_RADIUS * 2}). "
                f"Setting default value {DEFAULT_TESSELATION}"
            )
            tesselation_parameter = DEFAULT_TESSELATION
        path.calculate_stage_borders(tesselation_parameter)
        path.display(tesselation_parameter)
    except IOError:
        logger.error("File %s not accessible", filename)
