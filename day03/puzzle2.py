"""
Advent Of Code 2020. Day 03. Puzzle 2.
"""
import time

input_file = 'day03.txt'


TREE = '#'
SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def parse(puzzle_input):
    with open(puzzle_input) as f:
        lines = f.read().strip().split()
    return lines


def solution(puzzle_input):
    forest = parse(puzzle_input)
    width = len(forest[0])
    result = 1
    for x_step, y_step in SLOPES:
        trees = 0
        x_pos = y_pos = 0
        while y_pos < len(forest):
            if forest[y_pos][x_pos] == TREE:
                trees += 1
            x_pos, y_pos = (x_pos + x_step) % width, y_pos + y_step
        result *= trees
    return result


if __name__ == '__main__':
    start = time.perf_counter()
    print(solution(input_file), time.perf_counter() - start)
