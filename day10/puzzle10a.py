"""
Advent Of Code 2020, Day 10.
https://adventofcode.com/2020/day/10
This is a tribute to the stunning solution of Gravitar64.
https://https://github.com/Gravitar64
"""
import time

input_file = 'input10.txt'


def load(fn):
    with open(fn) as fh:
        puzzle = [int(n) for n in fh.read().strip().split('\n')]
    return puzzle


def part1(puzzle):
    deltas = ''.join(str(p - q) for p, q in zip(puzzle[1:], puzzle))
    return deltas.count('1') * deltas.count('3'), deltas


def part2(deltas):
    deltas = deltas.replace('1111', 'c').replace('111', 'b').replace('11', 'a')
    return 2 ** deltas.count('a') * 4 ** deltas.count('b') * 7 ** deltas.count('c')


if __name__ == '__main__':
    puzzle_input = load(input_file)
    jolt_list = [0] + sorted(puzzle_input) + [max(puzzle_input) + 3]

    start = time.perf_counter()
    result1, diff_string = part1(jolt_list)
    print('part 1:', result1, 'time', round(time.perf_counter() - start, 6))

    start = time.perf_counter()
    print('part 2:', part2(diff_string), 'time', round(time.perf_counter() - start, 6))
