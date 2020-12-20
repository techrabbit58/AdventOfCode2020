"""
Advent Of Code 2020, Day 20.
https://adventofcode.com/2020/day/20
"""
import re
import time
from itertools import permutations
from typing import List, Set

input_file = 'test20.txt'
# input_file = 'input20.txt'

Image = List[str]


class Tile:
    id: int
    neighbours: Set[int]
    image: Image

    def __str__(self) -> str:
        return str(self.id)

    @staticmethod
    def _edge(img, p):
        return ''.join(s[p] for s in img)

    def __init__(self, tile: str):
        head, _, tail = tile.partition('\n')
        self.id = int(re.match(r'^Tile (\d+):', head).group(1))
        self.neighbours = set()
        self.image = tail.split('\n')
        self.rim = [
            self.image[0], self.image[-1],
            self.image[0][::-1], self.image[-1][::-1],
            self._edge(self.image, 0), self._edge(self.image, -1),
            self._edge(self.image, 0)[::-1], self._edge(self.image, -1)[::-1]
        ]

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
    for a in photographs:
        if len(a.neighbours) == 2:
            # A tile with only two neighbors must be a corner.
            result *= a.id
    return result


def part2(photographs):
    corners, edges, paving = segregate_tiles_by_neighbour_count(photographs)
    matrix = [[0] * round(len(photographs) ** 0.5) for _ in range(round(len(photographs) ** 0.5))]
    for row in matrix:
        print(row)
    for a in corners:
        print(a.id, a.neighbours)
    for a in edges:
        print(a.id, a.neighbours)
    for a in paving:
        print(a.id, a.neighbours)
    return len(photographs)


def segregate_tiles_by_neighbour_count(photographs):
    a: Tile
    corners: List[Tile] = []
    edges: List[Tile] = []
    paving: List[Tile] = []
    for a in photographs:
        if len(a.neighbours) == 2:
            corners.append(a)
        elif len(a.neighbours) == 3:
            edges.append(a)
        else:
            paving.append(a)
    return corners, edges, paving


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
