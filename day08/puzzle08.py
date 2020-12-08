"""
Advent Of Code 2020.
Day 8.
"""
import time
import re
import enum

input_file = 'input08.txt'


class OpCode(enum.IntEnum):
    NOP = 0
    JMP = 1
    ACC = 2


decoder = re.compile(r'(nop|acc|jmp) ([+-]\d+)')


def load(fn):
    with open(fn) as fh:
        puzzle = [(OpCode[op.upper()], int(arg))
                  for op, arg in decoder.findall(fh.read().strip())]
    return puzzle


interpret = {
    OpCode.NOP: lambda ip, a, arg: (ip + 1, a),
    OpCode.ACC: lambda ip, a, arg: (ip + 1, a + arg),
    OpCode.JMP: lambda ip, a, arg: (ip + arg, a)
}


class ReasonCode(enum.IntEnum):
    DONE = 1
    SKIP = 2
    BREAK = 3


def run(code):
    ip, a, already_seen = 0, 0, set()
    if not len(code):
        return 0, ReasonCode.SKIP
    while ip < len(code):
        already_seen.add(ip)
        op, arg = code[ip]
        ip, a = interpret[op](ip, a, arg)
        if ip in already_seen:
            return a, ReasonCode.BREAK
    return a, ReasonCode.DONE


def part1(code):
    return run(code)


def patch(code, mem_loc):
    op, arg = code[mem_loc]
    if op not in {OpCode.NOP, OpCode.JMP}:
        return []
    code_copy = code[:]
    code_copy[mem_loc] = (OpCode.JMP if op == OpCode.NOP else OpCode.NOP, arg)
    return code_copy


def part2(code):
    result = reason = None
    for mem_loc in range(len(code)):
        result, reason = run(patch(code, mem_loc))
        if reason == ReasonCode.DONE:
            break
    return result, reason


if __name__ == '__main__':
    puzzle_input = load(input_file)

    start = time.perf_counter()
    print('part 1:', part1(puzzle_input), 'time',
          round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    print('part 2:', part2(puzzle_input), 'time',
          round(time.perf_counter() - start, 4))
