"""
Advent Of Code 2020, Day 15.
https://adventofcode.com/2020/day/15
"""
import time
from collections import defaultdict


def prepare():
    # return [1, 0, 15, 2, 10, 13]
    return [0, 3, 6]


def part1(puzzle, stop=2020):
    spoken = defaultdict(list)
    sequence = puzzle[:]
    last = None
    for turn, number in enumerate(puzzle, 1):
        spoken[number].append(turn)
        last = number
    for turn in range(len(puzzle) + 1, stop + 1):
        if len(spoken[last]) <= 1:
            this = 0
        else:
            this = spoken[last][-1] - spoken[last][-2]
        spoken[this].append(turn)
        last = this
        sequence.append(last)
    return last, sequence


def part2(sequence, stop=30000000):
    return stop, sequence


if __name__ == '__main__':
    input_records = prepare()

    start = time.perf_counter()
    last, sequence = part1(input_records)
    print('part 1:', last, 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(sequence), 'time', round(time.perf_counter() - start, 4))
