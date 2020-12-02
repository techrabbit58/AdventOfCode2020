"""
Advent Of Code 2020. Day 01. Puzzle 2.
Find, from a set of numbers, the three numbers that, when added,
give 2020 as a result.
Return the product of these three numbers.
"""
import time

input_file = 'day01.txt'


def solution(puzzle_input: str):
    with open(puzzle_input) as f:
        numbers = sorted([int(x) for x in f.read().strip().split()])
    result = None
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers[i + 1:]):
            c = 2020 - a - b
            if c in numbers:
                result = a * b * c
    return result


if __name__ == '__main__':
    start = time.perf_counter()
    print(solution(input_file), time.perf_counter() - start)
