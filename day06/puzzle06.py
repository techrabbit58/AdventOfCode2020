"""
Advent Of Code 2020.
Day 6.
"""
import time

input_file = 'input06.txt'


def load(fn):
    with open(fn) as fh:
        puzzle = [group.split('\n') for group in fh.read().strip().split('\n\n')]
    return puzzle


def part1(puzzle):
    result = 0
    for group in puzzle:
        answers = set(group[0])
        answers.update(*group[1:])
        result += len(answers)
    return result


def part2(puzzle):
    result = 0
    for group in puzzle:
        answers = set(group[0])
        answers.intersection_update(*group[1:])
        result += len(answers)
    return result


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    print('part 1:', part1(puzzle_input), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time', round(time.perf_counter() - start, 4))
