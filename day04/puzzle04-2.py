"""
Advent Of Code 2020. Day 4. Puzzle 2.
"""
import time

input_file = 'input04.txt'


def parse(puzzle_input):
    with open(puzzle_input) as f:
        puzzle = f.read().strip().split('\n')
    return puzzle


def solution(puzzle):
    result = puzzle
    return result


if __name__ == '__main__':
    puzzle = parse(input_file)
    start = time.perf_counter()
    print(solution(puzzle), time.perf_counter() - start)
