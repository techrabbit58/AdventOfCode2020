"""
Advent Of Code 2020. Day 4. Puzzle 2.
"""
import time

input_file = 'input04.txt'


def parse(puzzle_input):
    puzzle = None
    with open(puzzle_input) as f:
        puzzle = f.read().strip().split('\n')
    return puzzle


def solution(puzzle_input):
    puzzle = parse(puzzle_input)
    result = None
    return result


if __name__ == '__main__':
    start = time.perf_counter()
    print(solution(input_file), time.perf_counter() - start)
