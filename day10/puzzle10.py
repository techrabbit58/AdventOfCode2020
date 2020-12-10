"""
Advent Of Code 2020, Day 10.
https://adventofcode.com/2020/day/10
"""
import time
from collections import defaultdict, Counter

input_file = 'input10.txt'


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


known_jolt = {}


def count_paths(jolt, target_jolt, ratings):
    if jolt > target_jolt:
        return 0
    if jolt == target_jolt:
        return 1
    if jolt in known_jolt:
        return known_jolt[jolt]
    path_count = 0
    for next_jolt in ratings[jolt]:
        path_count += count_paths(next_jolt, target_jolt, ratings)
    known_jolt[jolt] = path_count
    return path_count


def part2(puzzle):
    target_jolt = max(puzzle) + 3
    adapters = [0] + sorted(puzzle) + [target_jolt]
    input_rating = defaultdict(list)
    for jolt in adapters:
        for d in range(1, 4):
            ir = jolt - d
            if ir in adapters:
                input_rating[ir].append(jolt)
    return count_paths(0, target_jolt, input_rating)


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    print('part 1:', part1b(puzzle_input), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time', round(time.perf_counter() - start, 4))
