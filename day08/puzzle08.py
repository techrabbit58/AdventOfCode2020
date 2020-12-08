"""
Advent Of Code 2020.
Day 8.
"""
import time
import re

input_file = 'input08.txt'

decoder = re.compile(r'(nop|acc|jmp) ([+-]\d+)*')


def load(fn):
    with open(fn) as fh:
        puzzle = [(op, int(arg)) for op, arg in decoder.findall(fh.read().strip())]
    return puzzle


interpret = dict(
    nop=lambda ip, a, arg: (ip + 1, a),
    acc=lambda ip, a, arg: (ip + 1, a + arg),
    jmp=lambda ip, a, arg: (ip + arg, a)
)


def run(code):
    ip, a, seen = 0, 0, set()
    if not len(code):
        return 0, 'Skip.'
    while ip < len(code):
        seen.add(ip)
        op, arg = code[ip]
        ip, a = interpret[op](ip, a, arg)
        if ip in seen:
            return a, '*break*'
    return a, 'Done.'


def part1(code):
    return run(code)


def patch(code, mem_loc):
    op, arg = code[mem_loc]
    if op not in {'jmp', 'nop'}:
        return []
    code_copy = code[:]
    code_copy[mem_loc] = ('jmp' if op == 'nop' else 'nop', arg)
    return code_copy


def part2(code):
    result = reason = None
    for mem_loc in range(len(code)):
        result, reason = run(patch(code, mem_loc))
        if reason == 'Done.':
            break
    return result, reason


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    print('part 1:', part1(puzzle_input), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time', round(time.perf_counter() - start, 4))
