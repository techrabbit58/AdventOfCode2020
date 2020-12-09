"""
Advent Of Code 2020.
Day 9.
"""
import time

input_file = 'input09.txt'
PREAMBLE = 25


def load(fn):
    with open(fn) as fh:
        puzzle = [int(n) for n in fh.read().strip().split('\n')]
    return puzzle


def part1(puzzle):
    for p in range(PREAMBLE, len(puzzle)):
        candidate = puzzle[p]
        a = set(puzzle[p - PREAMBLE:p])
        b = {candidate - x for x in a if x << 1 != candidate}
        if not a.intersection(b):
            return candidate, p
    return None


def part2(puzzle, i):
    weak_number = puzzle[i]
    remaining = puzzle[:i]
    for p in range(i):
        for q in range(2, i - p):
            subset = remaining[p:p + q]
            s = sum(subset)
            if s == weak_number:
                subset.sort()
                return subset[0] + subset[-1]
            if s > weak_number:
                break
    return None


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    weak_number, index = part1(puzzle_input)
    print('part 1:', weak_number, 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input, index), 'time', round(time.perf_counter() - start, 4))
