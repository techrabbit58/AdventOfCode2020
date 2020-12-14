"""
Advent Of Code 2020, Day 14.
https://adventofcode.com/2020/day/14
"""
import re
import time
from itertools import combinations

input_file = 'input14.txt'


def load(fn):
    with open(fn) as fh:
        return fh.read().strip()


def prepare(raw_input):
    return raw_input.split('\n')


class Computer:
    def __init__(self):
        self.mask = {}
        self.mem = {}

    def __repr__(self):
        return f'{self.__class__.__name__}(mask={self.mask}, mem={self.mem})'


parse_mask = re.compile(r'mask = ([01X]{36})')
parse_mem = re.compile(r'mem\[(\d+)] = (\d+)')

MEM = 'mem'
MASK = 'mask'


def decode(line):
    if line.startswith('mem'):
        args = parse_mem.match(line)
        return MEM, (int(args[1]), int(args[2]))
    elif line.startswith('mask'):
        args = parse_mask.match(line)
        mask = {35 - n: int(bit) for n, bit in enumerate(args[1]) if bit in '01'}
        return MASK, mask
    else:
        raise ValueError(f'ERROR - unknown instruction: "{line}".')


def part1(puzzle):
    computer = Computer()
    for line in puzzle:
        operation, operands = decode(line)
        if operation == MASK:
            computer.mask = operands
        else:
            address, arg = operands
            for bit, value in computer.mask.items():
                arg = arg | (1 << bit) if value else arg & ~(1 << bit)
            computer.mem[address] = arg
    return sum(computer.mem.values())


def apply_rules(address, mask):
    floating = []
    for bit in range(36):
        value = mask.get(bit, 'X')
        if value == 1:
            address |= (1 << bit)
        elif value == 'X':
            floating.append(bit)
    return address, floating


def bitmask_from(bits):
    m = 0
    for bit in bits:
        m += (1 << bit)
    return m


def bit_combinations(bits):
    for num_bits in range(len(bits) + 1):
        for bit_set in combinations(bits, num_bits):
            yield bit_set


def set_bits(address, bits):
    for bit in bits:
        address |= (1 << bit)
    return address


def part2(puzzle):
    computer = Computer()
    for line in puzzle:
        operation, operands = decode(line)
        if operation == MASK:
            computer.mask = operands
        else:
            address, arg = operands
            address, floating = apply_rules(address, computer.mask)
            m = bitmask_from(floating)
            affected = [set_bits(address & ~m, bits) for bits in bit_combinations(floating)]
            for a in affected:
                computer.mem[a] = arg
    return sum(computer.mem.values())


if __name__ == '__main__':
    puzzle_input = load(input_file)
    input_records = prepare(puzzle_input)

    start = time.perf_counter()
    print('part 1:', part1(input_records), 'time', round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(input_records), 'time', round(time.perf_counter() - start, 4))
