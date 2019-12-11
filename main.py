#!/usr/bin/env python

import json
import sys
from path import Path
from circleArc import CircleArc
from lineSegment import LineSegment

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
    

if __name__ == '__main__':
    filename = "path.json"
    if len(sys.argv) < 2:
        print("No arguments passed, assuming default filename: ", filename)
    else:
        filename = sys.argv[1]

    if not filename.endswith(".json"):
        print("Specified file is not a .json file, exiting...")
        exit()
    
    try:
        print("Loading", filename, "...")
        path = load(filename)
        print("Path loaded with", path.numberOfSegments, "segments")

        tesselationParameter = 1.0
        if len(sys.argv) > 2:
            tesselationParameter = float(sys.argv[2])

        path.display(tesselationParameter)
    except IOError:
        print("File", filename, "not accessible")

    

