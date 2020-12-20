"""
Advent Of Code 2020, Day 20.
https://adventofcode.com/2020/day/20
"""
import re
import time
from dataclasses import dataclass
from enum import Enum
from itertools import permutations
from typing import List, Dict

input_file = 'test20.txt'
# input_file = 'input20.txt'

Image = List[str]


class Fit(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    OVER = 3
    UNDER = 4


@dataclass
class Tile:
    id: int
    neighbours: Dict[Fit, int]
    upper: str
    lower: str
    left: str
    right: str

    def __str__(self) -> str:
        return str(self.id)

    @staticmethod
    def _edge(img, p):
        return ''.join(s[p] for s in img)

    @classmethod
    def from_str(cls, tile: str):
        head, _, tail = tile.partition('\n')
        tid = int(re.match(r'^Tile (\d+):', head).group(1))
        obj_id = tid
        img = tail.split('\n')
        obj_upper = img[0]
        obj_lower = img[-1]
        obj_left = Tile._edge(img, 0)
        obj_right = Tile._edge(img, -1)
        obj_neighbours = {}
        return cls(obj_id, obj_neighbours, obj_upper, obj_lower, obj_left, obj_right)

    def tie(self, other: "Tile") -> Fit:
        if self.upper == other.lower:
            self.neighbours[Fit.UNDER] = other.id
            return Fit.UNDER
        if self.lower == other.upper:
            self.neighbours[Fit.OVER] = other.id
            return Fit.OVER
        if self.right == other.left:
            self.neighbours[Fit.RIGHT] = other.id
            return Fit.RIGHT
        if self.left == other.right:
            self.neighbours[Fit.LEFT] = other.id
            return Fit.LEFT
        return Fit.NONE

    def flip_left(self) -> None:
        self.lower, self.upper = ''.join(reversed(self.lower)), ''.join(reversed(self.upper))
        self.left, self.right = self.right, self.left

    def flip_up(self) -> None:
        self.left, self.right = ''.join(reversed(self.right)), ''.join(reversed(self.left))
        self.lower, self.upper = self.upper, self.lower

    def rotate(self) -> None:
        self.left, self.upper, self.right, self.lower = self.lower, self.left, self.upper, self.right


def part1(photographs: List[Tile]):
    a: Tile
    b: Tile
    for a, b in permutations(photographs, 2):
        a.tie(b)
        b.flip_up()
        a.tie(b)
        b.flip_left()
        a.tie(b)
        b.flip_up()
        a.tie(b)
        b.flip_left()
        b.rotate()
        a.tie(b)
        b.flip_up()
        a.tie(b)
        b.flip_left()
        a.tie(b)
        b.flip_up()
        a.tie(b)
        b.flip_left()
        b.rotate()
        b.rotate()
        b.rotate()
    result = 1
    for a in photographs:
        if len(a.neighbours) == 2:
            result *= a.id
    return result


def part2(puzzle):
    return len(puzzle)


def load(fn):
    with open(fn) as fh:
        return fh.read().strip()


def chop(raw_input):
    return [line for line in raw_input.split('\n\n')]


def parse(chunks: List[str]):
    return [Tile.from_str(tile) for tile in chunks]


if __name__ == '__main__':
    puzzle_input = load(input_file)
    input_records = parse(chop(puzzle_input))

    start = time.perf_counter()
    print('part 1:', part1(input_records), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(input_records), 'time', round(time.perf_counter() - start, 4))
