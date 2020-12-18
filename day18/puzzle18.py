"""
Advent Of Code 2020, Day 18.
https://adventofcode.com/2020/day/18
"""
import time

input_file = 'input18.txt'


def load(fn):
    with open(fn) as fh:
        return fh.read().strip()


def prepare(raw_input):
    return [line for line in raw_input.split('\n')]


def simple(expr):
    n_stack = []
    o_stack = []
    while expr:
        ch, expr = expr[0], expr[1:]
        if ch == ' ':
            continue
        if ch == '(':
            n, expr = simple(expr)
            if o_stack:
                n_stack.append(o_stack.pop()(n_stack.pop(), n))
            else:
                n_stack.append(n)
        elif ch == ')':
            return n_stack[0], expr
        elif ch in '123456789':
            if o_stack:
                n_stack.append(o_stack.pop()(n_stack.pop(), int(ch)))
            else:
                n_stack.append(int(ch))
        elif ch == '+':
            o_stack.append(lambda a, b: a + b)
        elif ch == '*':
            o_stack.append(lambda a, b: a * b)
    return n_stack[0], expr


level = 0, None


def advanced(expr):
    global level
    n_stack = []
    o_stack = []
    print('level', level)
    while expr:
        ch, expr = expr[0], expr[1:]
        if ch == ' ':
            continue
        if ch == '(':
            n, expr = advanced(expr)
            if o_stack:
                n_stack.append(o_stack.pop()(n_stack.pop(), n))
            else:
                n_stack.append(n)
        elif ch == ')':
            return n_stack[0], expr
        elif ch in '123456789':
            if o_stack:
                n_stack.append(o_stack.pop()(n_stack.pop(), int(ch)))
            else:
                n_stack.append(int(ch))
        elif ch == '+':
            o_stack.append(lambda a, b: a + b)
        elif ch == '*':
            n, expr = advanced(expr)
            n_stack.append(n_stack.pop() * n)
    return n_stack[0], expr


def solution(puzzle, method):
    result = 0
    for line in puzzle:
        n, _ = method(line)
        result += n
    return result


if __name__ == '__main__':
    puzzle_input = load(input_file)
    input_records = prepare(puzzle_input)

    start = time.perf_counter()
    print('part 1:', solution(input_records, simple), 'time', round(time.perf_counter() - start, 4))

    # assert advanced('1 + 2 * 3 + 4 * 5 + 6') == (231, '')
    # assert advanced('1 + (2 * 3) + (4 * (5 + 6))') == (51, '')
    # assert advanced('2 * 3 + (4 * 5)') == (46, '')
    # assert advanced('5 + (8 * 3 + 9 + 3 * 4 * 3)') == (1445, '')
    # assert advanced('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == (669060, '')
    print(advanced('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 23340)

    # start = time.perf_counter()
    # print('part 2:', solution(input_records, advanced), 'time', round(time.perf_counter() - start, 4))
