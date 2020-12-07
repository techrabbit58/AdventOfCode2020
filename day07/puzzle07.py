"""
Advent Of Code 2020.
Day 7.
"""
import time
import re
from collections import defaultdict

input_file = 'input07.txt'

my_bag = 'shiny gold'

colors = re.compile(r'\d+ (\w+ \w+) bag[s]?[.,]')
counts = re.compile(r'(\d+) (\w+ \w+) bag[s]?[.,]')


def load(fn):
    with open(fn) as fh:
        puzzle = fh.read().strip().split('\n')
    return puzzle


def parse(puzzle):
    parents_ = defaultdict(set)
    children_ = {}
    for sentence in puzzle:
        outer, _, other = sentence.partition(' bags contain ')
        content, rules = colors.findall(other), counts.findall(other)
        if content:
            for color in content:
                parents_[color].add(outer)
            children_[outer] = [(int(n), c) for n, c in rules]
    return parents_, children_


def find_all_parents(parents_graph, child, color_bag):
    parents = parents_graph.get(child)
    if not parents:
        return color_bag
    for parent in parents:
        color_bag = find_all_parents(parents_graph, parent, color_bag).union({parent})
    return color_bag


def count_all_children(children_graph, parent, counters):
    children = children_graph.get(parent)
    if not children:
        return counters
    for num, child in children:
        counters += [num] + num * count_all_children(children_graph, child, [])
    return counters


def part1(parents_, my_bag_):
    return len(find_all_parents(parents_, my_bag_, set()))


def part2(children_, my_bag_):
    return sum(count_all_children(children_, my_bag_, []))


if __name__ == '__main__':
    puzzle_input = load(input_file)
    parents, children = parse(puzzle_input)

    start = time.perf_counter()
    print('part 1:', part1(parents, my_bag), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(children, my_bag), 'time', round(time.perf_counter() - start, 4))
