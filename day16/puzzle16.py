"""
Advent Of Code 2020, Day 16.
https://adventofcode.com/2020/day/16
"""
import time

input_file = 'input16.txt'


def load(fn):
    with open(fn) as fh:
        return fh.read().strip()


def prepare(raw_input):
    return [line for line in raw_input.split('\n')]


def part1(puzzle):
    return puzzle


def part2(puzzle):
    return len(puzzle)


if __name__ == '__main__':
    puzzle_input = load(input_file)
    input_records = prepare(puzzle_input)

    start = time.perf_counter()
    print('part 1:', part1(input_records), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(input_records), 'time', round(time.perf_counter() - start, 4))
