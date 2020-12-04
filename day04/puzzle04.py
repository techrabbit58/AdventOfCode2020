"""
Advent Of Code 2020. Day 4. Puzzle 1.
"""
import time

input_file = 'input04.txt'
required_fields = set('byr iyr eyr hgt hcl ecl pid cid'.split())


def parse(puzzle_input):
    with open(puzzle_input) as f:
        k = 7
        puzzle = [s.replace('$' * k, ' ') for s in f.read().replace('\n', '$' * k).split('$' * 2 * k)]
    return puzzle


def analyze(passport):
    kv_pairs = {}
    for field in passport.split():
        key, _, value = field.partition(':')
        kv_pairs[key] = value
    return kv_pairs


def part1(puzzle):
    result = 0
    for passport in puzzle:
        fields = analyze(passport)
        if not len(required_fields - set(fields.keys()) - {'cid'}):
            result += 1
    return result


def part2(puzzle):
    result = 0
    for passport in puzzle:
        fields = analyze(passport)
        if not len(required_fields - set(fields.keys()) - {'cid'}):
            result += 1
    return result


if __name__ == '__main__':
    puzzle = parse(input_file)
    start = time.perf_counter()
    print(part1(puzzle), time.perf_counter() - start)
    start = time.perf_counter()
    print(part2(puzzle), time.perf_counter() - start)
