"""
Advent Of Code 2020.
Day 7.
"""
import time
import re
from collections import defaultdict

input_file = 'test07.txt'
# input_file = 'input07.txt'


def load(fn):
    with open(fn) as fh:
        puzzle = fh.read().strip().split('\n')
    return puzzle


my_bag = 'shiny gold'
colors = re.compile(r'\d+ (\w+ \w+) bag[s]?[.,]')


def parse(puzzle):
    parents = defaultdict(set)
    for sentence in puzzle:
        outer, _, other = sentence.partition(' bags contain ')
        content = colors.findall(other)
        if content:
            for color in content:
                parents[color].add(outer)
    return parents


def part1(puzzle):
    parents = parse(puzzle)
    containers = parents[my_bag]
    for item in containers:
        if containers.intersection(children):
            containers.add(parent)
    print(containers)
    result = len(puzzle)
    return result


def part2(puzzle):
    result = puzzle
    return result


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    print('part 1:', part1(puzzle_input), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time', round(time.perf_counter() - start, 4))
