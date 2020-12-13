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
    arrival_time, buses = puzzle
    buses = [bus for bus in buses if bus != 0]
    a, b = min(zip(
        buses, [bus - (arrival_time + bus) % bus for bus in buses]), key=lambda x: x[1])
    return a * b


def part2(puzzle, start_time):
    _, buses = puzzle
    requirement = {(offset if offset else bus, bus)
                   for offset, bus in enumerate(buses[1:], 1) if bus}
    tick = buses[0]
    t = start_time - start_time % tick
    state = {(bus - t % bus, bus) for offset, bus in enumerate(buses[1:], 1) if bus}
    while state != requirement:
        t += tick
        state = {(bus - t % bus, bus) for offset, bus in state}
        if t % 1000000 == 1:
            print(t)
    return t


def crt(pairs):
    """
    After 8 hours of pointless optimizing, I searched for a good solution
    and finally found this from "sophiebits". She made a nice and lightning fast
    implementation of the Chinese Remainder Theorem. Please, follow the link
    to her original solution devoutly:
    https://github.com/sophiebits/adventofcode/blob/main/2020/day13.py
    """
    m = 1
    for x, mx in pairs:
        m *= mx
    total = 0
    for x, mx in pairs:
        b = m // mx
        total += x * b * pow(b, mx-2, mx)
        total %= m
    return total


def part2b(puzzle):
    _, buses = puzzle
    return crt([(bus - offset, bus) for offset, bus in enumerate(buses) if bus])


if __name__ == '__main__':
    puzzle_input = load(input_file)
    input_records = prepare(puzzle_input)

    start = time.perf_counter()
    print('part 1:', part1(input_records), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2b(input_records), 'time', round(time.perf_counter() - start, 4))
