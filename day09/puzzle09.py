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
    return None, None


def part2(puzzle, i):
    weak_number = puzzle[i]
    for p in range(i - 1):
        q, subset = 2, puzzle[p:p + 2]
        total = sum(subset)
        while total < weak_number:
            subset.append(puzzle[p + q])
            total += subset[-1]
            q += 1
        if total == weak_number:
            return min(subset) + max(subset)
    return None


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    weak_number, index = part1(puzzle_input)
    print('part 1:', weak_number, 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input, index), 'time', round(time.perf_counter() - start, 4))
