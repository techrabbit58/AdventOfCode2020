"""
Advent Of Code 2020, Day 13.
https://adventofcode.com/2020/day/13
Instead of 2D vectors, complex numbers can be used.
"""
import time

input_file = '../day13/input13.txt'


def load(fn):
    with open(fn) as fh:
        puzzle = [(ins[0], int(ins[1:])) for ins in fh.read().strip().split('\n')
    return puzzle


def part1(puzzle):
    position = 0
    heading = 1
    for action, value in puzzle:
        pass
    return puzzle


def part2(puzzle):
    return len(puzzle)


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    print('part 1:', part1(puzzle_input), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time', round(time.perf_counter() - start, 4))
