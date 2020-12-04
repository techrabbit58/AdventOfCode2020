"""
Advent Of Code 2020. Day 4.
3rd approach making extensive use of regular expressions for part 2.
Plus: try to optimize complex rule evaluation for part 2.
"""
import time
import re

input_file = 'input04.txt'
required_fields = set('byr iyr eyr hgt hcl ecl pid cid'.split())


def parse(fn):
    with open(fn) as fh:
        puzzle = fh.read().split('\n\n')
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


yr = re.compile(r'\d\d\d\d')
hgt = re.compile(r'(\d+)(cm|in)')
hcl = re.compile(r'#[0-9a-f]{6}')
ecl = re.compile(r'(amb|blu|brn|gry|grn|hzl|oth)')
pid = re.compile(r'\d{9}')


def as_year(s):
    return int(s) if yr.fullmatch(s) else -1


def as_valid_hgt(s):
    m = hgt.fullmatch(s)
    return (int(m.group(1)), m.group(2)) if m else (-1, '')


def part2(puzzle):
    result = 0
    for passport in puzzle:
        fields = analyze(passport)
        if not len(required_fields - set(fields.keys()) - {'cid'}):
            hgt_v, hgt_u = as_valid_hgt(fields['hgt'])
            if any((not 1920 <= as_year(fields['byr']) <= 2002,
                    not 2010 <= as_year(fields['iyr']) <= 2020,
                    not 2020 <= as_year(fields['eyr']) <= 2030,
                    hgt_u == 'cm' and not 150 <= hgt_v <= 193,
                    hgt_u == 'in' and not 59 <= hgt_v <= 76,
                    not hgt_u,
                    not hcl.fullmatch(fields['hcl']),
                    not ecl.fullmatch(fields['ecl']),
                    not pid.fullmatch(fields['pid']))):
                continue
            result += 1
    return result


if __name__ == '__main__':
    puzzle_input = parse(input_file)

    start = time.perf_counter()
    print(part1(puzzle_input), round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print(part2(puzzle_input), round(time.perf_counter() - start, 4))
