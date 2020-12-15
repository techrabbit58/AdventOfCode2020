"""
Advent Of Code 2020, Day 15.
https://adventofcode.com/2020/day/15
"""
import time
from collections import defaultdict


def prepare():
    """
    Given 0,3,6, the 30000000th number spoken is 175594.
    Given 1,3,2, the 30000000th number spoken is 2578.
    Given 2,1,3, the 30000000th number spoken is 3544142.
    Given 1,2,3, the 30000000th number spoken is 261214.
    Given 2,3,1, the 30000000th number spoken is 6895259.
    Given 3,2,1, the 30000000th number spoken is 18.
    Given 3,1,2, the 30000000th number spoken is 362.
    """
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


def part2(puzzle, sequence, stop=30000000):
    print(puzzle)
    return stop, sequence


if __name__ == '__main__':
    input_records = prepare()

    start = time.perf_counter()
    last, sequence = part1(input_records)
    print('part 1:', last, 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(input_records, sequence), 'time', round(time.perf_counter() - start, 4))
