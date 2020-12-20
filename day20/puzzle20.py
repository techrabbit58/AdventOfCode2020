"""
Advent Of Code 2020, Day 20.
https://adventofcode.com/2020/day/20
"""
import re
import time
from typing import List

input_file = 'test20.txt'
# input_file = 'input20.txt'


def load(fn):
    with open(fn) as fh:
        return fh.read().strip()


def chop(raw_input):
    return [line for line in raw_input.split('\n\n')]


def parse_tile(tile):
    head, _, image = tile.partition('\n')
    tid = int(re.match(r'^Tile (\d+):', head).group(1))
    return tid, image.split('\n')


def parse(chunks: List[str]):
    return dict(parse_tile(tile) for tile in chunks)


def part1(puzzle):
    return puzzle


def part2(puzzle):
    return len(puzzle)


if __name__ == '__main__':
    puzzle_input = load(input_file)
    input_records = parse(chop(puzzle_input))

    start = time.perf_counter()
    print('part 1:', part1(input_records), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(input_records), 'time', round(time.perf_counter() - start, 4))
