"""
Advent Of Code 2020. Day 4.
2nd approach making extensive use of regular expressions for part 2.
"""
import time
import re

input_file = 'input04.txt'
required_fields = set('byr iyr eyr hgt hcl ecl pid cid'.split())


def parse(puzzle_input):
    with open(puzzle_input) as f:
        puzzle = f.read().split('\n\n')
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
            if not 1920 <= as_year(fields['byr']) <= 2002:
                continue
            if not 2010 <= as_year(fields['iyr']) <= 2020:
                continue
            if not 2020 <= as_year(fields['eyr']) <= 2030:
                continue
            hgt_v, hgt_u = as_valid_hgt(fields['hgt'])
            if hgt_u == 'cm' and not 150 <= hgt_v <= 193:
                continue
            elif hgt_u == 'in' and not 59 <= hgt_v <= 76:
                continue
            elif not hgt_u:
                continue
            if not hcl.fullmatch(fields['hcl'].lower()):
                continue
            if not ecl.fullmatch(fields['ecl'].lower()):
                continue
            if not pid.fullmatch(fields['pid']):
                continue
            result += 1
    return result


if __name__ == '__main__':
    puzzle_ = parse(input_file)

    start = time.perf_counter()
    print(part1(puzzle_), round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print(part2(puzzle_), round(time.perf_counter() - start, 4))
