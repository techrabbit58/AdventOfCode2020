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


mask_decode = re.compile(r'mask = ([01X]{36})')
mem_decode = re.compile(r'mem\[(\d+)] = (\d+)')

MEM = 'mem'
MASK = 'mask'


class Computer:
    def __init__(self):
        self.mask = {}
        self.mem = {}

    def __repr__(self):
        return f'{self.__class__.__name__}(mask={self.mask}, mem={self.mem})'


def decode(line):
    if line.startswith('mem'):
        args = mem_decode.match(line)
        return MEM, (int(args[1]), int(args[2]))
    elif line.startswith('mask'):
        args = mask_decode.match(line)
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


def part2(puzzle):
    computer = Computer()
    for line in puzzle:
        operation, operands = decode(line)
        if operation == MASK:
            computer.mask = operands
        else:
            address, arg = operands
            floating = []
            for bit in range(36):
                value = computer.mask.get(bit, 'X')
                if value == 0:
                    pass
                elif value == 1:
                    address |= (1 << bit)
                else:
                    floating.append(bit)
            m = 0
            for bit in floating:
                m += (1 << bit)
            affected = []
            for num_bits in range(len(floating) + 1):
                for bit_set in combinations(floating, num_bits):
                    address &= ~m
                    for bit in bit_set:
                        address |= (1 << bit)
                    affected.append(address)
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
