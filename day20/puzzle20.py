"""
Advent Of Code 2020, Day 20.
https://adventofcode.com/2020/day/20
"""
import re
import time
from collections import defaultdict
from enum import Enum
from itertools import permutations
from typing import List, Dict, Tuple

input_file = 'test20.txt'
# input_file = 'input20.txt'

Image = List[str]


class Fit(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    UP = 4


class Tile:
    id: int
    neighbours: Dict[Tuple[int, int], Dict[Fit, int]]
    rotation: int
    flip: int
    upper: str
    lower: str
    left: str
    right: str

    def __str__(self) -> str:
        return str(self.id)

    @staticmethod
    def _edge(img, p):
        return ''.join(s[p] for s in img)

    def __init__(self, tile: str):
        head, _, tail = tile.partition('\n')
        tid = int(re.match(r'^Tile (\d+):', head).group(1))
        self.id = tid
        self.neighbours = defaultdict(lambda: {})
        self.rotation = 0
        self.flip = 0
        img = tail.split('\n')
        self.upper = img[0]
        self.lower = img[-1]
        self.left = Tile._edge(img, 0)
        self.right = Tile._edge(img, -1)

    def tie(self, other: "Tile"):
        if self.upper == other.lower:
            self.neighbours[(self.rotation, self.flip)][Fit.UP] = other.id
        elif self.lower == other.upper:
            self.neighbours[(self.rotation, self.flip)][Fit.DOWN] = other.id
        elif self.right == other.left:
            self.neighbours[(self.rotation, self.flip)][Fit.RIGHT] = other.id
        elif self.left == other.right:
            self.neighbours[(self.rotation, self.flip)][Fit.LEFT] = other.id
        else:
            pass

    def flip_left(self):
        self.flip = (self.flip + 1) % 2
        self.rotation = (self.rotation + 2) % 4
        self.lower, self.upper = ''.join(reversed(self.lower)), ''.join(reversed(self.upper))
        self.left, self.right = self.right, self.left

    def flip_up(self):
        self.flip = (self.flip + 1) % 2
        self.rotation = (self.rotation + 2) % 4
        self.left, self.right = ''.join(reversed(self.right)), ''.join(reversed(self.left))
        self.lower, self.upper = self.upper, self.lower

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
        self.left, self.upper, self.right, self.lower = self.lower, self.left, self.upper, self.right


def part1(photographs: List[Tile]):
    a: Tile
    b: Tile
    for a, b in permutations(photographs, 2):
        for _ in range(2):
            a.flip_left()
            for _ in range(4):
                a.rotate()
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
    possible_left_upper_corner = []
    for a in photographs:
        if {k: v for k, v in a.neighbours.items() if len(v) == 2 and Fit.RIGHT in v and Fit.DOWN in v}:
            possible_left_upper_corner.append(a)
    for a in possible_left_upper_corner:
        print(a.id, {k: v for k, v in a.neighbours.items() if len(v) == 2 and Fit.RIGHT in v and Fit.DOWN in v})
    return None


def part2(puzzle):
    return len(puzzle)


def load(fn):
    with open(fn) as fh:
        return fh.read().strip()


def chop(raw_input):
    return [line for line in raw_input.split('\n\n')]


def parse(chunks: List[str]):
    return [Tile(tile) for tile in chunks]


if __name__ == '__main__':
    puzzle_input = load(input_file)
    input_records = parse(chop(puzzle_input))

    start = time.perf_counter()
    print('part 1:', part1(input_records), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(input_records), 'time', round(time.perf_counter() - start, 4))
