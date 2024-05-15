#!/usr/bin/python
from __future__ import annotations
import math


class Vector:
    """
    Class of Vector(Point), represents a 2D vector (x, y).'
    """

    __slots__ = ["x", "y"]

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x - vector.x, self.y - vector.y)

    def __iadd__(self, vector: Vector) -> Vector:
        self.x = vector.x + self.x
        self.y = vector.y + self.y
        return self

    def __isub__(self, vector: Vector) -> Vector:
        self.x = self.x - vector.x
        self.y = self.y - vector.y
        return self

    def __div__(self, value: float) -> Vector:
        return Vector(self.x / value, self.y / value)

    def __mul__(self, value: float) -> Vector:
        return Vector(self.x * value, self.y * value)

    def __idiv__(self, value: float) -> Vector:
        self.x = self.x / value
        self.y = self.y / value
        return self

    def __imul__(self, value: float) -> Vector:
        self.x = self.x * value
        self.y = self.y * value
        return self

    def __getitem__(self, key: int) -> float:
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise Exception("Invalid key to Point")

    def __setitem__(self, key: int, value: float) -> None:
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise Exception("Invalid key to Point")

    def __str__(self) -> str:  # For printing
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:  # For printing
        return f'("{self.x}","{self.y}")'

    def __eq__(self, other: Vector) -> bool:
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:  # For using set() with Pts
        return hash(self.__repr__())

    def __ne__(self, other: Vector) -> bool:
        ret = self.__eq__(other)
        return ret if ret is NotImplemented else not ret


Point = Vector


def distance_squared(point1: Point, point2: Point) -> float:
    "Returns the distance between two points squared. Marginally faster than Distance()"
    return (point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2


def distance(point1: Point, point2: Point) -> float:
    "Returns the distance between two points"
    return math.sqrt(distance_squared(point1, point2))


def length_squared(vector: Vector) -> float:
    "Returns the length of a vector sqaured. Faster than Length(), but only marginally"
    return vector.x**2 + vector.y**2


def length(vector: Vector) -> float:
    "Returns the length of a vector"
    return math.sqrt(length_squared(vector))


def normalize(vector: Vector) -> Vector:
    "Returns a new vector that has the same direction as vec, but has a length of one."
    if vector.x == 0.0 and vector.y == 0.0:
        return Vector(0.0, 0.0)
    return vector / length(vector)


def dot(vector_a: Vector, vector_b: Vector) -> float:
    "Computes the dot product of a and b"
    return vector_a.x * vector_b.x + vector_a.y * vector_b.y


def project_onto(vector_a: Vector, vector_b: Vector) -> Vector:
    "Projects vector_a onto vector_b."
    return vector_b * dot(vector_a, vector_b) / length_squared(vector_b)


def rotate(point: Point, rotation_center: Point, angle: float) -> Point:
    "Rotate p around oAB by angle counterclockwise"
    sinus_a = math.sin(angle)
    cosinus_a = math.cos(angle)
    temporary_point = Point(
        (point.x - rotation_center.x) * cosinus_a
        - (point.y - rotation_center.y) * sinus_a,
        (point.x - rotation_center.x) * sinus_a
        + (point.y - rotation_center.y) * cosinus_a,
    )
    return Point(
        temporary_point.x + rotation_center.x, temporary_point.y + rotation_center.y
    )


def angle_of_a_vector(vector: Vector) -> float:
    "Returns the angle of a vector (in radians) in range [0, 2 * pi]"
    return (math.atan2(vector.y, vector.x) + 2 * math.pi) % (2 * math.pi)
