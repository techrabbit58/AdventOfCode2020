"""
Advent Of Code 2020, Day 13.
https://adventofcode.com/2020/day/13
"""
import time

input_file = 'input13.txt'


def load(fn):
    with open(fn) as fh:
        return fh.read().strip()


def prepare(raw_input):
    eta, _, schedule = raw_input.partition('\n')
    return int(eta), [int(id) for id in schedule.split(',') if id != 'x']


def part1(puzzle):
    eta, buses = puzzle
    a, b = min(zip(buses, [bid - (eta + bid) % bid for bid in buses]), key=lambda x: x[1])
    return a * b


def part2(puzzle):
    _, buses = puzzle
    return buses


if __name__ == '__main__':
    puzzle_input = load(input_file)
    test = """939
7,13,x,x,59,x,31,19"""
    input_records = prepare(puzzle_input)

    start = time.perf_counter()
    print('part 1:', part1(input_records), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(input_records), 'time', round(time.perf_counter() - start, 4))
