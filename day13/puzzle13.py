"""
Advent Of Code 2020, Day 13.
https://adventofcode.com/2020/day/13
"""
import time

input_file = 'input13.txt'


def load(fn):
    with open(fn) as fh:
        puzzle = fh.read().strip().split('\n')
    return puzzle


def part1(puzzle):
    return puzzle


def part2(puzzle):
    return len(puzzle)


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    print('part 1:', part1(puzzle_input), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time', round(time.perf_counter() - start, 4))
