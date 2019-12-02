#!/usr/bin/env python

import json
import sys
from path import Path
from segment import Segment

def load(filename):
    data = json.load(open(filename))
    path = Path(data["pathID"])
    for segment in data["segments"]:
        path.append(Segment(segment["x"], segment["y"], segment["curvature"], segment["g"]))
    return path
    

if __name__ == '__main__':
    filename = "path.json"
    if len(sys.argv) < 2:
        print("Assuming default filename: ", filename)
        print("You can pass name of file describing robots path as a script argument")
    else:
        filename = sys.argv[1]
    # todo: add checking if it's really .json file
    path = load(filename)
    print("Path loaded with ", path.numberOfSegments, " segments")

