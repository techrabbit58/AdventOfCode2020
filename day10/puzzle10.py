"""
Advent Of Code 2020, Day 10.
https://adventofcode.com/2020/day/10
"""
import time
from collections import defaultdict, Counter

input_file = 'smallinput.txt'


def load(fn):
    with open(fn) as fh:
        puzzle = [int(n) for n in fh.read().strip().split('\n')]
    return puzzle


def part1a(puzzle):
    target_jolt = max(puzzle) + 3
    input_rating = defaultdict(set)
    for jolt in puzzle + [target_jolt]:
        for d in range(1, 4):
            if d <= jolt:
                input_rating[jolt - d].add(jolt)
    jolt = 0
    deltas = Counter()
    used = []
    while jolt < target_jolt:
        new_jolt = min(input_rating[jolt])
        used.append(new_jolt)
        deltas[new_jolt - jolt] += 1
        jolt = new_jolt
    return deltas[1] * deltas[3]


def part1b(puzzle):
    adapters = [0] + sorted(puzzle) + [max(puzzle) + 3]
    deltas = Counter()
    for p in range(len(adapters) - 1):
        deltas[adapters[p + 1] - adapters[p]] += 1
    return deltas[1] * deltas[3]


def part2(puzzle):
    adapters = [0] + sorted(puzzle) + [max(puzzle) + 3]
    input_rating = defaultdict(list)
    for jolt in adapters:
        for d in range(1, 4):
            ir = jolt - d
            if ir in adapters:
                input_rating[ir].append(jolt)
    print(input_rating)
    return len(puzzle)


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    print('part 1:', part1b(puzzle_input), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time', round(time.perf_counter() - start, 4))
