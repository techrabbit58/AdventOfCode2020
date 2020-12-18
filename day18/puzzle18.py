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


def find_closing_paren(s):
    level = 0
    p = 0
    for ch in s:
        if ch == '(':
            level += 1
        elif ch == ')':
            level -= 1
        if level == -1:
            break
        p += 1
    return p if -1 <= level <= 0 else None


def advanced(expr):
    n_stack = []
    o_stack = []
    while expr:
        ch, expr = expr[0], expr[1:]
        if ch == ' ':
            continue
        if ch == '(':
            p = find_closing_paren(expr)
            sub_expr, expr = expr[:p], expr[p + 1:]
            n, _ = advanced(sub_expr)
            if o_stack:
                n_stack.append(o_stack.pop()(n_stack.pop(), n))
            else:
                n_stack.append(n)
        elif ch in '123456789':
            if o_stack:
                n_stack.append(o_stack.pop()(n_stack.pop(), int(ch)))
            else:
                n_stack.append(int(ch))
        elif ch == '+':
            o_stack.append(lambda a, b: a + b)
        elif ch == '*':
            p = find_closing_paren(expr)
            sub_expr, expr = expr[:p], expr[p + 1:]
            n, _ = advanced(sub_expr)
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

    start = time.perf_counter()
    print('part 2:', solution(input_records, advanced), 'time', round(time.perf_counter() - start, 4))
