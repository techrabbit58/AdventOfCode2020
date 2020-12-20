"""
Advent Of Code 2020, Day 20.
https://adventofcode.com/2020/day/20
"""
import re
import time
from itertools import permutations
from typing import List, Set, Tuple, Optional

input_file = 'test20.txt'
# input_file = 'input20.txt'

Image = List[str]


class Tile:
    id: int
    neighbours: Set[int]
    image: Image

    def __repr__(self) -> str:
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


def part2(photographs: List[Tile]) -> int:
    light_box = photographs[:]
    corners, edges, pavings = segregate_tiles_by_neighbour_count(light_box)
    height = width = round(len(light_box) ** 0.5)
    matrix: List[List[Optional[Tile]]] = [[None] * width for _ in range(height)]

    matrix[0][0] = corners[0]

    for col in range(1, width - 1):
        for tile in edges:
            if matrix[0][col - 1].id in tile.neighbours:
                matrix[0][col] = tile
                break
    for tile in corners:
        if matrix[0][-2].id in tile.neighbours:
            matrix[0][-1] = tile
            break
    show_matrix(matrix)

    for row in range(1, height - 1):
        pass

    return len(photographs)


def show_matrix(matrix):
    for row in matrix:
        print(row)


def segregate_tiles_by_neighbour_count(photographs: List[Tile]) -> Tuple[List[Tile], List[Tile], List[Tile]]:
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
