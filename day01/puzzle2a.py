"""
Advent Of Code 2020. Day 01. Puzzle 2.
Find, from a set of numbers, the three numbers that, when added,
give 2020 as a result.
Return the product of these three numbers.
"""
import time
from itertools import combinations

puzzle_input = 'day01.txt'


def solution(puzzle_input: str):
    with open(puzzle_input) as f:
        numbers = sorted([int(x) for x in f.read().strip().split()])
    for triple in combinations(numbers, 3):
        if sum(triple) == 2020:
            result = triple[0] * triple[1] * triple[2]
            break
    return result


if __name__ == '__main__':
    start = time.perf_counter()
    print(solution(puzzle_input), time.perf_counter() - start)
