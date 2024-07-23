from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class Point:

    x: int
    y: int

    def __add__(self, other: Point) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"{self.x},{self.y}"

    def dist(self, other: Point) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def adj(self, other: Point) -> bool:
        return self.dist(other) == 1


class Direction:
    NONE = Point(0, 0)
    LEFT = Point(-1, 0)
    DOWN = Point(0, 1)
    RIGHT = Point(1, 0)
    UP = Point(0, -1)