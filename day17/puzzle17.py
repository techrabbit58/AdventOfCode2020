"""
Advent Of Code 2020, Day 17.
https://adventofcode.com/2020/day/17
You may possibly want to view a talk on video, given by Jack Diederich.
(https://youtu.be/o9pEzgHorH0, PyCon US, Sta. Clara 2012)
"""
import time

input_file = 'input17.txt'


def load(fn):
    with open(fn) as fh:
        return fh.read().strip()


def prepare(raw_input):
    return {(x, y, 0, 0) for y, line in enumerate(raw_input.split('\n')) for x, ch in enumerate(line) if ch == '#'}


def neighbours_3d(cell):
    x, y, z, w = cell
    for dz in (1, 0, -1):
        yield x - 1, y - 1, z + dz, w
        yield x, y - 1, z + dz, w
        yield x + 1, y - 1, z + dz, w
        yield x - 1, y, z + dz, w
        yield x + 1, y, z + dz, w
        yield x - 1, y + 1, z + dz, w
        yield x, y + 1, z + dz, w
        yield x + 1, y + 1, z + dz, w
        if dz != 0:
            yield x, y, z + dz, w


def neighbours_4d(cell):
    x, y, z, w = cell
    for dw in (-1, 0, 1):
        for dz in (1, 0, -1):
            yield x - 1, y - 1, z + dz, w + dw
            yield x, y - 1, z + dz, w + dw
            yield x + 1, y - 1, z + dz, w + dw
            yield x - 1, y, z + dz, w + dw
            yield x + 1, y, z + dz, w + dw
            yield x - 1, y + 1, z + dz, w + dw
            yield x, y + 1, z + dz, w + dw
            yield x + 1, y + 1, z + dz, w + dw
            if dz != 0 or dw != 0:
                yield x, y, z + dz, w + dw


def advance(cells, neighbours=None):
    new_cells = set()
    updated = cells | set(new_cell for cell in cells for new_cell in neighbours(cell))
    for new_cell in updated:
        count = sum((neighbour in cells) for neighbour in neighbours(new_cell))
        if count == 3 or (count == 2 and new_cell in cells):
            new_cells.add(new_cell)
    return new_cells


def solution(state, last_cycle=6, neighbours=None):
    for _ in range(last_cycle):
        state = advance(state, neighbours)
    return len(state)


if __name__ == '__main__':
    puzzle_input = load(input_file)
    input_records = prepare(puzzle_input)

    start = time.perf_counter()
    print('part 1:', solution(input_records, neighbours=neighbours_3d), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', solution(input_records, neighbours=neighbours_4d), 'time', round(time.perf_counter() - start, 4))
