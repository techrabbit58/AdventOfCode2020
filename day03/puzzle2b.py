"""
Advent Of Code 2020. Day 03. Puzzle 2.
2nd approach, just to see if this may be faster.
It turns out, the first approach had been at least 3 times faster.
This second approach is slower. Hummm!
"""
import time

input_file = 'day03.txt'


TREE = '#'
SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def parse(puzzle_input):
    positions = set()
    height, width = 0, 0 
    with open(puzzle_input) as f:
        for y, line in enumerate(f):
            height, width = y + 1, len(line)
            for x, ch in enumerate(line):
                if ch == TREE:
                    positions.add((x, y))
    return positions, height, width


def trajectory(forest, height, width, slope):
    count, x = 0, 0
    dx, dy = slope
    for y in range(0, height, dy):
        if (x, y) in forest:
            count += 1
        x = (x + dx) % width
    return count


def solution(puzzle_input):
    forest, height, tile_width = parse(puzzle_input)
    hit_count = 1
    for slope in SLOPES:
        hit_count *= trajectory(forest, height, tile_width, slope)
    return hit_count


if __name__ == '__main__':
    start = time.perf_counter()
    print(solution(input_file), time.perf_counter() - start)
