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
        print("Assuming default filename: ", filename)
        print("You can pass name of file describing robots path as a script argument")
    else:
        filename = sys.argv[1]
    # todo: add checking if it's really .json file, and if it exists
    path = load(filename)
    print("Path loaded with ", path.numberOfSegments, " segments")
    path.display()

