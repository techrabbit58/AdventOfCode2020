"""
Advent Of Code 2020. Day 03. Puzzle 1.
"""
import time

input_file = 'day03.txt'


def parse(puzzle_input):
    with open(puzzle_input) as f:
        lines = f.read().strip().split()
    return lines


TREE = '#'


def solution(puzzle_input):
    forest = parse(puzzle_input)
    width = len(forest[0])
    x_pos = 0
    x_step = 3
    trees = 0
    for n, row in enumerate(forest, 1):
        if row[x_pos] == TREE:
            trees += 1
        x_pos = (x_pos + x_step) % width
    return trees


if __name__ == '__main__':
    start = time.perf_counter()
    print(solution(input_file), time.perf_counter() - start)
