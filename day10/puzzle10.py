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


def part1(puzzle):
    deltas = Counter(p - q for p, q in zip(puzzle[1:], puzzle))
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


def as_rating_graph(adapters):
    input_rating = defaultdict(list)
    for jolt in adapters:
        for d in range(1, 4):
            ir = jolt - d
            if ir in adapters:
                input_rating[ir].append(jolt)
    return input_rating


def part2(puzzle):
    return count_paths(0, puzzle[-1], as_rating_graph(puzzle))


if __name__ == '__main__':
    puzzle_input = load(input_file)
    jolt_list = [0] + sorted(puzzle_input) + [max(puzzle_input) + 3]

    start = time.perf_counter()
    print('part 1:', part1(jolt_list), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(jolt_list), 'time', round(time.perf_counter() - start, 4))
