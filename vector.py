#!/usr/bin/python

import math


class Vector(object):
    '''
    Class of Vector(Point), represents a 2D vector (x, y).'
    '''
    __slots__ = ["x", "y"]

    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, val):
        return Point(self[0] + val[0], self[1] + val[1])

    def __sub__(self, val):
        return Point(self[0] - val[0], self[1] - val[1])

    def __iadd__(self, val):
        self.x = val[0] + self.x
        self.y = val[1] + self.y
        return self

    def __isub__(self, val):
        self.x = self.x - val[0]
        self.y = self.y - val[1]
        return self

    def __div__(self, val):
        return Point(self[0] / val, self[1] / val)

    def __mul__(self, val):
        return Point(self[0] * val, self[1] * val)

    def __idiv__(self, val):
        self[0] = self[0] / val
        self[1] = self[1] / val
        return self

    def __imul__(self, val):
        self[0] = self[0] * val
        self[1] = self[1] * val
        return self

    def __getitem__(self, key):
        if(key == 0):
            return self.x
        elif(key == 1):
            return self.y
        else:
            raise Exception("Invalid key to Point")

    def __setitem__(self, key, value):
        if(key == 0):
            self.x = value
        elif(key == 1):
            self.y = value
        else:
            raise Exception("Invalid key to Point")

    def __str__(self):  # For printing
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __repr__(self):  # For printing
        return '("%s","%s")' % (self.x, self.y)

    def __eq__(self, other):
        return isinstance(other, Vector) and \
            self.x == other.x and self.y == other.y

    def __hash__(self):  # For using set() with Pts
        return hash(self.__repr__())

    def __ne__(self, other):
        ret = self.__eq__(other)
        return ret if ret is NotImplemented else not ret


Point = Vector


def distanceSqrd(point1, point2):
    'Returns the distance between two points squared. Marginally faster than Distance()'
    return ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)


def distance(point1, point2):
    'Returns the distance between two points'
    return math.sqrt(distanceSqrd(point1, point2))


def lengthSqrd(vec):
    'Returns the length of a vector sqaured. Faster than Length(), but only marginally'
    return vec[0]**2 + vec[1]**2


def length(vec):
    'Returns the length of a vector'
    return math.sqrt(lengthSqrd(vec))


def normalize(vec):
    'Returns a new vector that has the same direction as vec, but has a length of one.'
    if(vec[0] == 0. and vec[1] == 0.):
        return Vector(0., 0.)
    return vec / length(vec)


def dot(a, b):
    'Computes the dot product of a and b'
    return a[0]*b[0] + a[1]*b[1]


def projectOnto(w, v):
    'Projects w onto v.'
    return v * dot(w, v) / lengthSqrd(v)


def rotate(p, oAB, angle):
    'Rotate p around oAB by angle counterclockwise'
    s_a = math.sin(angle)
    c_a = math.cos(angle)
    p = Point((p[0]-oAB[0]) * c_a - (p[1]-oAB[1]) * s_a,
              (p[0]-oAB[0]) * s_a + (p[1]-oAB[1]) * c_a)
    return Point(p[0] + oAB[0], p[1] + oAB[1])

def angle(vec):
    'Returns the angle of a vector (in radians) in range [0, 2 * pi]'
    return (math.atan2(vec.y, vec.x) + 2*math.pi) % (2 * math.pi)
