"""
Advent Of Code 2020.
Day 5.
"""
import time

input_file = 'input05.txt'


def parse(fn):
    with open(fn) as fh:
        puzzle = fh.read().strip().split('\n')
    return puzzle


def part1(puzzle):
    result = puzzle
    return result


def part2(puzzle):
    result = puzzle
    return result


if __name__ == '__main__':
    puzzle_input = parse(input_file)

    start = time.perf_counter()
    print('part 1:', part1(puzzle_input), 'time', time.perf_counter() - start)

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time', time.perf_counter() - start)
