"""
Advent Of Code 2020. Day 4.
"""
import time

input_file = 'input04.txt'
required_fields = set('byr iyr eyr hgt hcl ecl pid cid'.split())


def parse(puzzle_input):
    with open(puzzle_input) as f:
        puzzle_ = f.read().split('\n\n')
    return puzzle_


def analyze(passport):
    kv_pairs = {}
    for field in passport.split():
        key, _, value = field.partition(':')
        kv_pairs[key] = value
    return kv_pairs


def part1(puzzle_):
    result = 0
    for passport in puzzle_:
        fields = analyze(passport)
        if not len(required_fields - set(fields.keys()) - {'cid'}):
            result += 1
    return result


def part2(puzzle_):
    result = 0
    for passport in puzzle_:
        fields = analyze(passport)
        if not len(required_fields - set(fields.keys()) - {'cid'}):
            if not 1920 <= int(fields['byr']) <= 2002:
                continue
            if not 2010 <= int(fields['iyr']) <= 2020:
                continue
            if not 2020 <= int(fields['eyr']) <= 2030:
                continue
            hgt_v, hgt_u = fields['hgt'][:-2], fields['hgt'][-2:]
            if hgt_u == 'cm' and not 150 <= int(hgt_v) <= 193:
                continue
            elif hgt_u == 'in' and not 59 <= int(hgt_v) <= 76:
                continue
            elif hgt_u not in {'in', 'cm'}:
                continue
            hcl = fields['hcl']
            if not (hcl[0] == '#' and len(hcl) == 7 and set(hcl[1:].lower()).issubset(set('0123456789abcdef'))):
                continue
            if fields['ecl'] not in set('amb blu brn gry grn hzl oth'.split()):
                continue
            pid = fields['pid']
            if not (len(pid) == 9 and pid.isdecimal()):
                continue
            result += 1
    return result


if __name__ == '__main__':
    puzzle = parse(input_file)

    start = time.perf_counter()
    print(part1(puzzle), round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print(part2(puzzle), round(time.perf_counter() - start, 4))
