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
    return int(eta), [(0 if bid == 'x' else int(bid)) for bid in schedule.split(',')]


def part1(puzzle):
    eta, buses = puzzle
    buses = [bus for bus in buses if bus != 0]
    a, b = min(zip(
        buses, [bus - (eta + bus) % bus for bus in buses]), key=lambda x: x[1])
    return a * b


def part2(puzzle, start_time):
    _, buses = puzzle
    requirement = [(-offset, bus) for offset, bus in enumerate(buses[1:], 1) if bus]
    tick = buses[0]
    t = start_time - start_time % tick
    state = [((t % bus) - bus, bus) for offset, bus in enumerate(buses[1:], 1) if bus]
    while state != requirement:
        state = [(((offset + tick) % bus - bus), bus) for offset, bus in state]
        t += tick
    return t


if __name__ == '__main__':
    puzzle_input = load(input_file)
    test = """939
7,13,x,x,59,x,31,19"""
    input_records = prepare(test)

    start = time.perf_counter()
    print('part 1:', part1(input_records), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(input_records, 1000000),
          'time', round(time.perf_counter() - start, 4))
