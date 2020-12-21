"""
Advent Of Code 2020, Day 20.
https://adventofcode.com/2020/day/20
"""
import re
import time
from itertools import permutations
from typing import List, Set, Tuple, Optional, Iterator

input_file = 'test20.txt'
# input_file = 'input20.txt'

Image = List[str]


class Tile:
    id: int
    neighbours: Set[int]
    image: Image
    rim: List[str]

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
            self._edge(self.image, 0)[::-1], self._edge(self.image, -1)[::-1]]

    def tie(self, other: "Tile"):
        for a in self.rim:
            for b in other.rim:
                if a == b:
                    self.neighbours.add(other.id)

    def flip(self):
        self.image = self.image[::-1]

    def rotate(self):
        new_image = []
        for i in range(len(self.image[0])):
            new_line = []
            for j in range(len(self.image)):
                new_line.append(self.image[j][i])
            new_image.append(''.join(new_line))
        self.image = new_image

    @property
    def up(self) -> str:
        return self.image[0]

    @property
    def down(self) -> str:
        return self.image[-1]

    @property
    def left(self) -> str:
        return self._edge(self.image, 0)

    @property
    def right(self) -> str:
        return self._edge(self.image, -1)


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


def transform(t: Tile) -> Iterator[Tile]:
    for _ in range(2):
        t.flip()
        for _ in range(2):
            t.rotate()
            yield t


def part2(light_box: List[Tile]) -> int:
    height = width = round(len(light_box) ** 0.5)
    corners, edges, pavings = segregate_tiles_by_neighbour_count(light_box)
    matrix = rearrange(width, height, corners, edges, pavings)
    picture: Image = []
    this, right, down, diagonal = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    for t in transform(this):
        for o in transform(down):
            if t.down == o.up:
                for r in transform(right):
                    if t.right == r.left:
                        for d in transform(diagonal):
                            if d.left == o.right and d.up == r.down:
                                this, right, down, diagonal = t, r, o, d
                                break
                        break
                break
    for col in range(1, width - 1):
        this, right, down, diagonal = \
            matrix[0][col], matrix[0][col + 1], matrix[1][col], matrix[1][col + 1]
        for r in transform(right):
            if r.left == this.right:
                for d in transform(diagonal):
                    if d.left == down.right and r.down == d.up:
                        print(this, r, this.right, right.left)
                        print(down, d, down.right, d.left)
                        print(d, r, d.up, r.down)

    return len(light_box)


def rearrange(wid: int, hgt: int, corners: List[Tile], edges: List[Tile], pavings: List[Tile]) -> List[List[Tile]]:
    matrix: List[List[Optional[Tile]]] = [[None] * wid for _ in range(hgt)]
    matrix[0][0] = corners[0]
    corners.remove(matrix[0][0])
    for col in range(1, wid - 1):
        for tile in edges:
            if matrix[0][col - 1].id in tile.neighbours:
                matrix[0][col] = tile
                break
        edges.remove(matrix[0][col])
    for tile in corners:
        if matrix[0][-2].id in tile.neighbours:
            matrix[0][-1] = tile
            break
    corners.remove(matrix[0][-1])
    for row in range(1, hgt - 1):
        for tile in edges:
            if matrix[row - 1][0].id in tile.neighbours:
                matrix[row][0] = tile
                break
        edges.remove(matrix[row][0])
        for col in range(1, wid - 1):
            for tile in pavings:
                if matrix[row - 1][col].id in tile.neighbours and matrix[row][col - 1].id in tile.neighbours:
                    matrix[row][col] = tile
                    break
            pavings.remove(matrix[row][col])
        for tile in edges:
            if matrix[row - 1][-1].id in tile.neighbours and matrix[row][-2].id in tile.neighbours:
                matrix[row][-1] = tile
                break
        edges.remove(matrix[row][-1])
    for tile in corners:
        if matrix[-2][0].id in tile.neighbours:
            matrix[-1][0] = tile
            break
    corners.remove(matrix[-1][0])
    for col in range(1, wid - 1):
        for tile in edges:
            if matrix[-1][col - 1].id in tile.neighbours and matrix[-2][col].id in tile.neighbours:
                matrix[-1][col] = tile
                break
        edges.remove(matrix[-1][col])
    matrix[-1][-1] = corners[0]
    return matrix


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
