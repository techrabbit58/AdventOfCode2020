"""
Advent Of Code 2020, Day 20.
https://adventofcode.com/2020/day/20
"""
import re
import time
from enum import Enum
from itertools import permutations
from typing import List, Set

# input_file = 'test20.txt'
input_file = 'input20.txt'

Image = List[str]


class Fit(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    UP = 4


class Tile:
    id: int
    neighbours: Set[int]
    image: List[str]

    def __str__(self) -> str:
        return str(self.id)

    @staticmethod
    def _edge(img, p):
        return ''.join(s[p] for s in img)

    def __init__(self, tile: str):
        head, _, tail = tile.partition('\n')
        tid = int(re.match(r'^Tile (\d+):', head).group(1))
        self.id = tid
        self.neighbours = set()
        self.rotation = 0
        self.flipped = 0
        image = tail.split('\n')
        self.image = image
        self.rim = [image[0], image[-1],
                    image[0][::-1], image[-1][::-1],
                    self._edge(image, 0), self._edge(image, -1),
                    self._edge(image, 0)[::-1], self._edge(image, -1)[::-1]]

    def tie(self, other: "Tile"):
        for a in self.rim:
            for b in other.rim:
                if a == b:
                    self.neighbours.add(other.id)


def part1(photographs: List[Tile]):
    a: Tile
    b: Tile
    for a, b in permutations(photographs, 2):
        a.tie(b)
        b.tie(a)
    result = 1
    corners = []
    for a in photographs:
        if len(a.neighbours) == 2:
            corners.append(a)
            result *= a.id
    for a in corners:
        print(a.id, a.neighbours)
    return result


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
